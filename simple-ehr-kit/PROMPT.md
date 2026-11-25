# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build me a simple private-pay EHR for my therapy practice using the Simple EHR Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — and start with the billing-scope question. Confirm with me, in plain words, that this system is **private-pay only**: it invoices clients and generates superbills, and it does **not** submit claims, check eligibility, or post ERAs. If that does not fit my practice, stop and tell me instead of building. Then cover practice identity, providers and sign-in, my fee schedule (from me — never guess a fee or a code), note templates, scheduling and video links, the intake packet and who authors its translations, how payments are taken (payment link or record-only — never collect card numbers in the app), retention/export, and solo-vs-group scale shape. Read `references/security-and-privacy.md` with me and confirm I accept the stated limits (token links are bearer links; the workbook holds chart data and is shared with nobody; not monitored in real time) **before** building. Do not build anything until I have answered.
2. Build in the kit's order: the **workbook + Drive chart folders + Settings** (`references/data-model.md`), the **server core** with the repository layer (`references/architecture.md`), the **provider app** (instant shell, Today view first), **notes** (`references/clinical-notes.md`), the **client portal and intake** (`references/portal-intake-and-scheduling.md`), then **billing** (`references/billing-private-pay.md`), reminders and export, and the archive job.
3. Obey the kit's hard rules: **one installation per practice** (never many practices in one workbook); **index in Sheets, content in Drive** (note bodies and documents are files, never fat cells); notes are **signed, locked and amended**, never edited after signing; all joins by **stable ID**, never by name; fees and codes come from **Settings data**, never hard-coded; and the performance rules in `references/scaling-and-performance.md` — no whole-tab reads on boot, lazy paginated loading, one workbook handle per execution, batched reads/writes, cached static data, housekeeping on timers only.
4. Server functions **never return a `Date` or `NaN`** to a view (coerce dates to text, numbers through a clean-number path — one bad value nulls the whole payload). Declare **all** manifest scopes the code uses up front, and remember that adding a scope to a live deployment walls the app behind an authorization error until the owner re-grants: sequence it, don't discover it.
5. Deploy with the kit's discipline: restore point before every push, verify the project **title** before pushing, bump the **existing** deployment (never mint a new URL), and verify from the **served** page after every bump.
6. Walk me through `references/test-checklist.md` — the harness with **live-shaped fixtures** (real date cells, empty amount cells, a signed note, an archived year), then the live click-test stages with a throwaway client — and don't call it done until they pass and the test data is cleaned out.

---
