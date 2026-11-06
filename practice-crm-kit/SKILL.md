---
name: practice-crm-kit
description: A lead-tracking CRM for a therapy practice, built on Google Workspace + Apps Script + Sheets. Use when a practice wants (1) a pipeline board for prospective clients (New → Contact Attempted → Consult Booked → Consult Held → Intake Sent → Started, with Not a Fit / Declined / No Response / Referred Out exits); (2) automatic lead capture from its consult booking system, post-consult outcome forms, website/directory forms, and hourly rule-based inbox ingest of directory-inquiry and answering-service emails; (3) follow-ups carried on each lead (Next Action + due date) with an Agenda view; and (4) group-practice roles — admin sees all leads including Notes, each provider sees only their own leads with Notes stripped server-side. No clinical notes, no unattended sends, workbook shared with nobody.
---

# Practice CRM Kit — Lead Tracking for a Therapy Practice

## What this system is

One Apps Script web app over **one dedicated workbook** (working title: `CRM`), deliberately **standalone** — not a view inside any other app, not linked to a task board. Follow-ups live on the lead itself. Automatic feeds (booking, outcome forms, contact forms, inbox ingest) write into it through small, logged upsert hooks; humans work it through a board, an Agenda, and a lead-detail view.

It exists because the gap between "inquired" and "started" is where practices lose people: a directory reply nobody followed up, a consult that happened with no outcome recorded, an intake packet sent and never chased. The CRM makes that gap visible and owned.

## Instructions for the agent

- Deliverable = paste-ready files (`Code.gs`, `Index.html`, `appsscript.json`) + the workbook + trigger setup + a deploy checklist, unless you have approved direct access to the owner's Google account.
- Run the setup interview first; never guess stages, sources, or provider identities.
- The runtime is **Apps Script and its triggers only** — no external AI service sits in the loop at runtime. Ingest parsing is rule-based (senders, subjects, structured fields), deterministic, and testable.
- Manifest scopes: if `oauthScopes` is declared, declare **every** service called — full `spreadsheets` for `openById` (never readonly), the mail-read scope if the app ingests inbox mail, and the trigger scope (`script.scriptapp`) if the code installs its own triggers. A missing scope fails a whole feature, often silently inside a try/catch.

## Setup interview (ask once, before building)

1. **Practice shape** — solo or group? If group: provider list + stable provider IDs, and who is admin.
2. **Pipeline** — confirm the default stages and exits (above), or adapt. Stage names are configuration, but don't invent more than ~10; a board people must interpret is a board they stop using.
3. **Sources** — the practice's real channels (booking page, website, each directory, answering service, referrals, walk-ins). These become the Source taxonomy; keep it a controlled list, not free text.
4. **Feeds** — which of these exist today: a booking system that can upsert on booking? A post-consult outcome form? Website/directory contact forms? An inbox where directory inquiries and answering-service summaries arrive (for hourly ingest)? Each "yes" gets a hook in `references/ingest-and-sync.md`; each "no" is manual quick-add until built.
5. **Follow-up cadence** — the practice's rhythm for new leads (a common pattern: Day 0 / 2 / 5 / 10) and after a held consult (Day 3 / 7). The CRM proposes due dates from the cadence; humans can always override.
6. **Lifecycle policy** — how long a lead sits in a stage before auto-archive (default 30 days; Started leads: 90 days past the consult), and the soft-delete grace period (default 7 days).
7. **Identity gate** — how users sign in. The reference build verifies name + PIN server-side against the practice's provider roster; a solo practice can use a single admin sign-in. Whatever you choose, **no lead data is served before the gate verifies**.

## Hard rules

1. **No clinical notes.** Fields describe intake logistics (source, payor named by the inquirer, concern *category*, stage, contact attempts). Presenting problems in the client's own words, session content, diagnoses — none of it belongs here. Once a lead Starts, the EHR is the system of record; the CRM keeps only the link/status.
2. **No unattended sends.** The system never contacts a lead autonomously. It surfaces what's due; a human sends.
3. **Server-side scoping, always.** A provider's board, search, Agenda, and detail calls return only their leads, filtered on the server. The **Notes field is stripped from provider payloads on the server** — not hidden in the UI. Fetching another provider's lead by ID returns nothing.
4. **The workbook is shared with nobody** and is separate from every other practice workbook.
5. **Matching order is fixed:** Lead ID → email → phone → name+provider. Automatic writes upsert; they never blindly insert a second lead for the same person, and they only move a stage **forward** (a late-arriving "booked" event must not drag a Started lead backwards).
6. **A failed CRM write never fails the source event.** If the booking system's CRM hook throws, the booking still succeeds; the failure lands in the Sync Log. The front door is more important than the ledger.
7. **Sync/ingest logs carry no personal data** — timestamps, source, event, lead ID, result. Never names, emails, or message bodies. (The lead row itself holds the contact data; the log doesn't need to.)
8. **Ingest is rule-based and body-free.** Directory-inquiry and answering-service emails become leads from their structured fields (sender, subject, known form fields). Message bodies are not copied into the CRM. Inquiry types that aren't leads (e.g. supervision-seeking from clinicians, if your practice excludes them) create nothing.

## Build order

1. Workbook per `references/data-model.md`, with self-healing header setup in code.
2. App shell + gate + board/Agenda/detail/dashboard per `references/board-and-views.md`.
3. Manual quick-add (admin + provider self-add) — the system is useful from this point.
4. Hooks: booking upsert, outcome write-back, form create/refresh, inbox ingest — per `references/ingest-and-sync.md`, one at a time, each with its Sync Log lines verified live.
5. Lifecycle: archive sweep, soft delete + purge, undo, bulk actions.
6. Deploy per `references/setup-and-deploy.md`; verify per `references/test-checklist.md`.

## Reference files

- `references/architecture.md` — components, roles, data flow
- `references/data-model.md` — workbook tabs and every lead field
- `references/board-and-views.md` — board, Agenda, detail, dashboard, attention panels
- `references/ingest-and-sync.md` — the four feeds, matching, forward-only stages, sync log
- `references/security-and-privacy.md` — scoping, notes discipline, sharing, retention
- `references/setup-and-deploy.md` — projects, scopes, triggers, embedding
- `references/test-checklist.md` — acceptance tests, permission tests first
