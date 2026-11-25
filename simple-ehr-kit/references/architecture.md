# Architecture

## Components

| Piece | What it is |
|---|---|
| Provider app | Apps Script web app: Today view, Clients, Calendar, Notes, Billing, Settings. Gated (provider PIN hash or Workspace sign-in). |
| Client portal | Same project's second view (or a second deployment): token-scoped, no account. Intake, appointments, invoices/superbills, documents. |
| Workbook | The **index**: Clients, Appointments, NotesIndex, Invoices, IntakeIndex, Providers, Templates, Settings, AuditLog. Skinny rows only. |
| Drive chart folders | One folder per client (by ClientID) holding note files, intake PDFs, uploaded documents; one folder for generated superbill/invoice PDFs; one owner-only backup folder. All shared with nobody. |
| Google Calendar | The appointment's calendar copy. The workbook row is the chart record; the calendar event is the scheduling surface. They link by AppointmentID stored in the event description. |
| Triggers | Reminder sweep (hourly is plenty), nightly housekeeping (archive top-up checks, session cleanup), weekly backup. Installed once, by hand, after first authorization. Never re-run the installer — it does not de-duplicate. |

## The sharding model (read before anything else)

**One installation per practice.** A practice = one workbook, one project, one set of Drive folders, under that practice's own Workspace account.

- Providers *inside* a practice share that practice's installation, scoped by ProviderID on every server call.
- Practices never share an installation. Ten practices means ten copies. That is what keeps each copy fast, keeps Google quotas per-practice instead of global, and keeps one practice's chart data physically separate from another's.
- The kit is distributed as a template/copy, not as a hosted multi-tenant service. Do not "optimise" it into a SaaS.

## Repository layer

All storage access goes through server-side repository functions — `getClientsPage()`, `getClient()`, `getAppointmentsForDay()`, `getNotesIndex()`, `loadNoteFile()`, `saveNoteFile()`, `getInvoices()` and so on. Views never touch a sheet or a file directly.

Why: it is the escape hatch. If a practice outgrows Sheets (thresholds in `scaling-and-performance.md`), the repository can be re-pointed at a real database while the UI, templates and portal survive unchanged. It also concentrates the performance rules (batching, caching, narrow ranges) in one place where they can be audited.

## Data flow

1. **Intake:** portal token → client submits forms → server validates → a row in IntakeIndex + a PDF/JSON file in the client's Drive folder → client record marked intake-complete.
2. **Session:** appointment (workbook + calendar) → provider starts a note from the appointment → note file created in Drive, index row created → provider signs → file frozen, hash + timestamp on the index row → invoice generated from Settings fees.
3. **Payment:** invoice → payment link sent by email (processor hosts the card page) or payment recorded manually → invoice row marked paid with method + reference.
4. **Superbill:** on request or on payment, generated from the invoice + client + provider identifiers in Settings → PDF in Drive → client downloads it from the portal.
5. **Export:** per-client export gathers the index rows + Drive files into one downloadable bundle; the export itself is audit-logged.

## Sessions and identity

- Provider sessions: short-lived server-side session tokens, hashed at rest, pruned by the housekeeping trigger.
- Client identity: the portal token, per-client, hashed in the index. No passwords, no client accounts, no "type your name to prove it's you" steps.
- Every server function re-checks scope: a provider sees their own clients (plus practice-wide only if the practice configures an admin role); a client token resolves to exactly one ClientID and nothing else. Guessing an ID returns nothing.
