# Architecture & Data Model — Solo Consult Booking Kit

How the two apps, one workbook, and one calendar fit together, and the
exact simplifications from the group-practice original.

## Components

| Piece | What it is | Runs as | Access |
|---|---|---|---|
| Booking app | Public wizard + client manage (reschedule/cancel) page. Apps Script project: `Code.gs`, `Index.html`, `Manage.html`, `appsscript.json`. | Owner (`USER_DEPLOYING`) | Anyone (anonymous) |
| Owner Console | Private app: My Consults + Availability + Settings & Tools. Apps Script project: `Code.gs`, `Index.html`, `appsscript.json`. | Owner (`USER_DEPLOYING`) | Anyone at the URL, but every view and server call is behind the owner PIN gate |
| Booking workbook | One private Google Sheet — all config, availability, bookings, settings, audit. Never shared publicly; ideally shared with nobody. | — | Owner only |
| Consult calendar | Owner's primary calendar, or a dedicated calendar in the same Workspace account. | — | Owner |

There is **no third app**. The group edition's Connect Your Calendar
app is unnecessary for a solo owner (see SKILL.md — "What the solo
edition deliberately drops"). There is also no separate roster
workbook, no submissions workbook, and no provider portal.

## The one workbook

Tabs, columns, and who writes them:

- **Config** — exactly one data row (the owner). Columns:
  `Name | Credentials | Active | AcceptingNewClients | CalendarID |
  TimeZone | LicensedStates | InsuranceAccepted | Languages |
  AgesServed | ClientTypes | SlidingScale | ServesInternational |
  BioLink | WorkEmail | PhotoURL | Notes`, plus the PIN columns
  `PinHash | PinToken` (see Console spec). Written by: owner by hand,
  and the Console (Accepting toggle, PIN setup).
  - `CalendarID`: primary calendar = the owner's email address;
    dedicated calendar = its ID from Google Calendar settings.
  - `InsuranceAccepted` is free text listing panels/EAPs/funds exactly
    as the owner names them; the booking wizard turns it into payment
    options on every page load.
- **Availability** — fallback weekly hours, one row per day-block:
  `Day | StartTime | EndTime | TimeZone | Source | Notes`. Multiple
  rows per day = split days. Written by: owner by hand (rarely), kept
  as the fallback if a Console availability submission can't be read.
- **AvailabilityLog** — append-only log of Console submissions (the
  solo replacement for the group's separate submissions sheet). One
  row per submission:
  `Timestamp | RequestType | AvailabilityFor | <Mon–Sun day cells> |
  SpecificDates | TimeOffStart | TimeOffEnd | TimeZone |
  SlotStepMinutes | Notes | BookingSettingsJSON`.
  Request types: `Weekly Availability`, `Date Specific Hours`,
  `Time Off`, `Consult Settings` (the auto-saved limits/notice/buffer
  card appends one of these). Latest submission of each kind wins.
- **TimeOff** — staff-entered hard blocks:
  `StartDate | EndDate | Notes`. (No ProviderID column is needed —
  there is one provider. A row blocks consults for its whole range.)
- **Appointments** — the booking record, one row per consult:
  `BookingID | CreatedAt | Status | StartISO | EndISO |
  ProviderTimeZone | ClientTimeZone | ClientName | ClientEmail |
  ClientPhone | State | City | PaymentType | PaymentName | Language |
  ForWhom | GoalsBrief | PriorTherapy | AffordIfOON | HeardAbout |
  CalendarEventID | ManageToken | ReminderSent | CancelledAt | Notes |
  ClientFollowUpSent | OwnerFollowUpNote | UiLanguage |
  OwnerReminderSent | PrivacyConsentAt | PrivacyConsentVersion`.
  Status: `Booked | Cancelled | No-show | Completed` (only `Booked`
  rows are processed by reminder/follow-up sweeps).
  `ManageToken` stores **only the SHA-256 hash** of the client's
  manage token — never the token itself.
- **Settings** — `Key | Value | Notes`, one row per key (full key list
  with defaults is in `booking-app-spec.md`). Written by: seeded by
  `setupSheet()`, edited day-to-day in the Console's Settings view.
  Both apps re-read Settings on every run, so edits apply with no
  redeploy.
- **AuditLog** — append-only, sheet-protected:
  `Timestamp | BookingID | Action | Actor | Details` with Action in
  `BOOKED | CANCELLED | RESCHEDULED | RETENTION_SWEEP`. IDs and times
  only — no PHI. Written by the Booking app; viewed/exported in the
  Console.

## Availability resolution (the booking page's math)

For a given date, open slots are computed as:

1. **Base hours**, first match wins:
   a. **Date-specific hours** for that date (latest `Date Specific
      Hours` submission) — replaces weekly hours for that date,
      including "unavailable that date."
   b. **Weekly hours** from the latest `Weekly Availability`
      submission.
   c. **Availability tab** rows (fallback).
2. **Subtract blocks**, in this precedence:
   - TimeOff tab rows (hard block — beats date-specific hours).
   - Time-off ranges from the AvailabilityLog (block the whole range).
   - Your calendar's **free/busy** for the window (one batched
     Calendar API call; busy titles/descriptions are never read).
   - Existing `Booked` Appointments.
   - The configured buffer around busy times.
3. **Apply rules:** slot start times on the provider's slot-step grid
   (Console setting wins, else the Settings default of 30 min);
   nothing sooner than the minimum notice (Console setting wins, else
   Settings default 12h); nothing beyond the booking window
   (default 14 days); the consult-frequency cap if set (one active
   cap — per day *or* week *or* month — counting only `Booked`
   consults in your time zone).
4. **Time zones are explicit everywhere.** Weekly hours are
   interpreted in the time zone declared with them (the Console
   pre-selects your device zone; the latest declared zone wins).
   Slots are stored as ISO instants and displayed to each viewer in
   their own zone. DST transitions must not shift a 9:00 AM local
   slot — compute in the declared zone, don't do naive UTC math.

If the calendar can't be read for the window, the owner simply offers
no slots (and the reason lands in the execution log) — the page never
guesses availability it can't verify.

## Booking flow (server side)

1. Client completes the wizard → server validates every field again
   (client-side checks are UX only): email shape, phone length,
   required fields, state/payment values against Config, start time
   is a real offered slot.
2. Duplicate guard: if the same email **or** normalized phone already
   holds an upcoming `Booked` consult, refuse with the "you already
   have a consultation — use your manage link or contact us" message.
   Honeypot field + per-contact and global attempt throttles reject
   bot submissions (fail-open: a cache outage must never block a
   legitimate client).
3. Under `LockService`, re-check free/busy + bookings for the chosen
   slot. If it was just taken, return the client to refreshed slots —
   exactly one of two racing bookings may succeed.
4. Create the calendar event (generic title, call-minimum
   description, **no attendee**), write the Appointments row (status
   `Booked`, manage-token hash, privacy-consent timestamp + version),
   append the AuditLog entry.
5. Email the client (confirmation + .ics + manage link, in the
   language they booked in) and the owner (triage minimum). Any email
   failure is logged; the booking itself never rolls back silently —
   the Appointments row is the record.

## Timers (installed once by `setupTriggers()`)

- **Every 5 minutes — the sweep:** send due client reminders (~24h
  before, once per booking), owner reminders (once per booking; a
  reschedule clears the marker so the new time gets its own), client
  follow-up survey emails (after the consult ends + configured delay,
  once), and the retention pass.
- **Daily — retention:** clear manage-token hashes 7 days after the
  appointment ends; redact `GoalsBrief` after `BookingRetentionDays`
  (default 90). Log each sweep action to AuditLog.
- Cancelled and no-show appointments never trigger reminders or
  follow-ups.

## Client manage page (reschedule / cancel)

The confirmation email's link carries the raw manage token; the page
looks the booking up by its hash. Tokens expire 48 hours after the
appointment ends, and rotate whenever a new manage link is emailed
(reminder emails re-issue). Reschedule re-runs the slot search for the
same fit criteria, moves the calendar event, updates the row, rotates
the token, and emails both parties. Inside the reschedule/cancel
cutoff (default 4h), online changes are refused with a "contact the
practice" message and nothing is altered. A tampered token shows
"link is not valid" and reveals nothing.

## Design rules that carry over unchanged from the group edition

- Sheet data loads once per request; availability uses **one batched
  free/busy call**, not one call per day.
- Payment options, states, and languages in the wizard are generated
  from Config on every page load — never hardcoded.
- Therapy-session availability is **not** this system. Consult hours
  are consult hours; changes to ongoing therapy scheduling stay in
  the owner's EHR / calendar by hand.
- No waitlist, no payments, no SMS, no third-party services, no
  analytics/trackers on the public page.
