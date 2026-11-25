---
name: between-sessions-kit
description: A between-session client homework system for a therapy practice, built on Google Workspace + Apps Script + Sheets instead of a paid homework-platform subscription. Use when a practice wants (1) a catalog of exercises and reminders (chatbot-style practices, journals, self-monitoring logs, breathing/timer items, affirmations) that providers assign in a few taps; (2) clients who need NO account — each assignment is one personal link, opened in a browser; (3) email-only reminders (NO SMS, ever) on a 15-minute engine, scheduled in the CLIENT's timezone, where an early submission credits the pending instance instead of triggering another reminder; (4) a bilingual client experience with authored (never machine-labelled) translations; (5) a review queue where crisis-adjacent submissions flag for prompt provider review; and (6) production guardrails — a nightly watchdog on the reminder engine and weekly workbook backups — with the limits stated honestly (token links are bearer links; the workbook holds client homework data and is shared with nobody; the EHR stays the system of record).
---

# Between Sessions Kit — A Client Homework System You Own

## What this system is

One Apps Script project, one deployment, **two audiences**, over **one Sheets workbook**:

1. **Provider app** (PIN-gated) — clinicians manage clients, assign catalog items with a reminder plan, watch adherence, review submissions, and author custom exercises. It can stand alone at the app URL or be embedded in the practice's provider portal.
2. **Client app** (no sign-in at all) — each assignment is a personal link (`https://<your-client-site>/exercises/<slug>?t=<token>`). The token *is* the identity: no client accounts, no passwords, no "type your first name." The same pages, opened without a token, run in a **public self-guided mode** (an index of the whole library) where nothing is saved or sent to anyone.

The **catalog** (exercises + reminders) ships as data generated into the project at build time — the workbook stores only clients, assignments, scheduled reminder instances, results, custom exercises, and the audit log. Reminder **email** is the only outbound channel; there is deliberately **no SMS anywhere** — no phone field is used for messaging, no text option exists in any UI.

## Read this first — the limits, plainly

