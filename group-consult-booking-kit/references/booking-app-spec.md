# Booking App Spec — Group Consult Booking Kit (Public App)

The single public front door. Build to this spec; `architecture.md`
holds the shared data model, routing, and availability math.

## Files & manifest

Project files: `Code.gs`, `Index.html` (wizard), `Manage.html`
(reschedule/cancel), `appsscript.json`. Three config constants at the
top of `Code.gs`: the Booking workbook ID, the Manage Availability
submissions sheet ID, and the Roster workbook ID (sync tooling only).

Manifest essentials:

- Calendar Advanced Service **v3** enabled (identifier `Calendar`).
- OAuth scopes — all of these, no more:
  `spreadsheets` (full — opens three workbooks by ID and writes;
  readonly makes `openById` throw), `calendar`, `calendar.events`,
  `gmail.send` (GmailApp client mail incl. send-as alias),
  `gmail.settings.basic` (**only** if client mail sends from an
  alias — without it alias sends throw and mail silently falls back
  to the bare account), `script.send_mail` (MailApp practice/provider
  notifications — not covered by `gmail.send`), `script.scriptapp`
  (triggers).
- Web app: execute as **Me** (practice account), access **Anyone**
  (anonymous). All authorization is server-side; the public has
  nothing sensitive to call.
- Project time zone = the practice's zone (logging/display only; all
  booking math is explicit-zone).

## The wizard (Index.html)

Flat website styling in the practice's branding (owner supplies
fonts/colors). No portal glass, no Google branding, no native
dialogs; minimum body font 13px.

1. **Location.** U.S. state dropdown, or "Outside the U.S." (+
   required free-text location). Drives licensure + international
   rules.
2. **Payment.** Options **generated from the Providers tab on every
   load** (grouped Insurance / EAP / Fund), plus Self-pay, plus
   Sliding scale if any eligible provider offers it. Outside-U.S. →
   only Self-pay + Sliding scale, with the can't-bill-insurance-
   abroad note.
3. **Preferences.** Who it's for (adult / teen / child / couple /
   family), therapy-language preference, provider gender preference
   (hidden + ignored if a preferred clinician is named — enforced in
   both the UI and server validation, so a stale value can never
   apply), preferred clinician (optional).
4. **Choose clinician + time.** Eligible provider cards (photo, name,
   credentials, languages, bio link — second-language names when the
   UI is in that language) with real slots in the visitor's zone. No
   eligible provider or no workable time → the no-match view (contact
   email + "mention your preferred clinician's name").
5. **Details + privacy acknowledgment.** Name, email, phone, city,
   brief goals (**≤600 chars**, visible warning against detailed
   clinical history), prior-therapy yes/no, out-of-network
   affordability, how-heard (optional), and **two required
   acknowledgments** (free consult, not a crisis service; the privacy
   notice linked to the practice policy). Server enforces both;
   stores `PrivacyConsentAt` + `PrivacyConsentVersion`. Honeypot
   field included.

**Confirmation screen:** provider, date/time in the client's zone,
booking ID, what happens next (that provider will call the number
given).

**Second language (optional):** one translated question set, toggle
on both public pages, `?lang=` URL support, `UiLanguage` stored per
booking, all client emails in the booking's language (templates in
Settings beside the English ones; a cleared translation falls back to
English), provider names from the roster's second-language column.

## Emails

Templates live in the booking workbook's Settings tab (edited in
Consult Admin; blank = built-in default in code). HTML + plain-text;
`[Link text]({Token})` / `[text](https://…)` renders as an anchor in
HTML and `text (url)` in plain text.

- **Client confirmation:** `ConfirmationSubject/Body`, tokens
  `{ClientFirstName}`, `{EventDateTime}`, `{ProviderName}`; the app
  appends an appointment-details block (provider, time in client zone
  + provider zone when different, the phone number the provider will
  call, booking ID, manage link) and attaches an .ics.
- **Client reminder** (~24h): `ReminderSubject/Body`; carries the
  manage link (issuing it rotates the token).
- **Client follow-up** (after end + delay): subject/body + survey URL;
  skipped and logged if unconfigured — never send half-configured.
- **Practice notification** (at booking, to practice inbox + the
  provider's work email): **triage minimum only** (booking ID, when,
  provider, state/city, payment, language, for-whom, international
  flag line when applicable); **no client name in the subject** —
  BookingID instead.
