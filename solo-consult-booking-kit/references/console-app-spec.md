# Owner Console Spec — Solo Consult Booking Kit

One private app that merges the group edition's three staff apps —
**Manage Availability**, **My Consults**, and **Consult Admin** —
because in a solo practice the provider and the admin are the same
person. One PIN, one URL, three views.

## Files, manifest, access

Project files: `Code.gs`, `Index.html`, `appsscript.json`.

- Scopes: full `spreadsheets`; `calendar` + the Calendar Advanced
  Service v3 (the Availability view computes real open slots with
  free/busy, using the booking app's own precedence); `gmail.send`
  **and** `script.send_mail` if the console sends any mail (the
  reference console sends an owner notification on availability
  submissions — if you drop that email, you may drop the mail scopes;
  never declare one mail scope and call the other API).
- Web app: execute as **Me**, access **Anyone** — the PIN gate, not
  Google sign-in, is the boundary (same pattern as the group portal
  apps), and every server function re-verifies the token
  server-side. Client-side hiding is not security.

## Sign-in (owner PIN)

- The gate offers exactly one identity: the owner from the Config
  tab. No dropdown of providers.
- PIN: exactly 4 digits, chosen by the owner on first use (only while
  no PIN is set). Stored **only** as a SHA-256 hash of
  `SOLO:<pin>` (any fixed per-install prefix string is fine — pick
  one, e.g. the string `OWNER`, and never change it after PINs exist)
  in Config `PinHash`; a random session token in `PinToken` is what
  the browser presents on later calls (remember-me on the device).
- **5 wrong tries → 15-minute lockout**, kept in CacheService.
  Prune rule (learned the hard way): delete a lockout entry only if
  it's missing or its lock-until timestamp is set **and** past —
  never prune on `until <= cutoff` alone, which deletes still-counting
  entries (until = 0) on every read and makes the lockout
  unreachable.
- Reset: owner clears `PinHash` + `PinToken` in the Config tab by
  hand; the next sign-in creates a fresh PIN.
- Server functions accept the client's argument shape exactly (the
  client sends one object `{token, …}` — the server reads that
  object). The test harness must call in the client's shapes.

## View 1 — My Consults

- Reads the Appointments tab live (match columns by header name,
  never by fixed position).
- Filters: **Upcoming** (default) · Past · Cancelled · All.
- Each row: date/time in the owner's zone (and the client's zone when
  different), client name, payment, status.
- Click → full detail: contact email/phone, state/city, payment
  type/name, language, for-whom, goals brief, prior therapy,
  booking ID, calendar event ID, privacy-consent timestamp/version.
- **Mark as no-show** on past appointments still `Booked`, behind an
  in-page confirmation card (no native `confirm()`). Sets Status to
  `No-show` — the booking app's sweeps only process `Booked` rows, so
  a prompt no-show mark also suppresses the follow-up email.
- No provider filter, no "see everyone's consults" — there is only
  the owner's list.

## View 2 — Availability

- **Accepting new clients** toggle: writes Config
  `AcceptingNewClients` (Yes/No) directly. Off = the booking wizard
  shows a "not currently accepting" message and offers no slots.
- **My Current Availability panel** (read-only, shown first): your
  resolved weekly hours (with their source: latest submission vs.
  Availability-tab fallback), date-specific hours on record, time off
  on record, your consult settings, and the **open slots for the next
  7 days** computed with the booking app's exact precedence
  (TimeOff tab > date-specific > time-off ranges > weekly, minus
  free/busy, minus bookings, with buffer/duration/step/min-notice and
  the consult cap). Refresh button + auto-refresh after a successful
  submission. This panel is how the owner verifies "what clients
  actually see" without making a test booking.
- **Submission form** — three request types, each appends one
  AvailabilityLog row and emails the owner a summary (the email is a
  receipt/record; the solo owner is submitting to themselves, so keep
  it brief):
  1. **Weekly Availability** — per-day time blocks (multiple blocks
     per day = split days), time zone (full zone list, not U.S.-only
     — include the zones the owner might travel to; the list in the
     reference build has 21), slot-step increment (5 min – 2 hours),
     minimum notice. Latest wins over the Availability tab.
  2. **Date Specific Hours** — pick one or more dates, set blocks or
     mark unavailable. Replaces weekly hours on those dates; only a
     TimeOff-tab row overrides it.
  3. **Time Off** — a date range; blocks consults for the whole
     range regardless of anything else in this app.
  - One flag, kept from the group edition because solo owners need it
    too: consult hours ≠ therapy hours. The form labels everything
    "initial consultations" and never claims to change ongoing
    therapy scheduling.
- **Consult Booking Settings card** (auto-save, no Save button —
  debounced, with a small Saving…/Saved note, reverting with an error
  if the write fails):
  - **One** frequency cap: toggle + count + Day / Week / Month
    (exactly one of the three cap columns is written; blank/off =
    no cap). Week = Sunday–Saturday in the owner's zone; month =
    calendar month.
  - Minimum notice (dropdown), buffer before / after (dropdowns).
  - Settings-card values win over the weekly form's values.
  - Appends a `Consult Settings` AvailabilityLog row; no email per
    change (it's a settings tweak, not a submission).

## View 3 — Settings & Tools

- **Settings editors** for the booking workbook's Settings tab,
  grouped: client email templates (confirmation / reminder /
  follow-up; plus the second language's set if enabled), owner
  reminder template, timing & booking rules, practice & sender
  settings. Template body fields are **visual editors** (content-
  editable with a Link button inserting `[text]({Token})` syntax),
  subjects are plain text. Only whitelisted keys are editable;
  values are validated server-side (numbers in range, email/URL/zone
  shapes, template length caps), saved under a lock, and **read back
  before the save is reported**. A blank template restores the
  booking app's built-in default.
- **Tools panel:**
  - Practice snapshot: consults today, next 7 days, next consult,
    last-30-days booked / cancelled counts, follow-ups outstanding.
  - Privacy & retention: consent coverage since the current notice
    version, counts of manage tokens / goals briefs pending the
    retention sweep.
  - Audit viewer: AuditLog rows in a chosen date range.
  - Exports: audit CSV, bookings CSV over **whitelisted columns only
    — the ManageToken hash is never exported**, and an audit PDF
    (in-memory HTML→PDF, cap ~2,000 entries with a truncation note).

## What the console never does

- It never edits Appointments rows other than the no-show status.
- It never deletes weekly submissions (they're only superseded);
  date-specific and time-off log rows may be deleted from this view.
- It never shows or exports manage tokens, PIN hashes, or raw tokens.
- It is never linked publicly — the URL is bookmarked/embedded on a
  private page; the PIN gate is the security boundary, the obscure
  URL is not.
