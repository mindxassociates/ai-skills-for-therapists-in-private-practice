# Architecture & Data Model — Group Consult Booking Kit

## Components

| Piece | Runs as | Access | Files |
|---|---|---|---|
| Public Booking app | Practice account (`USER_DEPLOYING`) | Anyone (anonymous) | `Code.gs`, `Index.html`, `Manage.html`, `appsscript.json` |
| Connect Your Calendar | **User accessing** (the provider) | Anyone; PIN-gated via the Booking app's API | `Code.gs`, `Index.html`, `appsscript.json` |
| Manage Availability | Practice account | Anyone at URL; PIN gate is the boundary | `Code.gs`, `Index.html`, `appsscript.json` |
| My Consults | Practice account | Anyone at URL; PIN gate | `Code.gs`, `Index.html`, `appsscript.json` |
| Consult Admin | Practice account | Anyone at URL; admin-only PIN gate (only the admin's roster entry can sign in, re-checked server-side on every call) | `Code.gs`, `Index.html`, `appsscript.json` |

The Connect app is the only project that runs as the visitor — that's
the whole point of it (see `connect-your-calendar-spec.md`). Every
other app runs as the practice account; the public never sees a sheet
or a calendar, and providers never touch the workbooks directly.

## Data stores (all owned by the practice account)

### 1. Provider Roster workbook (source of truth for people)

One tab, one row per clinician, columns identified **by header name**
in code (practices reorder columns; only the PIN columns are
positional by convention). The booking system reads: Provider ID,
names (incl. a second-language name column if bilingual), credentials,
work email, licensed states, contracted panels, languages, ages
served, client types, gender, sliding scale, serves-international,
accepting status, bio links, photo. Plus the shared PIN store:

- **Column AG — "Viewer PIN":** SHA-256 hash of `ProviderID:PIN`.
- **Column AH — "Viewer Token":** the random session token.

The Roster is also where the daily sync reads from — see below.

### 2. Booking workbook ("the booking system" proper)

- **Providers** — the booking app's working mirror of the roster:
  `ProviderID | Name | Credentials | Active | AcceptingNewClients |
  CalendarID | TimeZone | LicensedStates | InsuranceAccepted |
  Languages | AgesServed | ClientTypes | Gender | SlidingScale |
  BioLink | WorkEmail | Notes | NameZh | ServesInternational |
  BioLinkZh | PhotoURL` (drop/rename the `Zh` columns if not
  bilingual). Refreshed from the Roster by `syncProvidersFromRoster()`
  (daily trigger + on demand); the sync **preserves** CalendarID,
  TimeZone, Active, and Notes — everything else follows the roster.
- **Availability** — fallback weekly hours, one row per day-block:
  `ProviderID | ProviderName | Day | StartTime | EndTime | TimeZone |
  Source | Notes`. Used when a provider has no Manage Availability
  submission.
- **RoutingRules** — owner-defined exceptions:
  `RuleID | Type | MatchValue | ProviderID | Effect | Notes`
  (e.g. exclude a provider for a named payer or inquiry type).
- **Appointments** — one row per booking:
  `BookingID | CreatedAt | Status | ProviderID | ProviderName |
  StartISO | EndISO | ProviderTimeZone | ClientTimeZone | ClientName |
  ClientEmail | ClientPhone | State | City | PaymentType |
  PaymentName | Language | ForWhom | GenderPreference | GoalsBrief |
  PriorTherapy | AffordIfOON | HeardAbout | CalendarEventID |
  ManageToken | ReminderSent | CancelledAt | Notes |
  ClientFollowUpSent | ProviderFollowUpSent | UiLanguage |
  ProviderReminderSent | PrivacyConsentAt | PrivacyConsentVersion`.
  Status: `Booked | Cancelled | No-show | Completed`; only `Booked`
  rows are processed by the sweeps. `ManageToken` holds **only the
  SHA-256 hash** of the client's token.
- **Settings** — `Key | Value | Notes` (full key list in the booking
  spec). Read fresh on every run by every app that needs it, so
  Consult Admin edits apply with no redeploy.
- **TimeOff** — admin-entered hard blocks:
  `ProviderID | ProviderName | StartDate | EndDate | Notes`. A row
  with ProviderID **`ALL`** / name "All Providers" blocks **every**
  provider (practice-wide closure) — the booking app, Manage
  Availability's panel, and Consult Admin all honor it.
- **AuditLog** — append-only, sheet-protected:
  `Timestamp | BookingID | Action | Actor | Details`, Action in
  `BOOKED | CANCELLED | RESCHEDULED | RETENTION_SWEEP`, IDs/times
  only, no PHI.

### 3. Manage Availability submissions sheet

Append-only, one row per provider submission: timestamp, provider
name, request type (`Weekly Availability`, `Date Specific Hours`
— one row per date, `Time Off`, `Consult Limits`), availability-for
flag, per-day cells (multiple blocks per day, comma-separated),
specific dates, time zone, slot-step increment, and the consult-limit
/ notice / buffer columns. **Latest submission of each kind wins** —
weekly submissions are never deleted, only superseded.

## Routing (who a client can be matched to)

Eligibility is computed fresh per request from the Providers tab +
RoutingRules. A provider is eligible only if **all** hold:

- Active = Yes and AcceptingNewClients = Yes, has a connected
  calendar (CalendarID set and readable), and has ≥1 weekly-hours
  block from some source.
- Licensed in the client's state. Panel matching is **state-aware**:
  a panel entry carrying a state suffix (e.g. "BCBS — TX") matches
  only in that state; an unsuffixed entry matches in any licensed
  state. EAP/fund/self-pay/sliding options follow the same data.
- Serves the client's "for whom" group (ages + client types) and
  offers the requested therapy language (or the client chose
  no-preference).
- Sliding-scale requests require SlidingScale = Yes.
- Gender preference, when the client states one, filters by the
  roster Gender value — **unless the client named a preferred
  clinician**, in which case the gender question is hidden in the UI
  *and* ignored server-side (they already know that clinician).
- Outside-the-U.S. clients: only providers with ServesInternational =
  Yes, and only Self-pay / Sliding scale payment options (insurance
  and EAP can't be billed for therapy delivered outside the U.S.).
- RoutingRules exclusions remove a provider for the named match.

The wizard shows eligible providers (cards with photo, bio link,
languages) and their real slots; a preferred-clinician name, if the
practice collects one, narrows but never bypasses eligibility. No
eligible provider → a no-match message directing the client to the
practice contact email, asking them to name their preferred
clinician. **There is no waitlist.**

## Availability resolution (per provider, per date)

Same precedence everywhere (booking page, Manage Availability panel,
Consult Admin — one shared logic, three callers):

1. **Base hours**, first match wins: date-specific hours for that
   date (latest submission) → latest weekly submission → Availability
   tab.
2. **Blocks**, in precedence order: TimeOff-tab rows (incl. `ALL`
   rows) → provider time-off ranges from submissions → the provider's
   calendar free/busy (one batched Calendar API call across all
   eligible providers; only busy intervals are read, never titles) →
   existing `Booked` appointments → configured buffer around busy
   times.
3. **Rules:** the provider's slot-step grid (their submission wins,
   else Settings default 30 min); minimum notice (submission/settings
   card wins, else Settings default 12h); booking window (14 days);
   the provider's consult-frequency cap if set (one active cap —
   day *or* week (Sun–Sat, provider zone) *or* month — counting only
   `Booked` consults).
