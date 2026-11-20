# Starter prompt — copy, paste, send to your AI agent

Use this with any AI agent (skill-based, coding-workspace, or
chat-only). If your agent doesn't load skill folders automatically,
upload or include all of this kit's files first (`SKILL.md` and this
file), then paste the prompt below.

---

Deploy my Google Apps Script web app through the API using the Apps
Script Deploy Kit I've given you.

Work in this order, and don't skip steps:

1. Read `SKILL.md` in full before running anything.
2. Check my deployer setup with me: my own Google Workspace admin
   account, my own Cloud project with the Apps Script API and Drive
   API enabled, an Internal OAuth consent screen with the scopes the
   kit lists, and my own Desktop OAuth client whose credentials live
   in a private, owner-only location outside any repo. If any of that
   is missing, walk me through setting it up first. Never ask me to
   paste a credential or token value into this chat — refer to them
   by location only. The one-time OAuth consent is mine to click in
   my own browser.
3. Ask me the kit's per-app setup interview: app name, project title,
   script ID (or "new project"), which deployment is canonical and
   where its /exec URL is used, execute-as and access level, the exact
   file set, and how we'll verify. Write my answers down; never guess
   an ID or a URL.
4. Before pushing, read the target project and confirm its title
   matches the app I named. If it doesn't match, stop and tell me.
5. Push the exact files I tested (Code.gs, the HTML files,
   appsscript.json) via projects.updateContent — the exact intended
   file set, nothing extra. Then read the project content back and
   compare it with my local files. If the read-back differs, do not
   create a version; tell me what differs.
6. Create a version, then update the EXISTING canonical deployment to
   that version. Never create a new deployment for an app that is
   already live — a new deployment means a new URL and a stale old
   one. After the update, wait a few seconds and list deployments
   again before concluding anything; the list can lag.
7. Verify from the served /exec URL: HTTP 200, and markers that only
   the new version contains. If the change is interactive, click-test
   it in a real browser. Run the one end-to-end test we agreed on,
   then clean up the test data and confirm the source is back to its
   original state.
8. Deploy one app at a time. If a call fails with a quota-style
   error, wait and retry the same step instead of changing code.
9. Report failures as failures, with the actual state — never report
   a deploy as done because an API call returned success.

Start by confirming you've read the kit and checking my deployer
setup with me.

---
