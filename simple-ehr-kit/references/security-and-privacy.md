# Security and privacy — the honest limits

## Say these plainly, in the app and to the practice

- **Not end-to-end encrypted.** Chart data is readable by anyone with access to the workbook or chart Drive folders — in practice, the practice admin account. Provider/portal access is scoped by the app; the underlying files are the boundary.
- **Token links are bearer links.** Possession = access to that one client's portal. Mitigations: per-client tokens, hashed at rest, revocable, regenerated on request, never printed on superbills or invoices sent outside the portal.
- **Not monitored in real time; not a crisis channel.** Portal copy carries crisis resources and response-time expectations.
- **Safeguards support HIPAA compliance; nothing is "HIPAA certified."** The prerequisites are organisational as much as technical: a Google Workspace account with a **signed BAA**, staff training, and the practice's own policies.

## Controls checklist

- [ ] Workbook and all chart Drive folders: sharing = **nobody** (owner only). Verified at setup and re-checked by a housekeeping report.
- [ ] Script runs under the practice admin account; providers/clients never receive file-level access — app access only.
- [ ] PINs, session tokens and portal tokens stored **hashed** (SHA-256, salted with the record ID). Raw values never logged.
- [ ] Lockout: 5 failed provider sign-in attempts → 15-minute lock; lockouts alert the admin (IDs only).
- [ ] Server-side scoping on **every** call: provider → own clients (admin role → practice-wide, if configured); client token → exactly one client. ID guessing returns nothing.
- [ ] Audit log append-only and hash-chained: sign-ins, chart opens by non-owning providers/admin, note signing/amendment, invoice changes, exports, token regeneration. IDs and actions only — never content.
- [ ] Email minimalism: notifications and reminders carry no diagnosis, no note content, no amounts. Links point to the gated app/portal.
- [ ] Uploads (if the portal accepts documents): type/size/count caps, filename sanitisation, stored unshared in the client's folder, served only through the app to a scoped user, downloads audit-logged.
- [ ] Backups: weekly, to an owner-only folder, last 4 kept; a backup is a copy of the crown jewels — its sharing is checked like the original's.
- [ ] Departed provider: disable the Providers row (sessions die, PIN stops working) — never delete the row; their signed notes remain part of the charts.
- [ ] Client discharge/archival follows the practice's written retention policy and jurisdiction — the kit implements the period the practice sets; it does not choose one.

## First-use disclosures (practice adapts, kit supplies the structure)

Portal first-open copy must cover: what the portal is for; that it is not monitored in real time and what to do in a crisis (988 in the US / local equivalent, 911 for emergencies); expected response times; that practice administration can access portal and chart data for operations and supervision; and that superbills are documents the client submits to their insurer themselves, with no guarantee of reimbursement.
