# Setup and deploy

## Prerequisites

- A Google Workspace account for the practice (BAA signed) to own the workbook and projects.
- The setup interview answered; the provider roster (or user list) the gate will verify against.

## Step 1 — the workbook

Create a workbook titled `CRM` in the admin account, shared with **nobody**. Don't hand-build the tabs — the app's setup function creates Leads / Activity / Sources / Archive / Trash / Ingest Log / Sync Log with their headers and seeds the Sources taxonomy. Copy the workbook ID into the app config.

## Step 2 — the app project

Apps Script project (Execute as owner). Files: `Code.gs`, `Index.html`, `appsscript.json`. Config constants / script properties: workbook ID, gate source (roster ID + tab, or the built-in user list), lifecycle numbers (archive days, started-archive days, trash purge days), cadence defaults.

**Manifest scopes** — declare everything the code calls:

- `https://www.googleapis.com/auth/spreadsheets` (full; readonly breaks `openById`)
- `https://www.googleapis.com/auth/gmail.readonly` (only if inbox ingest is built — and note MailApp needs a *send* scope instead if any code path sends mail; the CRM core sends nothing)
- `https://www.googleapis.com/auth/script.scriptapp` (the code installs its own triggers — without this scope the setup function dies at the trigger step, after everything else succeeded)

Deploy: **Web app, Execute as Me, Access: Anyone** (the gate is in the app; the deployment must be reachable for the sign-in page to render). Embed it in the provider portal or link it where providers already work. On later code changes, bump the **same deployment** to a new version — never mint a second deployment URL.

## Step 3 — triggers (installed by a setup function, run once by the owner)

- Inbox ingest: **hourly** (if built).
- Archive sweep + Trash purge: **daily**.
- Verify in the project's Triggers page that both exist and are owned by the admin account; run each once by hand and read its log rows before trusting the schedule.

## Step 4 — the feeds, one at a time

Add the shared sync helper to the booking project first; make a real booking; watch the Sync Log row and the lead appear. Then the outcome form; then each front-door form; then enable inbox ingest and watch one real directory inquiry land. **One feed at a time, each verified on a real event** — a CRM that silently misses a feed is worse than a manual CRM, because people stop keeping the manual list.

## Step 5 — people

- Providers set their PINs / sign in once; confirm each provider's board shows only their (initially empty) scope.
- Show the team the Agenda's awaiting-outcome row and the one-tap outcomes — that's the habit that makes the data real.
- Run `references/test-checklist.md` — permission tests before feature tests.
