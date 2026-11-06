# Consult Admin Spec — Group Consult Booking Kit

The admin-only console. One project: `Code.gs`, `Index.html`,
`appsscript.json`. Manifest: Calendar Advanced Service v3; scope
**only** full `spreadsheets` + `calendar` (no mail scopes — this app
sends no mail). Runs as the practice account.

## Access (stricter than the provider apps)

- The sign-in gate lists **only the admin's roster entry**; every
  server function re-checks the caller's token *and* that the caller
  is the admin (`authAdmin`) before returning anything. A provider
  token must get nothing from this app, even by calling functions
  directly.
- Same fleet PIN scheme (Roster AG/AH). Where the app is embedded is
  a convenience, never the security boundary.

## View 1 — Availability (oversight + edit on behalf)

- Overview: every provider's effective consult availability —
  resolved hours (with source), time zone (+ source), caps, buffers,
  calendar connection state, and computed open days — using the same
  resolution logic as the booking app (shared precedence, `ALL`
  time-off rows honored).
- Provider detail: weekly schedule, date-specific overrides, time-off
  rows, and recent submissions.
- **Edit on behalf of a provider** (for providers who won't or can't
  self-serve): save weekly hours, save a date override, add/remove
  staff TimeOff rows — including **practice-wide blocks** (one row
  with ProviderID `ALL`). On-behalf writes go to the same stores the
  provider apps use, in the same row shapes, stamped as admin-entered
  (e.g. "[Entered by <Admin> via Consult Admin]"). A weekly save also
  updates the Roster's typical-availability cell, mirroring Manage
  Availability. Provider-submitted date-specific / time-off rows may
  be deleted from here; weekly submissions are only ever superseded.

## View 2 — Emails & Booking Settings

Editors over the booking workbook's Settings tab — this is how all
client/provider wording and rules change without a redeploy:

- Client templates (confirmation / reminder / follow-up; each
  language's set if bilingual), provider templates (reminder /
  follow-up), timing & booking rules, practice & sender settings.
- Template body fields are **visual editors** (contenteditable, with
  a Link button inserting the `[text]({Token})` syntax); subjects are
  plain text; the stored format stays plain text either way.
- **Whitelist only:** the server accepts only known Settings keys,
  validates each value (numbers in range, email/URL/time-zone shapes,
  template length caps), saves under a lock, and **reads the value
  back before reporting success**. A blank template restores the
  booking app's built-in default text.
- Note for the builder: the booking app must read provider templates
  from Settings with built-in defaults equal to the prior hardcoded
  texts — ship that companion change with this view, or provider
  template edits silently do nothing.

## View 3 — Admin Tools

- **Practice snapshot:** consults today, next 7 days, next consult,
  30-day booked/cancelled counts, follow-ups outstanding.
- **Privacy & retention panel:** privacy-consent coverage since the
  current notice version; counts of manage tokens / goals briefs
  pending the retention sweep.
- **Audit viewer:** AuditLog rows in a chosen date range.
- **Exports:** audit CSV; bookings CSV over **whitelisted columns
  only — the ManageToken hash is never exported**; audit PDF
  (in-memory HTML→PDF, ~2,000-entry cap with a truncation note). No
  new scopes for any of this.

## Boundaries

- Admin Tools data never leaves this app: no provider-facing surface
  shows stats, audit rows, or exports.
- This app writes Settings values and availability stores only — it
  never edits Appointments rows (corrections to a booking are made in
  the sheet by hand, where the AuditLog can see them).
- Because it is admin-only and not provider-visible, keep it **out**
  of any provider-facing changelog/announcement surface the practice
  runs.
