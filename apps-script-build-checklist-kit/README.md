# Apps Script Build Checklist Kit

**A pre-deploy checklist for Google Apps Script web apps, distilled
from defects that actually shipped** — so your first build doesn't
repeat them. Run it before every deploy; grep your finished source
for the failure strings it names.

This kit is an **agent skill**: plain-Markdown instructions an AI
agent applies while building or reviewing your app. It follows the
open Agent Skills format (`SKILL.md`) and **works with any capable AI
agent — it is not tied to one vendor.** It pairs with the Apps Script
Deploy Kit in this repository (checklist first, then deploy).

## The greatest hits — what this checklist catches

| Defect | What happens in production |
|---|---|
| Manifest has `gmail.send` but the app calls **MailApp** | Every MailApp call throws for want of `script.send_mail`; try/catch swallows it; submissions "succeed" and **no email is ever sent** |
| Top-level variable named **`history`** | `window.history` is unforgeable, so the variable silently isn't yours, code below it in the script block dies, and a sign-in gate or picker stays disabled forever with no error shown |
| Server expects two scalars, client sends **one object** | Every correct PIN is rejected — and the test harness passes, because it called the server in the signature's shape, not the client's |
| Records joined by **display name** | The same person under a short name in one app and a full name in another never matches; availability and bookings silently detach |
| Blank form fields **overwrite** saved values | A partial save wipes fields the person filled in last week; work is lost with no error anywhere |
| Button restores **only on success** | One dropped response and the button is dead for the rest of the session |
| Workbook timezone ≠ practice timezone | Sheets converts your timestamp strings using the workbook's setting; every stored time shifts by hours and the app code gets blamed |
| Triggers assumed to travel with code | A migrated app runs with no timers at all — no reminders, no cleanup, no warning |

Plus: readonly spreadsheets scope breaking `openById`, undeclared
consent-screen scopes, native dialogs breaking white-label branding,
missing busy feedback, `Number(null)` turning unset fields into 0,
PIN checks compared against a stored hash, custom `addMetaTag` names
taking the whole app down, and more — each with the cheap build-time
fix in `SKILL.md`.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The full checklist: 11 sections (scopes, window-global collisions, white-labeling, production config, triggers, doGet, button feedback, no-data-loss forms, stable-ID joins, argument-shape/PIN verification, spreadsheet timezones) plus a 12-item pre-deploy sweep. An agent should read this first. |
| `PROMPT.md` | A copy-paste starter prompt for chat-based agents. |
| `skill.yaml` | Skill metadata for tools that index skills by file. |

## How to use it

**While building:** hand the kit to your agent at the start (see
`PROMPT.md`) so the rules shape the code, not just the review.

**Before deploying:** run the pre-deploy sweep at the end of
`SKILL.md` against the finished source — including grepping for the
named failure strings, running a global-collision scan on the HTML,
and click-testing interactive gates and pickers in a real browser
(simulated-DOM tests don't reproduce every browser behavior).

**Your values, not anyone else's:** where the checklist needs a
practice-specific standard — your portal header, your palettes, your
ID and PIN-hash scheme — it tells you to copy or document **your
own** reference. Nothing in this kit ships with another practice's
branding, IDs, or configuration baked in.

## Use it with any AI agent

**A. Agent with native skill support** — install or drop this whole
folder where your tool keeps skills, then ask it to use the
`apps-script-build-checklist-kit` skill when building or reviewing
your app.

**B. Coding agent with a workspace** — unzip this kit into a project
folder, open it in the tool, and send the starter prompt in
`PROMPT.md`.

**C. Chat-only agent** — start a new conversation, upload this kit's
`.md` files plus your app's files, then paste the starter prompt from
`PROMPT.md` and ask for a checklist review before you deploy.

## What it is not

- Not a guarantee: a checklist catches the known repeat defects. You
  still test your own app's logic, with a harness that calls server
  functions in the exact shapes your client sends.
- Not a style guide for your brand: it enforces *consistency with
  your own* reference app and audience-appropriate styling, whatever
  those are.
- Not a substitute for verifying the live deploy — that's the Apps
  Script Deploy Kit's job (read-back, existing-deployment bump,
  served-URL verification).

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address from your browser's address bar, paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
