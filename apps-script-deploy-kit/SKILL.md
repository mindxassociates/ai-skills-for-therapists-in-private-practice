---
name: apps-script-deploy-kit
description: Deploy Google Apps Script web apps through the Apps Script API with your own OAuth client, instead of pasting code into the editor. Use when a practice owner or their agent wants to (1) set up a private deployer OAuth client under their own Google Workspace account; (2) create or update an Apps Script project by pushing Code.gs, HTML files, and appsscript.json via projects.updateContent; (3) create a version and bump the EXISTING deployment to it — never minting a new deployment URL; and (4) verify the deploy from the served /exec URL and from a content read-back before calling it done.
---

# Apps Script Deploy Kit — Deploy Through the API, Not the Editor

## Why deploy through the API

Pasting code into the Apps Script editor is slow, error-prone, and
hard to verify: it is easy to paste an old file, miss a file, or deploy
a version that does not match the files you tested. Deploying through
the Apps Script API fixes that:

- The local folder is the single source of truth. You push the exact
  bytes you tested.
- Every step is scriptable and repeatable — the same push, version,
  and deployment-bump sequence for every app, every time.
- You can read the project back after a write and compare it to your
  local files before you snapshot a version, so a failed or partial
  write never gets frozen into a release.

This kit is platform-neutral Markdown. It works with any capable AI
agent, and the deploy helper can be a small script in any language
that can make authenticated HTTPS calls to Google APIs.

## Before you start — set up your own deployer OAuth client

You deploy with **your own** OAuth client, under **your own** Google
Workspace admin account, in **your own** Google Cloud project. Never
use someone else's client, credentials, or project, and never ask
anyone to share theirs with you.

Setup interview — collect these once, write them down (without any
secret values), and never guess them:

- **Owner account:** the Workspace admin account that will own the
  Apps Script projects (your admin address at your own domain).
- **Cloud project:** a Google Cloud project you create in that
  account's organization, dedicated to deploying (one project can
  serve all your apps).
- **APIs to enable** in that project: Apps Script API, Drive API.
  Enable the Google Sheets API as well if your helper also reads or
  writes spreadsheets directly.
- **OAuth consent screen:** Audience = **Internal** (so only your own
  organization's accounts can consent, and refresh tokens are
  long-lived). Add these scopes under Data Access:
  - `https://www.googleapis.com/auth/script.projects`
  - `https://www.googleapis.com/auth/script.deployments`
  - `https://www.googleapis.com/auth/drive`
  - `https://www.googleapis.com/auth/userinfo.email`
- **Client type:** Desktop app client. Download its JSON once, through
  your own browser, from your own Cloud console.

### Credential hygiene (hard rules)

- Store the client JSON and any token file in **one private location
  outside any code repository** — for example a config folder in your
  home directory that only your OS user can read. Set the folder to
  owner-only permissions (700) and the files to owner read/write only
  (600).
- **Never** print, paste, copy, or store credential or token values in
  chat, in notes or memory files, in a skill, in a spreadsheet, or in
  any file that gets shared, synced to a public repo, or committed.
  Refer to credentials by location and purpose only, never by value.
- If a token is revoked or a credential is ever exposed, delete it in
  the Cloud console, create a new client, and re-run the one-time
  consent flow as the owner account. Treat exposure as an incident,
  not an inconvenience.
- The one-time consent itself (opening the authorization URL, signing
  in, approving, exchanging the code) is always done by the account
  owner, in their own browser. An agent prepares the URL and the
  commands; the owner clicks the consent.

## Pick the route first

- **Default: the API route in this kit**, once your deployer client
  exists. It is faster and verifiable.
- **Editor paste is the fallback**, for example when the owner prefers
  to paste and deploy themselves (common for a bulk restyle with no
  logic changes). Then your deliverable is the exact files plus a
  short checklist, and the owner does the paste + deploy clicks.
- Do not send a helper or sub-agent to type code into the web editor
  as the primary route — editor automation is brittle, and a stall
  there looks like progress while nothing has actually been written.

## The deploy sequence (every time, in this order)

### 1. Confirm the project before you touch it

- Resolve the target project from your own project list: title,
  script ID, and the deployment you intend to bump. **Read the project
  first and confirm its title matches the app you mean to deploy.**
  Project IDs are easy to mix up in notes, and pushing App A's files
  into App B's project is a real, silent failure mode. If the title
  does not match, stop.
