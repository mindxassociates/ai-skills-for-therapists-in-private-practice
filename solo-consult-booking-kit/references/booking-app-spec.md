# Booking App Spec — Solo Consult Booking Kit

The public app. Build to this spec; the Console spec and the
architecture reference share its workbook and vocabulary.

## Files & manifest

Project files: `Code.gs`, `Index.html` (wizard), `Manage.html`
(reschedule/cancel), `appsscript.json`.

Manifest essentials:

- Enable the **Calendar Advanced Service v3** (identifier `Calendar`).
- OAuth scopes — declare **all** of these, no more:
  - `https://www.googleapis.com/auth/spreadsheets` (full — the app
    opens its workbook by ID and writes bookings/audit/retention;
    `spreadsheets.readonly` makes `openById` throw)
  - `https://www.googleapis.com/auth/calendar`
  - `https://www.googleapis.com/auth/calendar.events`
  - `https://www.googleapis.com/auth/gmail.send` (GmailApp — client
    emails, including from a send-as alias)
  - `https://www.googleapis.com/auth/gmail.settings.basic` (**only**
    if sending from a send-as alias; required for alias sends,
    otherwise mail silently falls back to the bare account address)
  - `https://www.googleapis.com/auth/script.send_mail` (MailApp —
    owner notifications; `gmail.send` does **not** cover MailApp)
  - `https://www.googleapis.com/auth/script.scriptapp` (installing
    the time-driven triggers)
- Web app: execute as **Me** (the owner), access **Anyone**
  (anonymous visitors must be able to book). All authorization
  decisions are server-side; the public simply has nothing sensitive
  to call.
- Set the project time zone to the practice's zone (display/logging
  only — all booking math uses explicit zones).

There is deliberately **no** `script.external_request` scope: the app
calls no third-party APIs. (In the group edition that scope belonged
to the separate calendar-connection app, which the solo edition
doesn't have.)

## The wizard (Index.html)

Flat website styling in the practice's own branding (owner supplies
fonts/colors in the setup interview). No portal glass, no Google
branding, no native dialogs. Minimum body font 13px. Steps:

1. **Location.** State (dropdown of U.S. states) or "Outside the
   U.S." (+ required free-text location). State gates licensure:
   if the client's state isn't in Config `LicensedStates` (and, for
   outside-U.S., Config `ServesInternational` isn't Yes), show the
   no-fit message (below) — don't collect further data.
2. **Payment.** Options generated from Config `InsuranceAccepted`
   (grouped Insurance / EAP / Fund by the owner's naming) plus
   Self-pay, plus Sliding scale if Config `SlidingScale` is Yes.
   Outside-U.S. clients see **only** Self-pay and Sliding scale, with
   a note that insurance/EAP can't be billed for therapy outside the
   U.S. If the chosen payment is one the owner doesn't accept, no-fit
   message.
3. **About the consult.** Who it's for (adult / teen / child /
   couple / family — checked against Config `AgesServed` /
   `ClientTypes`), therapy-language preference (Config `Languages` +
   "No preference"), prior therapy yes/no (optional). A mismatch is a
   no-fit message, not an error.
4. **Pick a time.** Open slots from the availability math in
   `architecture.md`, shown in the visitor's own time zone (detected,
   changeable). If none in the window: a clear "no openings in the
   next N days — email us" message.
