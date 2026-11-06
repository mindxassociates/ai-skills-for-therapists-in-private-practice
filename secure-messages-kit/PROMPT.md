# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build me a secure client-messaging portal for my therapy practice using the Secure Messages Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — practice name and sender identity, provider list, whether externals are included, the one-time-reply default, retention decision, and where the portal page will live. Read `references/security-and-privacy.md` with me and confirm the practice accepts the stated limits (not end-to-end encrypted; practice admin can access messages; workbook shared with nobody) **before** building. Do not build anything until I have answered, and never guess a value — use a placeholder and flag it.
2. Build in this order: the **portal workbook + Drive folder** via a one-time boot function (`references/data-model.md`), the **portal app** (`references/messaging-features.md`, sign-in per `references/access-and-sessions.md`), then the **admin console** if I chose it.
3. Obey the kit's hard rules: message content lives only in the workbook and the attachment files — notification emails carry no body, no subject, no client reference; codes, PINs, DOBs, and session tokens are stored only as hashes; every payload is participant-scoped on the server; the audit log records IDs, never bodies; attachments are stored unshared and served only through the app; and the words "HIPAA certified" appear nowhere.
4. Declare **all** manifest scopes the code uses — spreadsheets (full), Drive, and both mail scopes if both mail APIs are called — and use the no-downtime sequence if adding a scope to a live deployment.
5. Deliver paste-ready files plus the deploy/admin checklists from `references/setup-and-deploy.md`. I will do the Google authorize/deploy clicks myself unless you have approved direct access to my account.
6. Walk me through `references/test-checklist.md` — especially the scoping tests (a client must not be able to reach another client's thread by guessing IDs; an external sees nothing but their own threads) — and don't call it done until they pass.

---
