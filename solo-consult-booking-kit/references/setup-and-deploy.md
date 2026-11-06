# Setup & Deploy — Solo Consult Booking Kit

Prerequisite gate: **Google Workspace + signed BAA + hardened owner
account** (see SKILL.md). Do not start Step 1 until that's confirmed.

Who clicks what: these steps are written for the **owner** to perform
in their own Google account, with the agent preparing the files and
guiding. That's deliberate and platform-neutral — it works whether
the agent is a chat assistant with no account access or a coding
agent with a deploy path. An agent with direct, owner-approved
access may perform the same steps itself, but the order, the
authorization prompts, and the verification checks are identical.

Deployment order (do not reorder): ① workbook → ② Booking app →
③ Console app → ④ test → ⑤ embed & swap links. **There is no
calendar-connection step** — the owner needs no extra app to "connect"
their own calendar.

## Step 1 — Create the workbook (as the owner)

1. In the owner's Workspace Drive, create a spreadsheet named e.g.
   **Consult Booking**. Keep it private (shared with nobody).
2. Note its ID from the URL — both apps' `Code.gs` takes it as the
   single config constant (`WORKBOOK_ID`). No other spreadsheet IDs
   exist in the solo edition: no roster workbook, no submissions
   workbook.
3. Tabs are created by the Booking app's `setupSheet()` in Step 2 —
   don't hand-build them.

## Step 2 — Booking app

1. script.google.com (signed in as the owner) → New project → name it
   **Initial Consult Booking**.
2. Project Settings → check "Show appsscript.json manifest file" →
   replace the manifest with the project's `appsscript.json` (it
   enables the Calendar Advanced Service v3; if the manifest is
   rejected, enable it manually: Services → Google Calendar API v3,
   identifier `Calendar`).
3. Replace `Code.gs`; add HTML files named exactly **Index** and
   **Manage**. Set the one config constant: `WORKBOOK_ID` (Step 1).
   Seed the code-level defaults (practice name, contact email,
   privacy-policy URL, notice version) from the setup interview.
4. Run **`setupSheet()`** → authorize when Google prompts (the only
   account authorizing is the owner's). This creates the tabs with
   the exact headers from `architecture.md` and seeds Settings.
5. Fill the **Config** row by hand: name, credentials, calendar ID,
   time zone, licensed states, panels (client-facing names),
   languages, ages/client types, sliding scale, serves-international,
   bio link, work email, Active = Yes, AcceptingNewClients = Yes.
   Seed the **Availability** tab or wait and use the Console in
   Step 3 for weekly hours.
   - Calendar ID: for the primary calendar, it's the owner's email
     address. For a dedicated calendar: Google Calendar → Settings →
     that calendar → "Calendar ID."
6. Run **`checkSetup()`** → read View → Logs. It must report
   `accessRole=owner`, `freebusy=OK`, and ≥1 weekly-hours block.
   Anything else is a setup error to fix now (wrong CalendarID is the
   usual cause) — there is no sharing step that could fix it later,
   because no sharing is involved.
7. Run **`setupTriggers()`** once — installs the 5-minute sweep
   (reminders, follow-ups) and daily retention. Verify in the
   editor's Triggers view that both exist.
8. Run the alias test-send function; confirm the From header on the
   arrived test email (if an alias is configured and the mail fell
   back to the bare account address, fix the send-as alias on the
   account — and confirm `gmail.settings.basic` is in the manifest).
9. **Deploy → New deployment → Web app:** Execute as **Me**, Who has
   access **Anyone**. Copy the `/exec` URL — that's the booking link.

## Step 3 — Owner Console

1. New Apps Script project as the owner, named **Consult Console**:
   `Code.gs`, `Index.html`, `appsscript.json` from the Console spec;
   same `WORKBOOK_ID` constant.
2. First open after deploy: create the owner PIN (4 digits) at the
   gate. Confirm the three views load: My Consults (empty is fine),
   Availability (submit the real weekly hours now if Step 2 used no
   seed), Settings & Tools (templates present).
3. **Deploy → New deployment → Web app:** Execute as **Me**, access
   **Anyone** (the PIN gate is the boundary). Bookmark the `/exec`
   URL somewhere private; optionally embed it on a private page only
   the owner uses.

## Step 4 — Test

Run `references/test-checklist.md` in the deployed apps, with a test
client identity (the owner's own name/personal email on a *test*
booking is fine — delete the row + event afterwards). At minimum:
one end-to-end booking, one double-booking attempt, one
reschedule/cancel through the emailed manage link, one no-fit path,
and manual runs of the reminder + follow-up sends. Restore any
Settings you perturbed during testing.

## Step 5 — Go live (Google Sites embed, or any website)

- Add a booking page on the practice website with an **Embed** block
  pointing at the Booking app's `/exec` URL, with generous height —
  or link a "Book a consultation" button straight to the `/exec` URL.
  Clients book without an account either way.
- Manage (reschedule/cancel) links in emails point at the app's own
  `script.google.com` address — an embed can't receive the manage
  token, so the manage page opens on Google's domain with the
  practice's branding. This is normal for Apps Script systems;
  accept it rather than building a custom-domain wrapper.
- Swap public links (website buttons, directories, email signature)
  to the new page. Keep the old booking service live as a fallback
  until the first real booking completes cleanly.

## Updating later (both apps, forever)

1. Edit/paste the new files locally, run the local harness.
2. Push the content, then **read the deployed project content back
   and require a byte-for-byte match before creating a version** —
   a stale-content deploy looks identical to a good one until
   someone opens the app.
3. **Deploy → Manage deployments → edit the live deployment →
   Version: New version.** Never create a new deployment (new URL =
   broken embeds + old code still served at the old URL).
4. After bumping, wait a few seconds and re-list deployments to
   confirm the version actually moved (lists lag).
5. Remember: pasted code never brings triggers. A brand-new project
   needs `setupTriggers()` run by hand; an updated existing project
   keeps its triggers.
6. Settings/template changes are **not** deploys — the owner edits
   them in the Console and both apps pick them up on their next run.

## Day-to-day administration (owner, no code)

| Change | Where |
|---|---|
| Pause / resume taking consults | Console → Availability → Accepting toggle (or Config `AcceptingNewClients`) |
| Weekly consult hours | Console → Availability → Weekly Availability submission |
| One-off different hours | Console → Availability → Date Specific Hours |
| Vacation / blocked dates | Console → Availability → Time Off |
| Consult frequency cap, minimum notice, buffers | Console → Availability → Consult Booking Settings (auto-saves) |
| Booking window, cutoffs, reminder timing, retention days | Console → Settings & Tools (Settings tab keys) |
| Email wording | Console → Settings & Tools (templates) |
| Panels / states / languages you offer | Config tab row (wizard options regenerate on next page load) |
| A booking needs manual help | Appointments tab has every detail; `CalendarEventID` identifies the calendar event |
| Reset a forgotten Console PIN | Clear Config `PinHash` + `PinToken`, then set a new PIN at the gate |
| Kill all outstanding manage links at once | Clear the Appointments `ManageToken` column (incident response) |

Errors a client can see are deliberately plain (calendar unreachable,
slot just taken, cutoff passed, invalid details) with the practice
contact email. The technical cause lives in the Apps Script execution
log and `checkSetup()` output — never on the public page.