- **Token links are bearer links.** Anyone holding a client's assignment link can open that assignment and submit as that client. That is the trade that buys zero-friction access for clients who will not manage another account. Links are per-assignment (not per-client), ending an assignment kills its token, and tokens are stored hashed — the one plaintext copy lives only inside the restricted workbook, where the engine needs it to build recurring email links. Say this plainly to the practice; if they cannot accept it, this kit is the wrong tool.
- **The workbook holds client data** (emails, homework answers). It is **shared with nobody** — its sharing list is the access boundary, exactly like the workbook in the Secure Messages Kit. Client payloads are token-scoped server-side; provider payloads are filtered to the signed-in provider's own clients on every call.
- **Not a crisis channel and not monitored in real time.** Items the practice marks as crisis-adjacent (e.g. a personal safety plan) show crisis resources (988 in the US, or the practice's local equivalent) on the page and flag every submission for prompt review — but completion copy must say results are *reviewed by the provider*, never that anyone is watching live.
- These are safeguards that **support** HIPAA compliance inside a Google Workspace with a signed BAA. The phrase "HIPAA certified" is banned from every artifact this kit produces. The **EHR remains the system of record** once a client starts — this tool holds between-session homework, not clinical notes.

## Instructions for the agent

- Deliverable = the project files (server code, two HTML views, catalog data, string tables) + a one-time setup that creates the workbook and seeds providers + checklists. Or build/deploy directly with approved account access, verifying from read-backs and served pages.
- Run the setup interview first. Never guess the sender identity, the provider list, the languages, or the crisis copy.
- Build in the phases in **Build order** below, and do not skip the hardening phase: the two defects that actually bite in production (transport-poisoned payloads and row-by-row materialisation) are invisible in casual testing — see `references/build-and-deploy.md`.

## Setup interview (ask once, before building)

1. **Practice identity** — practice name; reminder sender (a no-reply send-as alias on the script-owning account, with a display name); the public base URL client links will live under (your directory/portal pages that embed the app, or the raw app URL).
2. **Languages** — English only, or bilingual? If bilingual: which second language, and **who authors the translations**? Clinical content is never machine-translated and labelled as authored — an item without an authored translation renders in English with a visible note until a human writes one.
3. **Catalog starting point** — adapt the category/type structure in `references/catalog-format.md` and author your own items, or start from a small core set (breathing, thought log, journals, self-monitoring, sleep log, safety plan) and grow. Item wording is clinical content — the practice owns it.
4. **Providers** — list + stable IDs (state-prefix + number works well, e.g. `CA0001`); PIN source: mirrored from an existing roster's PIN hashes, or set by an admin seed. PINs are verified as SHA-256 of `ProviderID + ":" + PIN`; 5 failed attempts → 15-minute lockout.
5. **Assessments in or out?** — the reference build deliberately keeps standardised assessments (PHQ-9 etc.) in the EHR and ships exercises + reminders only. Decide explicitly; the data model does not change either way.
6. **Crisis copy + flag items** — the crisis resources shown on flagged items (988 / local equivalent + the practice's wording, in every UI language) and which catalog items flag on submission (safety-plan-type items at minimum).
7. **Public self-guided index** — on (anyone can browse and practise, nothing saved) or off (every page requires a token)?
8. **Workbook + backups** — the workbook is created fresh, owned by the script account, shared with nobody; backups go to an owner-only Drive folder (weekly, keep the last 4).

## Hard rules

1. **No SMS.** Email reminders + provider copy-link are the only channels. No phone-as-messaging field, no "text" option anywhere, and the instance schema's channel value is always `email` — any other value is a validation error.
2. **No client accounts.** Identity is the per-assignment token. Never add a client login, a client PIN, or a name-typing step.
3. **The client's timezone governs reminder times.** Assignment dates/times are wall times in the *client's* zone; instances store unambiguous epochs; provider displays label times with the client's zone. A client with no stored zone falls back to the practice zone (legacy behaviour, preserved exactly).
4. **Early work is credited, never re-reminded.** A submission credits the earliest pending instance for that assignment (or the sent one); the engine checks for covering results before every send — including results saved before the crediting rule existed — and never emails about work already done. Adherence = Completed ÷ Sent, computed at read time.
5. **Transport discipline (the production-killer).** `google.script.run` cannot transport `Date` objects or `NaN`/`Infinity` — **one such value nulls the entire payload** and the view silently never renders. Sheets auto-converts date-shaped strings into date cells, so server functions must coerce every date-shaped field to text and every optional number through a clean-number path (blank → `''`, never `NaN`) before returning. See `references/build-and-deploy.md`.
6. **Never materialise a whole series row-by-row.** Creation writes only the next **60 days** of instances, in **one bulk write**; a nightly top-up extends the window idempotently. A daily-for-a-year assignment is ~370 instances — appending them one call each takes minutes; the window makes it seconds.
7. **Catalog-driven, authored content only.** Client steps come from authored step data. Never synthesise client-facing prompts from internal build notes, flow specs, or developer text — that defect class shipped spec language ("Client taps the pill button…") to real clients once; the renderer must have no path that can do it. Translations follow the same rule (Hard rule in the setup interview, Q2).
8. **Joins by stable ID only** — ProviderID / ClientID / AssignmentID / catalog slug. Never by display name (duplicate names are normal). Records are edited in place: a client's ID and assignment tokens never change on edit, so links already sent keep working.
9. **Deploy discipline.** Restore point before every push; verify the Apps Script project **title** via the API before pushing (project-ID mix-ups happen); push exact files and read back byte-identical; create a version and bump the **existing** deployment — never mint a new URL; verify from the **served** page afterwards. Never re-run the trigger installer (it does not de-duplicate).
10. **Guardrails run themselves.** A nightly watchdog flags reminder instances stuck unsent > 3 hours and alerts the admin (IDs only, no client names, no content); weekly workbook backups with 4-copy retention run in the same housekeeping trigger. Triggers are created once, by hand, after the owner's first authorization.

## Build order

1. Workbook + catalog generation + provider seed, per `references/data-model.md` and `references/catalog-format.md`.
2. Server core: routing, provider PIN gate + sessions, client token resolution.
3. Provider app: clients (add / edit / archive / delete-with-cascade), the 3-step assign wizard, reminders summary.
4. Client app: item renderers (chatbot, journal, self-monitoring, timer, affirmation, custom reminder), self-guided index, language pill.
5. Reminder engine + triggers + bilingual email templates, per `references/reminder-engine.md`.
6. Review + flags + export, and the custom-exercise builder (draft → publish → retire, or delete outright while a draft, retired, or never assigned; practice-shared option).
7. Public pages / embedding (token passthrough), parity check between catalog and public pages.
8. Hardening + release: transport sweep, watchdog, backups, full test pass per `references/test-checklist.md` — including a **live click-test**, because served-HTML checks do not prove interactive behaviour.

## Reference files

- `references/architecture.md` — components, data flow, tokens, embedding, triggers
- `references/data-model.md` — the workbook: 8 tabs, columns, status vocabularies
- `references/catalog-format.md` — item schema, step kinds, bilingual fields, categories
- `references/reminder-engine.md` — recurrence, the 60-day window, timezones, crediting, adherence
- `references/build-and-deploy.md` — build phases, transport discipline, deploy discipline, test harness
- `references/operations.md` — day-2 operations + troubleshooting table from real incidents
- `references/security-and-privacy.md` — the honest limits, controls, admin checklist
- `references/test-checklist.md` — harness coverage + live click-test stages
