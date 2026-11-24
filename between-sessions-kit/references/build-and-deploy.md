# Build and deploy

## Build phases (mirroring a real build's arc)

1. **Foundation** — workbook with all tabs/headers; catalog source + generator; provider seed. Nothing serves yet; that's fine.
2. **Server core + gate** — routing, PIN verify + sessions, token resolution, client CRUD.
3. **Provider app** — dashboard, clients, the 3-step assign wizard (library accordions + live search → client → schedule chips + natural-language summary sentence), reminders summary.
4. **Client app** — renderers per catalog type, completion summary (the client's own answers echoed with their prompts before Submit — clients should see what they're sending), self-guided index, language pill.
5. **Engine** — materialisation window, 15-minute sender, crediting, bilingual branded email (HTML + plain fallback, same link in both).
6. **Review + builder** — review views/charts/CSV export, flagged queue + mark-reviewed, custom-exercise builder with a step editor (never a raw-JSON field — providers are clinicians, not developers).
7. **Public surface** — one page per slug on the practice's site with token passthrough; provider app embedded in the portal if the practice has one; catalog ↔ page parity check.
8. **Hardening** — transport sweep (below), watchdog, backups, mobile pass (stacked-card tables, ≥44px targets, sticky nav), then the live click-test programme.

Expect the click-tests to find real defects the harness can't (they found, in the reference build: a summary view killed by live-shaped data, a confirm button whose success card rendered below the fold, a missing client-edit path, and uneditable drafts). Budget phases for fixing what they find.

## Transport discipline — the defect class that blanks screens

`google.script.run` delivers return values through a strict transport: **`Date` objects and non-finite numbers (`NaN`, `Infinity`) are not transportable — a payload containing one arrives at the success handler as `null`**, and the handler typically throws on `response.ok` before rendering anything. The view just never appears. No error banner, nothing in any log a provider would see.

Two live incidents, same class:

- **Summary never loads:** Sheets auto-converts the `"2026-11-22 11:14"` text the app appends into a real DATE_TIME cell. `getValues()` hands back JS `Date`s; a summary function returned them raw; the payload nulled; the tab silently never switched.
- **Review renders blank:** an unscored result's empty score cell became `NaN` in a computed series total. One NaN nulled the whole review payload while the dashboard (different function, clean numbers) showed the data plainly.

Rules that prevent the class:

- Every server function that returns data passes **every** field that could be date-shaped through a coerce-to-text helper (Date → formatted text in the relevant zone; null → `''`), and every optional number through a clean-number helper (blank/null → `''`; never return the raw `NaN`). Scores that are absent are `''` on the wire; the client's `Number(x) || 0` reads 0.
- Client handlers **guard nulls**: a null or not-ok response renders a visible in-view error card — a view must never fail silently again. Transport failures route to the same in-view slot, not a page-top banner nobody scrolls to.
- **Fixtures must be live-shaped.** The harness mocks Sheets with the values `getValues()` actually returns: real `Date` objects for date-shaped cells, empty strings for blank scores. String-only fixtures passed every test while the live view was broken. Reproduce live failures by replicating the live row exactly (read it via the Sheets API, grid/effective values) before fixing.

## The test harness

A Node harness loads the server code against a mock workbook and calls every function **in the exact argument shape the shipped client sends** (one object per call — harnesses that call in a scalar shape prove nothing about the real contract). It covers: gate + lockout, CRUD + ownership scoping, assignment creation per pattern, materialisation window walks + DST seam, engine sends/retries/crediting (including the legacy-uncredited guard), review payloads asserted **transport-legal** by a strict model (no Date, no non-finite number, recursively), catalog sweeps (spec-language, translation completeness, category coverage), and string-table parity. A DOM smoke suite drives both HTML views with a stubbed `google.script.run`, including null-payload and transport-failure modes for every view. A global-collision scan runs on the HTML files (never name a top-level variable `history`, `location`, `name`, `status`, … — `window.history` is unforgeable and a collision can silently kill a whole script block).

**Run date-sensitive suites with the practice timezone pinned** (e.g. `TZ=America/Chicago`): fixtures that straddle a day boundary fail spuriously under a UTC shell clock, and a red suite under the wrong TZ is not evidence of a regression.

## Deploy discipline

- **Restore point before every push** (a full copy of the current source tree, named by date + phase).
- **Verify the project title via the API (`projects.get`) before pushing.** Project IDs are easy to mix up across a fleet of similar apps; a push to the wrong project is silent and the deployments there pin versions, so the damage hides. Title first, every time.
- Push exact files; **read back byte-identical**; create a version; **bump the existing deployment** — never mint a new deployment URL (embeds everywhere point at the existing one). Deployment lists lag after an update — poll until the new version shows before concluding anything.
- **Served verification after every bump:** fetch the app's routes (provider view, index, a client item) and grep the served bytes for the new markers and the absence of removed ones. Served-HTML checks prove delivery, **not** interactive behaviour — pair them with the click-test stages in `test-checklist.md`.
- **Sheet data is a production input your fixtures never carry.** When a live behaviour contradicts a "no defect" conclusion, re-test live before defending the conclusion — in the reference fleet, a popup that "couldn't" fail was dead because a spreadsheet cell held an `http://` URL where every fixture had `https://`, and an exact-match lookup missed it silently. Test with the sheet's actual values.
- **Triggers are installed once**, by the owner running the setup function in the editor after the first authorization. Content pushes and version bumps never touch them. Never re-run the installer.
- **First deploy of an API-created project serves 403** until the owner authorizes the project's scopes once in the editor. That single run is also what creates the triggers — plan it as one owner action, not a defect hunt.
- **Adding a scope to a live app** (e.g. Drive, for backups) walls the app behind an authorization error until the owner re-grants. Sequence it: ship code that degrades gracefully without the new scope, stage the manifest change, have the owner re-authorize, then rely on the scope. If the old grant silently covers only the old scopes, the new-scope calls fail quietly in try/catch — verify the new capability end-to-end (an actual backup file), not just the consent click.
- **Concurrent editors:** if two agents/sessions work on the same project, each push compares remote HEAD to its base first; deployments pin version snapshots, so a stale HEAD push does not change what's live — but it will confuse the next pusher. Rebase on the verified live tree, never on assumption.