4. **Zones are explicit:** hours are interpreted in the zone declared
   with them (the latest Manage Availability declaration wins over the
   Providers tab value); slots are ISO instants, displayed per-viewer
   in their own zone; DST must not shift a 9:00 AM local slot.

A provider whose calendar errors or isn't shared at writer level is
silently omitted from results (reason in the execution log) — the
page never invents availability.

## Booking transaction

Server-validates everything again → duplicate guard (same email *or*
normalized phone with an upcoming `Booked` consult → refused, pointed
at their manage link) → honeypot + per-contact/global throttles →
under `LockService`, re-checks the slot → creates the calendar event
(generic title, call-minimum description, no attendee) on the
**provider's** calendar → writes the Appointments row (token hash,
consent timestamp/version) → AuditLog entry → emails (client:
confirmation + .ics + manage link, in their booking language;
practice notification: triage minimum, BookingID in the subject, to
the practice inbox + the provider's work email).

## Timers (Booking app, installed by `setupTriggers()`)

- **Every 5 minutes — the sweep:** client reminders (~24h before,
  once; reschedule clears markers), provider reminders (once per
  booking), client follow-up survey emails (after end + delay, once),
  provider follow-up emails (after end + delay, once; admin-configured
  exclusions honored), retention pass.
- **Daily — roster sync:** `syncProvidersFromRoster()` refreshes the
  Providers tab and emails the practice inbox when a provider is
  added or removed (a new provider still needs a calendar connection
  + hours before they can be booked).
- **Daily — retention:** clear manage-token hashes 7 days after the
  appointment ends; redact GoalsBrief after `BookingRetentionDays`
  (default 90); AuditLog each sweep action.

## Client manage page

Token in the confirmation link → looked up by hash → reschedule
(re-runs slot search for the same provider + fit criteria) or cancel,
inside the configured cutoffs (default 4h; inside → refused with a
contact-us message). Tokens expire 48h after the appointment ends and
rotate whenever a new manage link is emailed. Tampered token →
"link is not valid," nothing revealed.