- For a brand-new app: create the project under your own Workspace
  admin account, name it for the app, and keep its script ID in your
  deploy notes (IDs are configuration, not secrets — but keep them in
  your private notes, not in shared code).

### 2. Push the exact tested files with projects.updateContent

- Keep the local app folder as the source of truth: typically
  `Code.gs`, one or more HTML files (e.g. `Index.html`), and
  `appsscript.json`.
- Write those files through the Apps Script API method
  `projects.updateContent`. Send the **exact file set** the project
  should hold — no more, no fewer. If the local folder contains extra
  HTML files (previews, test pages), exclude them explicitly; a push
  built from a directory glob will happily upload them into the
  project.
- Keep the exact bytes you tested locally. Do not reformat, re-save
  through a text editor that changes line endings, or "fix" anything
  during the push.

### 3. Read back before you version

- Call `projects.getContent` (or your helper's equivalent) and compare
  the returned files with your local files — names, count, and
  content.
- **Treat a write that reports success with suspicion when the
  read-back differs.** A masked write error can otherwise be
  snapshotted as the next version, which then silently carries the
  *previous* content while everyone believes the fix shipped.
- Optionally reload the project in the editor and confirm the function
  dropdown lists every expected function before you call the write
  done.

### 4. Create a version

- Only after the read-back matches, create a new version
  (`projects.versions.create`) with a short description of the change.
- A deployment serves its pinned version forever. Creating the version
  does not change what any live URL serves — that is the next step.

### 5. Bump the EXISTING deployment — never mint a new URL

- List the project's deployments, find the canonical one (the one
  whose `/exec` URL is embedded on your website, linked in your
  portal, or shared with your team), and update **that** deployment
  (`projects.deployments.update`) to point at the new version.
- **Never create a fresh deployment for an existing app.** A new
  deployment mints a new `/exec` URL, leaves the old URL serving the
  old code forever, and breaks every embed and bookmark that points
  at the canonical URL.
- The one exception is an app's very first deploy: create the
  deployment once (Execute as: Me / your deploying identity; access
  set to what the app needs — e.g. "Anyone" for a public page,
  organization-only for an internal tool), record its `/exec` URL as
  canonical, and bump that deployment from then on.
- After a bump, wait a few seconds and list deployments again before
  concluding anything: the deployments list can lag the update
  response by several seconds, and a stale first read has made more
  than one good deploy look failed. Re-check, don't re-deploy.

### 6. Verify from the served URL

- Open the canonical `/exec` URL and check it returns HTTP 200 and
  renders the expected UI — look for markers that only the new version
  contains (a new heading, button, or version string), not just "a
  page loaded." An old version also loads fine.
- For interactive changes (a gate, a picker, a form), a string check
  on served HTML is **not** verification: click-test it in a real
  browser — the field enables, the list opens, the action completes.
- Run one end-to-end test that writes a real record (a test row, a
  test booking), confirm the result landed where designed, then
  delete the test data and verify the data source is back to its
  original state.

### 7. Pace deploys

- Deploy **one app at a time**. Parallel or rapid-fire deploys can
  trip Google's per-minute quotas and fail in ways that look like
  code errors. If a deploy fails with a quota-style error, wait and
  retry the same step — do not change code to chase it.

## Setup interview for each app you deploy

Ask once per app, before the first push:

1. App name and the project title to match it against.
2. Script ID (existing app) or "new project" — and who owns it.
3. The canonical deployment: which deployment is live, and where its
   `/exec` URL is used (website embed, portal link, shared doc).
4. Execute-as identity and access level the deployment should have.
5. The exact file set the project should hold.
6. What "verified" means for this app: the served-page markers and
   the one end-to-end test you will run after the bump.

## Hard rules

- Your own OAuth client, your own Workspace account, your own Cloud
  project. No borrowed credentials, ever.
- Credentials live in one private, owner-only location outside the
  repo; their values never appear in chat, files, or notes.
- Confirm the project title by reading the project before every push.
- Push the exact tested bytes and the exact intended file set.
- Read back and compare before creating a version.
- Bump the existing deployment; never mint a new URL for a live app.
- Verify from the served `/exec` URL (and by click-testing interactive
  changes), not from the push response.
- One deploy at a time; treat quota errors as pacing problems.
- Report failures as failures, with the actual state you observed —
  never report a deploy as done because a call returned success.
