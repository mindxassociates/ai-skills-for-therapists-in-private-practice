# Build and deploy

## Build phases

Follow SKILL.md's Build order. Each phase ends with its slice of the test checklist passing before the next begins — especially: workbook/index before UI, notes before billing (invoices read signed sessions), portal last among client-facing pieces (it exposes everything beneath it).

## Manifest and scopes

Declare every scope the code actually uses, up front, in `appsscript.json` — typically: spreadsheets, Drive, Calendar (if events are written), Mail/Gmail send (matching the API actually called), and external requests only if a payment-processor check is implemented. Adding a scope to a live deployment walls the app behind an authorization error until the owner re-grants: stage code that degrades gracefully under the old manifest, re-authorise, then version and bump.

Other manifest rules: timezone set explicitly to the practice's zone (spreadsheet/script timezone drift shifts stored timestamps); web app access set deliberately (portal must reach clients; provider views are gated in code, not by deployment access alone).

## Transport discipline

`google.script.run` cannot carry `Date` objects or `NaN`/`Infinity`; one bad value nulls the entire payload and the view silently never renders. Sheets auto-converts date-shaped strings into date cells, so:

- Every date-shaped field is coerced to an ISO text string server-side before return.
- Every optional number passes a clean-number helper (blank → `''`, never `NaN`).
- Epoch integers are the safest transport for timestamps; format in the view, in the labelled timezone.

## Deploy discipline

1. Restore point: copy the current project files before pushing anything.
2. Verify the Apps Script project **title** via the API before pushing — project-ID mix-ups are a real failure mode when a practice runs many small apps.
3. Push exact files; read back and diff.
4. Create a version; bump the **existing** deployment. Never mint a new deployment URL — portal links already in clients' hands point at the existing one.
5. Verify from the **served** page: load, sign in as a test provider, open a test client, write/sign a note, generate an invoice and a superbill.
6. Triggers are installed once, by hand, after the owner's first authorization. Never re-run an installer that creates triggers without checking for existing ones.

## Performance gate before release

Run the scaling reference as a checklist against the finished build: boot payload contents, per-screen call counts, batch shapes, cache coverage, housekeeping placement. A build that fails the gate is not released with a promise to optimise later — the patterns are structural and only get harder to change once real charts exist.
