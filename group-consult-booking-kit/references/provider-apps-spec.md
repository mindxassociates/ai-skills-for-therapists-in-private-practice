# Provider Apps Spec — Manage Availability + My Consults

Both apps are provider-facing, portal-styled, PIN-gated, and run as
the practice account. Build them as separate projects (providers
bookmark them separately), sharing the patterns below.

## The shared PIN gate (fleet scheme — identical in every provider app)

- Sign-in = name dropdown (live from the Roster) + 4-digit PIN.
- Server stores/verifies against the **Roster**: column AG holds
  SHA-256 hex of `ProviderID:PIN`; column AH holds the session token
  the browser presents after sign-in (remember-me per device).
- First use with an empty AG cell = create-your-PIN flow (only while
  empty). Admin resets by clearing that provider's AG + AH cells.
- **5 wrong tries → 15-minute lockout**, kept in script cache.
  Prune rule: delete a lockout entry only if missing or its
  lock-until is set **and** past — deleting on `until <= cutoff`
  removes still-counting entries (until = 0) on every read and the
  lockout never accumulates (a real fleet bug; don't reintroduce it).
- Every data function re-verifies `(providerId, token)` server-side
  and scopes results to that provider. Client-side hiding is not
  security, and a provider must never be able to read or write
  another provider's data by tampering with request values.
- Server functions accept the **client's exact argument shapes**
  (Manage Availability's client sends one object; My Consults'
  reference client sends two scalars to `verifyPin` — either is fine,
  but each server must match *its* client, and harnesses must call in
  the client's shapes).

## Manage Availability

Files: `Code.gs`, `Index.html`, `appsscript.json`. Manifest: Calendar
Advanced Service v3; scopes full `spreadsheets`, `calendar`,
`gmail.send` **and** `script.send_mail` (it mails submission receipts
via MailApp — declare both). Workbook constants: the submissions
sheet ID (its own store), the booking workbook ID (read for the
panel; writes nothing there), the Roster ID (PIN + accepting toggle).

Views/sections, in order after sign-in:

1. **My Current Availability** (read-only panel): the provider's
   resolved weekly hours with source labeled (latest submission vs.
   Availability-tab fallback), date-specific hours on record, time
   off on record, their consult settings, and the **open consult
   slots for the next 7 days** computed with the booking app's exact
   precedence (TimeOff tab incl. `ALL` rows > date-specific >
   provider time-off > weekly; minus free/busy, minus bookings, with
   buffer/duration/step/min-notice/cap). Providers whose calendar
   isn't connected see their record plus a "connect your calendar to
   see open slots" note — never invented slots. Refresh button +
   auto-refresh after a successful submission.
2. **Accepting New Clients toggle** — writes the provider's *own*
   Roster cell (found by header name) under their verified identity;
   the daily roster sync carries it into the booking Providers tab.
3. **Consult Booking Settings card** — auto-save (debounced, Saving…/
   Saved note, revert on failure, **no Save button, no email per
   change**): ONE frequency cap (toggle + count + Day/Week/Month →
   exactly one cap column written), minimum-notice dropdown,
   buffer-before/after dropdowns. Stored as a `Consult Limits`
   submission row (latest wins); card values win over the weekly
   form's.
4. **Submission form** — three request types, each appends submission
   rows and sends a receipt email to the practice inbox (+ writes the
   Roster "typical availability" summary cell on weekly saves):
   - **Weekly Availability:** per-day blocks (multiple per day =
     split days), time zone (a **full** zone list — providers may
     live/travel outside the home country; the reference list has 21
     zones across the Americas, Europe, and Asia-Pacific), slot-step
     increment (5 min – 2h), minimum notice, "Applies to: Initial
     Consultations / Therapy Sessions / Both" flag.
   - **Date Specific Hours:** one or more dates, blocks or
     Unavailable, one submission row per date.
   - **Time Off:** a date range.
   - Any submission flagged Therapy Sessions or Both gets a
     **"MANUAL FOLLOW-UP NEEDED"** line in the receipt email —
     therapy-schedule changes are made by hand in the EHR, never by
     this system. Consult bookings honor a time-off range regardless
     of the Applies-to flag (a provider who is away gets no new
     consults).

## My Consults

Files: `Code.gs`, `Index.html`, `appsscript.json`. Manifest: **only**
full `spreadsheets` (it reads Appointments and writes one column —
no calendar, no mail scopes; don't copy a sibling app's manifest).

- Reads the booking workbook's Appointments tab live, matched by
  header name.
- Views: Upcoming (default) · Past · Cancelled · All time.
- A provider sees **only their own** rows (`canSee` check
  server-side). The practice admin's roster entry sees all rows and
  gets a provider filter.
- Click a row → full detail: client contact, payment, goals, times in
  both the provider's and the client's zones, booking ID, consent
  timestamp/version.
- **Mark as no-show** on past rows still `Booked`, behind an in-page
  confirmation card (never a native `confirm()`). Sets Status =
  `No-show`, which also drops the booking out of the follow-up sweeps
  — prompt marking is how a provider suppresses a follow-up that
  shouldn't go out.

## Styling

Provider apps use the practice's **internal portal** style (whatever
the practice's other provider tools look like — one shared header/
brand bar copied verbatim across the fleet, not improvised per app).
The public booking page's flat website style does *not* belong here,
and this portal style does not belong on the public page.
