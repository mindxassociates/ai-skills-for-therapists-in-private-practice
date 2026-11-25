---
name: simple-ehr-kit
description: A simple EHR for solo therapists and small practices, built on Google Workspace + Apps Script + Sheets instead of a per-seat EHR subscription. Use when a practice wants (1) PRIVATE-PAY work only — direct client payment, invoices and payment links, PDF superbills for out-of-network reimbursement, HSA/FSA receipts — and explicitly does NOT need insurance claim submission, eligibility checks, ERA posting or denial management; (2) clients, scheduling linked to Google Calendar, a custom note builder with one-click carry-over, sign-and-lock with amendments, and a token-link client portal with digital intake; (3) telehealth by pasting the provider's own video link, and email reminders only (no native video, no SMS in v1); (4) a system that stays fast with many providers because each practice installs its OWN copy — one workbook per practice, Sheets as an index only, note and document content in Drive, yearly archiving, batched reads/writes and cached static data; and (5) honest limits stated up front — token links are bearer links, the workbook is shared with nobody, the practice admin can read the chart, and safeguards support HIPAA compliance inside a BAA-covered Workspace but nothing is "HIPAA certified."
---

# Simple EHR Kit — A Private-Pay EHR You Own

## What this system is

One Apps Script project (provider app + client portal in one project, or two deployments of it), over **one Sheets workbook + Drive folders**, all owned by the practice's own Google Workspace account:

1. **Provider app** (PIN- or sign-in-gated) — Today view, clients, calendar, notes, invoices and superbills. Opens to today's appointments and unsigned notes only; everything else loads on demand.
2. **Client portal** (no account) — each client has one personal token link: digital intake forms, upcoming appointments, invoices/superbills to download, and their own video link for each session. The token *is* the identity.
3. **The workbook is an index, not a filing cabinet.** It stores client demographics, appointment metadata, note metadata, invoice rows and the audit log. Note bodies, intake PDFs, uploaded documents and superbill PDFs live as **files in Drive**, referenced by file ID. See `references/data-model.md` and `references/scaling-and-performance.md`.

**Billing scope is the defining decision.** This is a **private-pay EHR**: the client pays the practice directly, the system invoices them and can hand them a standards-shaped superbill to submit to their insurer themselves for out-of-network reimbursement. It does **not** submit claims, check eligibility, post ERAs/EOBs, or manage denials — and it never will inside this kit. If a practice bills insurance panels in-network, this kit is the wrong chart for that work; say so in the setup interview and stop, or scope the kit explicitly to the practice's private-pay caseload only.

## Read this first — the limits, plainly

