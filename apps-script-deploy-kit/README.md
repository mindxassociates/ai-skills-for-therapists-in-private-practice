# Apps Script Deploy Kit

**Deploy Google Apps Script web apps through the Apps Script API —
with your own OAuth client — instead of pasting code into the editor.**
You push the exact files you tested, read them back, create a version,
and bump the *existing* deployment to it, so your live `/exec` URL
never changes and a failed write never gets frozen into a release.

This kit is an **agent skill**: plain-Markdown instructions that an AI
agent (or a small deploy script you control) follows to deploy your
apps the same verifiable way every time. It follows the open Agent
Skills format (`SKILL.md`) and **works with any capable AI agent — it
is not tied to one vendor.**

## What problem this solves

- Editor paste is easy to get wrong: an old file, a missed file, or a
  version that doesn't match what you tested.
- A brand-new deployment mints a brand-new URL — and every website
  embed, portal link, and bookmark pointing at the old URL keeps
  serving the old code, silently.
- A write can report success and still not have landed. Without a
  read-back, you can snapshot the *previous* content as your "new"
  version and ship nothing while believing you shipped the fix.

The kit's sequence — confirm project title → push exact file set →
read back and compare → create version → bump the existing deployment
→ verify from the served URL — closes each of those holes.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The main playbook: setting up your own deployer OAuth client, credential hygiene, the 7-step deploy sequence, per-app setup interview, hard rules. An agent should read this first. |
| `PROMPT.md` | A copy-paste starter prompt for chat-based agents. |
| `skill.yaml` | Skill metadata for tools that index skills by file. |

## You bring your own everything

- **Your own Google Workspace account** — the admin account that owns
  your Apps Script projects.
- **Your own Google Cloud project** in that account, with the Apps
  Script API and Drive API enabled, and an **Internal** OAuth consent
  screen with the scopes listed in `SKILL.md`.
- **Your own Desktop OAuth client**, created by you in your console.
  Its credentials live in one private, owner-only location outside
  any repository. This kit never asks for, stores, or transmits
  credential values — and you should never paste them into a chat,
  a note, or a shared file.

If you don't have the OAuth client yet, `SKILL.md` walks through
setting it up; the one-time consent is always clicked by you, the
account owner, in your own browser.

## Use it with any AI agent

**A. Agent with native skill support** — install or drop this whole
folder where your tool keeps skills, then ask it to use the
`apps-script-deploy-kit` skill to deploy your app.

**B. Coding agent with a workspace** — unzip this kit into a project
folder, open it in the tool, and send the starter prompt in
`PROMPT.md`. The agent writes (or adapts) a small deploy helper
against the Apps Script API and runs the sequence with you.

**C. Chat-only agent** — start a new conversation, upload this kit's
`.md` files, then paste the starter prompt from `PROMPT.md`. The
agent can prepare files, commands, and checklists — but the Google
sign-in, OAuth consent, and any console clicks are always yours.

**What to expect on every route:** the agent confirms the target
project's title before pushing, pushes only the intended file set,
reads the content back before versioning, bumps your existing
deployment (never a new one), and verifies from the served `/exec`
URL before reporting success. If an agent wants to skip the read-back
or create a fresh deployment "just this once," stop it — the kit's
hard rules exist because those shortcuts have shipped stale code.

## What it is not

- Not a way to deploy with someone else's credentials or project —
  there is nothing shared to borrow; you set up your own client.
- Not a code editor or a build system: you still write and test your
  app files first (the companion Apps Script Build Checklist Kit
  covers the recurring build-time defects to check before you deploy).
- Not a shortcut around verification: a successful API response is
  the start of the check, not the end of it.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address from your browser's address bar, paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
