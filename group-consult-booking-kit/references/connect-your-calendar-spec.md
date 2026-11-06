# Connect Your Calendar Spec — Group Consult Booking Kit

**Why this app exists (group edition only).** The booking system runs
as the practice account. It can only read free/busy and create events
on a provider's calendar if that calendar is shared with the practice
account at **"Make changes to events"** (writer). Asking every
provider to do that by hand in Google Calendar settings is slow and
error-prone; this app lets each provider do it themselves, signed in
as themselves, in about 30 seconds. The solo edition has no such app
because a solo owner already owns the only calendar involved.

## Shape

Project files: `Code.gs`, `Index.html`, `appsscript.json`.

- **Deployment is the whole trick:** Execute as **User accessing the
  web app**, access Anyone. The app acts *as the provider* for
  exactly one job — sharing/unsharing their calendar — and for
  nothing else.
- Manifest: Calendar Advanced Service v3; scopes **exactly**
  `calendar`, `script.external_request` (calling the Booking app's
  API), `userinfo.email`. **No spreadsheets scope** — this app never
  touches a workbook.
- Two config constants baked into `Code.gs` before deploy:
  `BOOKING_API_URL` (the deployed Booking app `/exec` URL — which is
  why this app is built *after* the Booking app) and `ADMIN_EMAIL`
  (the practice account, the share target). Bake the real values into
  the source of truth; a placeholder left in a redeploy wipes the
  live configuration (this has happened in production).

## Provider flow (Index.html, portal styling)

1. Pick your name from the provider list (fetched live from the
   Booking app's API), enter your fleet PIN — or create one if none
   is set (same PIN as Manage Availability / My Consults; the Booking
   app verifies it against the Roster, this app holds no credentials).
2. Authorize with **your own Google account** when Google prompts —
   the app needs to act as you to share your calendar.
3. Pick the calendar your work schedule lives on → **Connect.** The
   app shares that calendar with the practice account ("Make changes
   to events"), registers its ID with the Booking app, then **reads
   the status back from the booking system's side** and shows it
   ("Booking system check: connected") — what the provider sees is
   the ground truth, not the local share's say-so.
4. **Disconnect** (switching calendars, offboarding) is the same
   screen: removes the share and clears the registration.

## The Booking-app API it consumes (booking app's `doPost`)

JSON POSTs; every call after sign-in carries the provider's token;
the booking app re-verifies it against the Roster on every call.

| Action | Does |
|---|---|
| `listProviders` | Roster provider list (id, name, hasPin) |
| `verifyPin` | Checks PIN (5-try/15-min lockout), returns session token |
| `setupPin` | First-time PIN creation (only while the Roster PIN cell is empty) |
| `checkToken` | Remember-me validation |
| `registerCalendar` | Writes the CalendarID into the booking workbook's Providers tab (+ provenance note), returns whether the practice account's access is confirmed writer/owner |
| `clearCalendar` | Clears the CalendarID (+ note) |
| `calendarStatus` | The booking side's view: connected?, calendarId, accessRole |

This app never reads the Roster or booking workbook directly — by
design. All authorization decisions happen in the Booking app.

## Google OAuth verification — read before you promise timelines

Because this app runs as arbitrary users and requests the (sensitive)
calendar scope, real-world deployment hits Google's app-verification
regime. Plan for it honestly:

- **Unverified-app screen:** until Google verifies the app, providers
  on personal Google accounts will see "Google hasn't verified this
  app." They can proceed via **Advanced → Go to Connect Your
  Calendar** — it's the practice's own app. The provider page must
  warn them to expect this screen, in plain language, before they hit
  it (in every language the practice onboards in). Providers on the
  practice's own Workspace domain may not see it at all.
- **Verification is submittable and free** for sensitive scopes (the
  paid security assessment applies to *restricted* scopes, not this
  one). Preparing the packet: privacy policy URL with a specific
  section describing this app's calendar use and Google's Limited Use
  requirements; OAuth consent screen values; a per-scope
  justification for each of the three scopes; a short demo video
  showing the OAuth flow and exactly how the calendar scope is used.
- **Declare the scopes in the GCP console's Data Access section by
  hand** — the consent tooling reads the console's declared scopes,
  not the manifest. If they're missing there, the Verification Center
  will misleadingly say "verification is not required," while users
  keep hitting the unverified screen.
- **There may be no reply channel** in the Verification Center;
  follow-ups arrive by email to the practice account. Review takes
  as long as it takes — the practice can fully operate in the
  meantime via the Advanced click-through and the manual fallback
  below. Do not block the booking cutover on verification.

## Manual sharing fallback (equivalent, always available)

A provider can share by hand — Google Calendar (on a computer) →
Settings → "Settings for my calendars" → pick the real-schedule
calendar → "Share with specific people or groups" → add the practice
account at **"Make changes to events"** → Send. Then the admin sets
that calendar's ID in the booking workbook's Providers tab (a primary
calendar's ID is the provider's email address). Result is identical
to the app's; `checkSetup()` confirms it the same way. Ship providers
a short help article covering: the unverified-app warning (for the
app route), these manual steps, how to change the shared calendar,
and how to remove the share when leaving the practice.

## Failure notes

- "See only free/busy" sharing is enough to *display* times but
  every booking fails — `checkSetup()` flags it per provider; the fix
  is re-sharing at writer level, not debugging the booking app.
- A provider authorizing with the *wrong* Google account (not the one
  that owns their schedule calendar) connects the wrong calendar;
  the status read-back + a test booking per provider catches it.
- Offboarding: disconnect in this app (or remove the share manually)
  **and** set the provider inactive in the Roster, then re-run the
  sync — either step alone leaves a stale path open.
