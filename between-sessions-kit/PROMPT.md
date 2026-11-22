# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build me a between-session client homework system for my therapy practice using the Between Sessions Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — practice name and sender alias, languages and who authors the translations, catalog starting point, provider list and PIN source, whether assessments stay in the EHR, crisis copy and which items flag, whether the public self-guided index is on, and where the client pages will live. Read `references/security-and-privacy.md` with me and confirm the practice accepts the stated limits (token links are bearer links; the workbook holds client data and is shared with nobody; not monitored in real time) **before** building. Do not build anything until I have answered, and never guess a value — use a placeholder and flag it.
2. Build in the kit's order: the **workbook + catalog generation + provider seed** (`references/data-model.md`, `references/catalog-format.md`), the **server core** (PIN gate, token resolution), the **provider app**, the **client app**, then the **reminder engine and triggers** (`references/reminder-engine.md`), review/flags and the custom-exercise builder, and finally the public pages and hardening.
3. Obey the kit's hard rules: **no SMS anywhere** (email + copy-link only); **no client accounts** (one token link per assignment); reminder times are read in the **client's timezone**; an early submission credits the pending instance and the engine **never re-reminds submitted work**; server functions **never return a `Date` or `NaN`** to the client (coerce to text / clean numbers — one bad value nulls the whole payload); assignment creation materialises only the next **60 days** of instances in **one bulk write**, with a nightly top-up; client-facing steps come only from **authored** step data and **authored** translations; and all joins are by stable ID, never by name.
4. Declare **all** manifest scopes the code uses — spreadsheets (full), both mail scopes if both mail APIs are called, the send-as settings scope if a no-reply alias is used, and Drive if backups are built in — and remember that adding a scope to a live deployment walls the app behind an authorization error until the owner re-grants: sequence it, don't discover it.
5. Deploy with the kit's discipline: restore point before every push, verify the project **title** before pushing, bump the **existing** deployment (never mint a new URL), never re-run the trigger installer, and verify from the **served** page after every bump.
6. Walk me through `references/test-checklist.md` — the harness with **live-shaped fixtures** (real date cells, empty score cells), then the live click-test stages with a throwaway client — and don't call it done until they pass and the test data is cleaned out.

---
