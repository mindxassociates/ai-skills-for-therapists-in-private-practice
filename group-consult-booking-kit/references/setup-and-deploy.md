# Setup & Deploy — Group Consult Booking Kit

Prerequisite gate: **Workspace + signed BAA + hardened practice
account + the provider-calendar policy decision** (see SKILL.md). Do
not start Step 1 until those are confirmed.

Who clicks what: steps are written for the **practice admin** in the
practice account, with the agent preparing files and guiding. An
agent with direct, admin-approved access may perform them itself —
order, authorizations, and verification checks are identical either
way.

**Deployment order (do not reorder):** ① workbooks → ② Booking app →
③ Connect Your Calendar (needs the Booking app's URL) → ④ Manage
Availability → ⑤ My Consults → ⑥ Consult Admin → ⑦ provider
onboarding → ⑧ test → ⑨ cutover.

## Step 1 — Workbooks (as the practice account)

Create three spreadsheets, all private: **Provider Roster** (one tab,
your roster columns + the AG/AH PIN columns from `architecture.md`),
**Consult Booking** (the booking workbook — tabs are created by the
Booking app's `setupSheet()`; don't hand-build them), and **Manage
Availability Submissions** (one sheet; headers self-heal from the
app). Note all three IDs — each app's `Code.gs` takes them as config
constants. Fill the Roster with verified provider data (setup
interview); unverified providers are simply left out until verified.

## Step 2 — Booking app

1. New Apps Script project as the practice account: **Initial Consult
   Booking**. Show the manifest (Project Settings), paste
   `appsscript.json` (enables Calendar v3), `Code.gs` (with the three
   workbook IDs + practice defaults baked in), HTML files **Index**
   and **Manage**.
2. Run `setupSheet()` → authorize → creates tabs + seeds Settings.
3. Run `syncProvidersFromRoster()` → Providers tab populated
   (CalendarIDs default to work emails until providers connect).
4. Run `setupTriggers()` once; verify in Triggers: 5-minute sweep,
   daily sync, daily retention.
5. Run the alias test-send; confirm the From header on arrival.
6. **Deploy → New deployment → Web app:** Execute as **Me**, access
   **Anyone**. Copy the `/exec` URL — everything else needs it.
7. Run `checkSetup()` now for a baseline (expect calendar warnings
   until Step 7 — that's what onboarding fixes).

## Step 3 — Connect Your Calendar

1. New project as the practice account, files from the Connect spec.
   In `Code.gs`, bake in `BOOKING_API_URL` = Step 2's `/exec` URL and
   `ADMIN_EMAIL` = the practice account.
2. **Deploy → New deployment → Web app:** confirm it shows Execute
   as **User accessing the web app**, access Anyone. (If it says
   "Me," stop — the app would act as the practice account and could
   never share a provider's calendar.)
3. Publish the URL where providers will find it (portal page) along
   with the provider help article (unverified-app warning + manual
   fallback, per the Connect spec).
4. Optionally start the OAuth verification packet now (Connect spec)
   — in parallel, never as a blocker.

## Steps 4–6 — Manage Availability, My Consults, Consult Admin

Same pattern each: new project as the practice account, paste files +
manifest, set workbook-ID constants, deploy as Web app (Execute as
**Me**, access Anyone — PIN gates are the boundary), embed/link where
providers (or only the admin, for Consult Admin) will find them.
First opens: each provider creates their fleet PIN at whichever app
they meet first (it works in all of them); the admin signs in to
Consult Admin with the admin roster entry. After the Manage
Availability deploy, open it once as the practice account and
re-authorize if Google prompts (its calendar scope is new to that
project).

## Step 7 — Provider onboarding (per provider, ~5 minutes)

1. Provider opens **Connect Your Calendar**, signs in (name + PIN),
   authorizes as themselves, picks their schedule calendar, Connect.
   (Personal accounts: expect the unverified-app screen → Advanced →
   continue.) Fallback: manual share at "Make changes to events" +
   admin sets the CalendarID.
2. Provider opens **Manage Availability** and submits real weekly
   consult hours (with their time zone), or the admin enters hours
   for them in Consult Admin.
3. Admin runs `checkSetup()`: the provider's line must show
   `accessRole=writer` (or owner), `freebusy=OK`, ≥1 hours block,
   correct zone. Fix the flagged item — not the booking app — if not.
4. Repeat until every go-live provider is clean. Providers with no
   hours or no connection simply don't appear to clients; nobody is
   half-live.

## Step 8 — Test

Run `references/test-checklist.md` in the deployed apps with test
identities: routing matrix against your real roster facts, conflicts,
double-booking race, reschedule/cancel via emailed links, failure
modes, reminders/follow-ups by hand, bilingual paths if enabled.
Delete test rows/events; restore any perturbed Settings.

## Step 9 — Cutover

- Embed the Booking app on the practice website's booking page
  (generous-height embed of the `/exec` URL), or link booking buttons
  straight to it. Manage links in emails point at the app's own
  Google address — normal for Apps Script; don't build a
  custom-domain wrapper for them.
- Replace per-provider scheduler links everywhere with the single
  booking page (website, directories, chatbot/answering-service
  scripts, email signatures) — **after** the checklist passes. Keep
  the old links live as fallback until the first real bookings
  complete cleanly, then retire them.
- Announce to providers once, with the three links (Connect,
  Availability, My Consults) and the help articles.

## Updating later (all apps, forever)

1. Edit locally, run harnesses, push content, **read deployed content
   back byte-for-byte before creating a version**.
2. **Deploy → Manage deployments → edit the live deployment →
   Version: New version.** Never a new deployment.
3. Wait a few seconds, re-list deployments to confirm the bump
   (lists lag).
4. Fresh projects need their trigger setup run by hand; updated
   existing projects keep theirs.
5. Production config stays baked into the local source — a delivery
   that reverts a live URL or ID ships a broken app.
6. Settings/template changes are not deploys: Consult Admin edits,
   effective on the next run.

## Day-to-day administration

| Change | Where |
|---|---|
| Provider joins | Roster row → run sync (or wait for daily) → they connect calendar + submit hours → `checkSetup()` |
| Provider leaves | Connect-app Disconnect (or manual unshare) + Roster Active = No → sync → clear their PIN cells |
| Provider pauses bookings | Their Manage Availability toggle, or Providers tab `AcceptingNewClients = No` |
| Practice-wide closure | Consult Admin TimeOff row with ProviderID `ALL` (one row blocks everyone) |
| Weekly hours for a provider who won't self-serve | Consult Admin → Availability → edit on behalf |
| Booking rules / email wording | Consult Admin → Emails & Booking Settings |
| Stats, audit, exports | Consult Admin → Admin Tools |
| A booking needs manual help | Appointments tab; `CalendarEventID` identifies the event |
| Forgotten provider PIN | Clear that provider's Roster AG/AH cells; they create a new PIN |
| Kill all manage links at once | Clear the Appointments `ManageToken` column (incident response) |

Public-page errors are deliberately plain (slot taken, cutoff passed,
invalid details) with the practice contact email; technical causes
live in the execution log and `checkSetup()` output.