5. **Your details + privacy acknowledgment.** Name, email, phone,
   city, brief goals (**≤600 characters**, with a visible warning:
   "Please don't share detailed clinical history here — this is for
   scheduling; you'll discuss details in your consultation"),
   how-they-heard (optional), and **two required acknowledgments**:
   the consult is free and not a crisis service, and the privacy
   notice (linked to the practice privacy policy). Server enforces
   both and stores `PrivacyConsentAt` + `PrivacyConsentVersion`.
   Hidden honeypot field included.

**No-fit message (any step):** kind, specific, and useful — "We're
not able to offer a consultation for [reason category]. If you think
this is a mistake, or you'd like a referral, email
<practice contact>." Never a form error, never a partial record.

**Confirmation screen:** your name, date/time in the client's zone,
booking ID, what happens next (you will call them at the number they
gave), and the manage-link note.

**Second language (optional):** if the owner books in a second
language, ship one translated question set (same questions, collective
voice where the language uses one), a toggle on both public pages,
`?lang=` support on the URL, the booking's `UiLanguage` stored, and
all client emails sent in that language (templates in Settings next
to the English ones; a cleared second-language template falls back to
English).

## Emails

All templates live in the Settings tab (tokens below); blank =
built-in default text ships in code. HTML + plain-text parts; the
HTML is a simple branded shell (practice accent color, ink text).
Link syntax in templates: `[Link text]({Token})` or
`[text](https://…)` renders as an anchor in HTML and as
`text (url)` in plain text.

- **Client confirmation** (at booking): subject/body templates
  `ConfirmationSubject` / `ConfirmationBody`; tokens
  `{ClientFirstName}`, `{EventDateTime}`, `{ProviderName}`. The app
  appends an "Appointment details" block (your name, time in the
  client's zone + your zone when different, the phone number you will
  call, booking ID, manage link) and attaches an .ics file.
- **Client reminder** (~24h before): `ReminderSubject` /
  `ReminderBody`. Carries the manage link — sending it rotates the
  token if a new link is issued.
- **Client follow-up** (after the consult + delay): subject/body +
  `{SurveyURL}`; skipped (and logged) if templates/URL are unset —
  never send a half-configured email.
- **Owner notification** (at booking): **triage minimum only** —
  booking ID, when, state/city, payment type/name, language, for-whom.
  **No client name in the subject** (use the BookingID). Full details
  live in the Appointments tab / Console.
- **Owner reminder** (~24h before): this one is to you, from the
  system, and may carry the client name + phone + a Console link,
  since it stays inside your Workspace mailbox.
- **Reschedule / cancellation notices** to both parties.
- **Crisis footer on every client email:** the practice is not a
  crisis service, email isn't monitored for emergencies, U.S. clients
  → 911 + 988 Suicide and Crisis Lifeline; outside-U.S. bookings get
  a local-emergency-services variant. Appended centrally in the send
  function so no template edit can lose it.

Client emails send from the owner's address or a configured send-as
alias (`ClientFromEmail` / `ClientFromName` in Settings) via GmailApp;
on alias failure, log and fall back to the account address so no
email is lost. After deploying, run the built-in test-send function
and confirm the From header on the arrived email.

## Calendar event (minimization — do not "improve" this)

- Title: `Initial Consultation — <BookingID>` (exactly; no name).
- Description: booking ID, the phone number to call, therapy
  language, for-whom, and the line "Free <duration>-minute initial
  consultation booked through <PracticeName>." For outside-U.S.
  bookings add: "International client — therapy is private pay only;
  confirm you may serve clients in their location."
- **No client attendee.** No goals text, ever.
- Reschedules delete the old event and create the new one the same
  way, noted "(Rescheduled)" in the description.

## Settings keys (defaults — owner-editable in the Console)

`PracticeName`, `PracticeContactEmail`, `PracticeNotificationEmail`,
`ClientFromEmail`, `ClientFromName`, `ReplyToEmail`,
`PracticeWebsite`, `PrivacyPolicyURL`, `DefaultTimeZone`,
`AppointmentDurationMinutes` (15), `SlotStepMinutes` (30),
`BufferMinutes` (10), `BookingWindowDays` (14),
`DefaultMinNoticeMinutes` (720), `RescheduleCutoffHours` (4),
`CancelCutoffHours` (4), `ReminderHoursBefore` (24),
`ClientFollowUpDelayMinutes` (5), `BookingRetentionDays` (90),
`PreventDuplicateActiveBooking` (Yes),
`BookingAttemptLimitPerContact` (8), `BookingAttemptWindowMinutes`
(10), `BookingAttemptGlobalLimit` (120), `SurveyURL`,
`ConfirmationSubject/Body`, `ReminderSubject/Body`,
`ClientFollowUpSubject/Body`, `OwnerReminderSubject/Body`
(+ `…Zh`-style suffixed variants for each client template if a second
language is enabled).

`PRIVACY_NOTICE_VERSION` is a code constant, not a Setting — bump it
whenever the Step 5 privacy wording changes, so each booking proves
which notice the client accepted.

## Server functions the build must include

- `doGet` — wizard, or the Manage page when `?manage=<token>` is
  present.
- Availability search + booking + reschedule + cancel endpoints with
  full server-side validation; **clients only ever see fixed,
  localized error strings** — raw exception text goes to the
  execution log only.
- `setupSheet()` — create any missing tabs with the exact headers in
  `architecture.md`, seed Settings defaults. Idempotent; self-heals
  missing columns/tabs on later runs (e.g., AuditLog creation).
- `checkSetup()` — the go-live audit, run from the editor: reports
  the Config row (calendar ID, time zone + source, accepting status),
  the calendar's access role for the script owner (must be `owner`
  for your own calendar — anything less means the CalendarID is
  wrong), a free/busy probe, weekly-hours block count (0 = you can
  never appear), and the current consult cap/buffers. Read its log
  output before embedding the page.
- `setupTriggers()` — install the 5-minute sweep + daily retention.
  Run once per project; pasted code never brings triggers with it.
- Test-send function for the client From alias (see Emails).

## Performance & quotas

Sheet data loads once per request; slot search uses one batched
free/busy call for the whole window and caps returned slots (e.g.
120). Workspace mail quotas (~1,500/day) are far above consult
volume. The lock + throttles are the only background machinery.
