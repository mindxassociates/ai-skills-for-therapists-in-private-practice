# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build me a referral network for my therapy practice using the Referral Network Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — my practice name, the admin email that should receive submission notices, which service types the directory covers, whether I want just the internal add form or also the public "get recommended" form, and whether the directory needs a second language view. Do not build anything until I have answered, and never guess a value — use a placeholder and flag it.
2. Build the three pieces from the reference specs:
   - the **directory sheet** (`references/data-model.md`)
   - the **read-only directory app** (`references/directory-app-spec.md`)
   - the **add form** — internal edition, and the public edition too if I chose it (`references/add-form-spec.md`)
3. Obey the kit's hard rules: the sheet is the single source of truth and the directory reads it live on every page load; duplicate provider names are rejected case-insensitively; new entries are inserted at the end of their service-type section; the admin email fires on every submission but a failed email never fails a submission; the directory contains professional public information only, never client data.
4. Deliver paste-ready files for each Apps Script project (Code.gs, Index.html, appsscript.json) plus a deploy checklist from `references/setup-and-deploy.md`. I will do the Google authorize/deploy clicks myself unless you have approved direct access to my account.
5. Walk me through `references/test-checklist.md` at the end and don't call it done until the duplicate test, the section-grouping test, and the live-edit test (change the sheet → reload the directory → see the change) all pass.

---
