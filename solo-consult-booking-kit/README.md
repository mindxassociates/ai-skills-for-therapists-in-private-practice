# Solo Consult Booking Kit

**A HIPAA-supporting, Acuity-Scheduling-style booking system for a solo
therapy private practice — with no monthly subscription.** Prospective
clients book a free initial consultation against your real Google
Calendar availability; you manage hours, consults, email templates, and
booking rules from one private console. Built entirely on Google
Workspace (Apps Script + Sheets + Calendar + Gmail), so the only cost
is the Google Workspace subscription you already pay for.

This kit is an **agent skill**: a set of plain-Markdown build specs
that an AI agent turns into the two working apps for *your* practice.
It follows the open Agent Skills format (`SKILL.md` + `references/`)
and **works with any capable AI agent — it is not tied to one vendor.**

## ⚠️ Before anything else — the HIPAA prerequisite

Do not build or use this with real client data until you have:

1. **Google Workspace** on your practice's own domain (not a free
   `@gmail.com` account — personal accounts have no BAA), and
2. **Signed Google's Business Associate Agreement (BAA)** in the
   Google Admin console, and
3. Everything (scripts, spreadsheet, calendar, mailbox) inside that
   one Workspace account, with 2-Step Verification on.

No software is "HIPAA certified." This system is built with
HIPAA-supporting safeguards and runs on a vendor that signs a BAA;
compliance also needs your own policies and risk analysis. Full
details: `SKILL.md` (top section) and
`references/security-and-hipaa.md`.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The main playbook: prerequisite, setup interview, build order, hard rules. An agent should read this first. |
| `PROMPT.md` | A copy-paste starter prompt for chat-based agents. |
| `references/architecture.md` | How the pieces fit: one workbook, availability math, booking flow, timers. |
| `references/booking-app-spec.md` | The public booking app: wizard, emails, calendar events, settings. |
| `references/console-app-spec.md` | Your private console: My Consults + Availability + Settings & Tools in one app. |
| `references/security-and-hipaa.md` | Risk analysis, scope justifications, incident response. Keep with your compliance files. |
| `references/setup-and-deploy.md` | Step-by-step setup and deployment, plus day-to-day administration. |
| `references/test-checklist.md` | The end-to-end tests to pass before you swap your public links. |

The system you end up with is **two** Apps Script projects (a public
Booking app and a private Owner Console), **one** spreadsheet, and
your own calendar. There is deliberately no third "connect your
calendar" app — as a solo owner you own the calendar, so there is
nothing to connect.

## Use it with any AI agent

You need an agent that can write and revise code files across several
steps. Pick the route that matches your agent:

**A. Agent with native skill support** (e.g. Muse, Muse, and
other tools that load Agent Skills folders)
Install or drop this whole folder where your tool keeps skills, then
ask it to use the `solo-consult-booking-kit` skill to build your
booking system.

**B. Coding agent with a workspace** (e.g. Cursor, Windsurf, Copilot,
Replit, or a local coding agent)
Unzip this kit into a project folder, open that folder in the tool,
and send the starter prompt in `PROMPT.md`. The agent builds the app
files (`Code.gs`, `Index.html`, etc.) in the workspace.

**C. Chat-only agent** (e.g. ChatGPT, Claude.ai, Gemini — no files, no
account access)
Start a new conversation, upload **all** the `.md` files in this kit
(`SKILL.md`, `PROMPT.md`, and everything in `references/`), then paste
the starter prompt from `PROMPT.md`. The agent will interview you,
write the app files in the chat for you to save, and walk you through
pasting them into Google Apps Script and deploying — those Google
sign-in, authorization, and deploy clicks are always yours to make,
on any platform.

**What to expect on every route:** the agent asks the setup interview
once (practice details, licensed states, panels, hours, email
wording), builds and tests locally first, and deploys only after the
test checklist passes. If an agent tries to skip the BAA prerequisite,
hardcode your fees/panels into the page, or go live without testing,
stop it — the kit's hard rules say not to.

**No agent?** The specs are complete enough to hand to a human
developer or a technically confident colleague as a build brief.

## What it is not

- Not a general scheduler: it books **initial consultations** only.
  Ongoing therapy scheduling stays in your EHR.
- Not payments, not SMS, not a waitlist, no third-party services or
  trackers on the booking page.
- Not a substitute for your HIPAA policies, training, risk analysis,
  or Notice of Privacy Practices.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/solo-consult-booking-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