- **Private pay only.** See above. EAP and insurance may appear in a chart as *record-keeping* (payer name, copay collected, an export a biller or a platform can submit from) — the system itself submits nothing to any payer.
- **Token links are bearer links.** Anyone holding a client's portal link can open that client's portal. That is the trade that buys zero-friction access. Tokens are per-client, revocable, stored hashed in the index (the engine's plaintext copy, if any, lives only inside the restricted workbook), and regenerated on request.
- **Not end-to-end encrypted.** Chart data is plain text in the workbook and Drive files. The practice admin account can read everything. Encryption is HTTPS in transit + Google's at-rest encryption. The workbook and the chart Drive folders are **shared with nobody** — their sharing lists *are* the access boundary.
- These are safeguards that **support** HIPAA compliance inside a Google Workspace with a signed BAA. The phrase "HIPAA certified" is banned from every artifact this kit produces.
- **No native video and no SMS in v1.** Sessions happen on the provider's own video link (Zoom, Google Meet, or similar), pasted per appointment or set as a provider default. Reminders are email only; SMS, if ever added, is a separate pay-as-you-go vendor decision, never a silent default.
- **Sheets is not a database.** With the sharding, index-only and archiving rules in this kit, a solo or small group practice has years of headroom. A large group, or a practice that outgrows the thresholds in `references/scaling-and-performance.md`, graduates to a real database through the repository layer — by design, with data exportable the whole way.

## Instructions for the agent

- Deliverable = the project files (server code, provider view, portal view, templates) + a one-time setup that creates the workbook, Drive chart folders and seed settings (IDs in Script Properties — never hard-code a workbook ID). Or build/deploy directly with approved account access, verifying from read-backs and served pages.
- Run the setup interview first. Never guess fees, the provider list, the note templates, or the retention decision.
- Build in the phases in **Build order**, and do not skip the scaling rules: a build that loads whole tabs, stores note text in cells, or puts many practices in one workbook will work in the demo and fail in production.

## Setup interview (ask once, before building)

1. **Billing scope confirmation** — private-pay only, understood and accepted? Any private-pay caseload split (e.g. this chart is only for the self-pay part of a mixed practice)? Superbills offered — yes/no; what provider/practice identifiers go on them (legal name, NPI, tax ID, license, diagnosis and CPT codes the practice uses) — supplied by the practice, never invented.
2. **Practice identity** — practice legal and display name, address and phone for invoices/superbills, reminder/invoice sender (a send-as alias on the script-owning account), timezone.
3. **Providers** — list + stable IDs (state-prefix + number works well); sign-in method: PIN (SHA-256 of `ProviderID + ":" + PIN`, 5 failures → 15-minute lockout) or Workspace sign-in for providers in the same domain. Solo build = one provider, same structure.
4. **Fees** — the practice's own fee schedule by service/CPT, session lengths, cancellation/no-show policy as written policy text. Fees live in a Settings tab, editable by the admin, never hard-coded.
5. **Note templates** — starting set (e.g. a progress-note template, an intake/assessment template, a treatment-plan template): fields, field types, which fields carry over. The practice owns clinical wording.
6. **Scheduling** — which Google Calendar(s) appointments write to; provider default video link(s); email reminder timing (e.g. 24 hours before); whether clients may request reschedules from the portal (request only — provider confirms) or view-only.
7. **Intake packet** — the forms a new client completes (demographics, consents, policies, history questionnaire): the practice's own documents/wording, in every UI language offered. Who authors translations — clinical/legal content is never machine-translated and labelled as authored.
8. **Payments** — invoices by payment link (e.g. Stripe Payment Links / the practice's processor) or record-only (cash/check/card recorded manually)? Card numbers are **never** collected or stored in the app, ever.
9. **Retention + export** — chart retention period per the practice's jurisdiction and policy; who may export; backups (weekly workbook + Drive snapshot, owner-only folder, keep last 4).
10. **Scale shape** — solo, or group? If group: confirm **one workbook for this practice only**, providers share it by stable ID, and the yearly archive plan in `references/scaling-and-performance.md` is accepted.

## Hard rules

1. **Private-pay scope is a wall, not a preference.** No claim submission, no eligibility calls, no ERA parsing, no payer portals inside this system. Do not add a "just send this one claim" exception — that is a different product.
2. **One installation per practice.** Never host many unrelated practices in one workbook or one project. Each practice's copy carries its own data, quotas and access boundary. Adding providers *inside* one practice is supported; adding *practices* means new installations.
3. **Index in Sheets, content in Drive.** Note bodies, intake responses beyond short fields, documents and PDFs are Drive files. Index rows stay skinny: IDs, dates, status, amounts, file IDs. A cell caps at 50,000 characters and every fat cell slows every read that touches its tab.
4. **Notes are signed, locked, and amended — never edited.** Signing writes a timestamp + content hash and freezes the file. Corrections happen as dated amendments appended to the record. The audit log is append-only.
5. **Joins by stable ID only** — ProviderID / ClientID / AppointmentID / NoteID / InvoiceID. Never by display name. IDs never change on edit, so portal links and calendar events keep working.
6. **Fees and codes come from Settings, never from code.** Session fees, CPT/diagnosis code lists and policy text are data the admin edits. No fee is ever hard-coded, and no code is ever guessed for a superbill.
7. **No card data, ever.** Payments happen on the processor's page via a link, or are recorded as paid by an external method. The app stores amount, method label, date and processor reference only.
8. **Performance discipline is a correctness rule.** No whole-tab reads on boot; Today view first, everything else lazy and paginated; one workbook handle per execution; batched `getValues`/`setValues`, never per-cell loops; no volatile formulas over data tabs; static data (templates, fees, provider list) through CacheService; housekeeping (schema checks, folder ensures, archiving) on timers, never inside every request. See `references/scaling-and-performance.md`.
9. **Transport discipline.** `google.script.run` cannot transport `Date` objects or `NaN`/`Infinity` — one such value nulls the entire payload. Coerce every date-shaped field to text and every optional number through a clean-number path before returning anything to a view.
10. **Crisis and scope copy is honest.** The portal states it is not monitored in real time and is not a crisis channel, and shows crisis resources (988 in the US, or the practice's local equivalent). Completion/confirmation copy never implies anyone is watching live.
11. **Deploy discipline.** Restore point before every push; verify the Apps Script project **title** via the API before pushing; push exact files and read back; create a version and bump the **existing** deployment — never mint a new URL; verify from the **served** page, including a live click-test with a throwaway client, because served-HTML checks do not prove interactive behaviour.

## Build order

1. Workbook + Drive chart folders + Settings/fees seed, per `references/data-model.md`.
2. Server core: routing, provider gate + sessions, client token resolution, repository layer (all sheet/Drive access behind `getClients()`, `getNotes()` etc. — see `references/architecture.md`).
3. Provider app shell: instant shell + Today view, then Clients (add/edit/archive), then Calendar/Appointments.
4. Notes: template renderer, custom builder, carry-over, sign-and-lock, amendments, per `references/clinical-notes.md`.
5. Client portal: intake packet, upcoming appointments, documents, per `references/portal-intake-and-scheduling.md`.
6. Billing: invoices, payment links / payment recording, superbill PDF generation, per `references/billing-private-pay.md`.
7. Email reminders + triggers; per-client and full-chart export.
8. Hardening + release: scaling pass per `references/scaling-and-performance.md`, security pass per `references/security-and-privacy.md`, full test pass per `references/test-checklist.md`, yearly archive job installed.

## Reference files

- `references/architecture.md` — components, sharding model, repository layer, data flow, triggers
- `references/data-model.md` — the workbook: tabs, columns, status vocabularies, Drive layout
- `references/clinical-notes.md` — custom note builder, carry-over, sign-and-lock, amendments, treatment plans
- `references/portal-intake-and-scheduling.md` — client token portal, intake packet, calendar sync, reminders, video links
- `references/billing-private-pay.md` — fees, invoices, payment links, superbills, receipts, what is out of scope
- `references/scaling-and-performance.md` — why it slows down, the thresholds, and every countermeasure
- `references/security-and-privacy.md` — the honest limits, controls, admin checklist
- `references/build-and-deploy.md` — build phases, transport discipline, deploy discipline
- `references/test-checklist.md` — harness coverage + live click-test stages
