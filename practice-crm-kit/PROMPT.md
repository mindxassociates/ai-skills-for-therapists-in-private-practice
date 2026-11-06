# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build me a practice CRM for my therapy practice using the Practice CRM Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — practice shape (solo or group), provider list, pipeline stages, lead sources, which systems will feed leads (booking, outcome forms, website forms, inbox ingest), and the archive/delete policy. Do not build anything until I have answered, and never guess a value — use a placeholder and flag it.
2. Build in this order: the **CRM workbook** (`references/data-model.md`), the **app** — board, Agenda, lead detail, dashboard (`references/board-and-views.md`), then the **ingest and write-backs** (`references/ingest-and-sync.md`).
3. Obey the kit's hard rules: no clinical notes; no unattended sends; the workbook is shared with nobody; a provider's data is filtered on the **server** (Notes never leave the server for a non-admin); lead matching goes Lead ID first, then email, then phone/name; and a failed CRM write must never fail the booking or form submission that triggered it — it logs to the sync log instead.
4. Deliver paste-ready files (Code.gs, Index.html, appsscript.json) plus the setup/deploy steps from `references/setup-and-deploy.md`. I will do the Google authorize/deploy clicks myself unless you have approved direct access to my account.
5. Walk me through `references/test-checklist.md` at the end — especially the permission tests (provider B must not be able to fetch provider A's lead, even by guessing its ID) — and don't call it done until they pass.

---