- **Provider reminder** (~24h, to the provider's work email):
  `ProviderReminderSubject/Body` with `{ProviderFirstName}`,
  `{ClientName}`, `{ClientPhone}`, `{EventDateTime}` + a My Consults
  link. Sent once per booking; reschedule re-arms it.
- **Provider follow-up** (after end + delay):
  `ProviderFollowUpSubject/Body`, `{FirstName}`, `{FormURL}`;
  admin-configured exclusions (e.g. the practice owner) honored.
- **Reschedule / cancellation notices** to client + practice.
- **Crisis footer on every client email** (not a crisis service,
  email unmonitored, U.S. → 911 + 988; international → local
  emergency services), appended centrally in the send function so no
  template edit can lose it.

Client mail sends from the configured alias (`ClientFromEmail` /
`ClientFromName`) via GmailApp with logged fallback to the practice
account address. Ship a test-send function and verify the From header
on the arrived email after deploy.

## Calendar events (minimization — do not "improve")

Title exactly `Initial Consultation — <BookingID>`; description =
booking ID, phone to call, language, for-whom, and "Free
<duration>-minute initial consultation booked through
<PracticeName>." (+ the international flag line when applicable);
**no attendee, no goals text**. Reschedule deletes + recreates the
same way, marked "(Rescheduled)".

## Settings keys (defaults; Consult Admin edits them)

`PracticeName`, `PracticeContactEmail`, `PracticeNotificationEmail`,
`ClientFromEmail`, `ClientFromName`, `ReplyToEmail`,
`PracticeWebsite`, `PrivacyPolicyURL`, `DefaultTimeZone`,
`AppointmentDurationMinutes` (15), `SlotStepMinutes` (30),
`BufferMinutes` (10), `BookingWindowDays` (14),
`DefaultMinNoticeMinutes` (720), `RescheduleCutoffHours` (4),
`CancelCutoffHours` (4), `ReminderHoursBefore` (24),
`ClientFollowUpDelayMinutes` (5), `ProviderFollowUpDelayMinutes` (5),
`BookingRetentionDays` (90), `PreventDuplicateActiveBooking` (Yes),
`BookingAttemptLimitPerContact` (8), `BookingAttemptWindowMinutes`
(10), `BookingAttemptGlobalLimit` (120), `SurveyURL`,
`NextStepsFormURL`, template keys (`Confirmation…`, `Reminder…`,
`ClientFollowUp…`, `ProviderReminder…`, `ProviderFollowUp…` subject +
body, plus per-language variants if bilingual).

`PRIVACY_NOTICE_VERSION` is a code constant — bump it whenever the
Step 5 wording changes.

## Server functions the build must include

- `doGet` (wizard / Manage page by `?manage=`), availability search,
  book, reschedule, cancel — full server-side validation; **clients
  see only fixed localized error strings**, raw exceptions only in
  the execution log.
- `setupSheet()` — create missing tabs with the exact headers in
  `architecture.md`, seed Settings; idempotent, self-healing
  (AuditLog included).
- `syncProvidersFromRoster()` — per architecture; preserves
  CalendarID/TimeZone/Active/Notes.
- `checkSetup()` — the go-live audit: per provider, calendar access
  role for the practice account (must be `writer` or `owner` —
  free/busy-only sharing can display times but every booking will
  fail, and the report must say so), free/busy probe, weekly-hours
  block count + source, effective time zone + source, consult caps
  and buffers. No provider goes live until their line is clean.
- `setupTriggers()` — 5-minute sweep, daily roster sync, daily
  retention. Run once per fresh project; pasted code brings no
  triggers.
- **The Connect API (`doPost`)** — the token-checked JSON API the
  Connect Your Calendar app calls (full contract in
  `connect-your-calendar-spec.md`): `listProviders`, `verifyPin`,
  `setupPin`, `checkToken`, `registerCalendar`, `clearCalendar`,
  `calendarStatus`. All roster/sheet work happens here, server-side;
  generic error text on failure.
- Test-send function for the client From alias.

## Performance & quotas

Sheet data loads once per request; slot search = **one batched
free/busy call for all eligible providers**, slots capped (e.g. 120
per provider). Workspace mail quota (~1,500/day) is far above consult
volume for any realistic group. Lock + throttles are the only
background machinery.
