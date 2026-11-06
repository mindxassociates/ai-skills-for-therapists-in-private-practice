# Group Consult Booking Kit

**A HIPAA-supporting, Acuity-Scheduling-style booking system for a
group therapy practice — with no per-provider monthly subscriptions.**
One public booking page routes each prospective client to the right
clinician (state/license, insurance panel, language, age group) and
books against that clinician's real Google Calendar availability.
Providers connect their own calendars, set their own consult hours,
and view their own consults; the practice admin oversees everything
from one console. Built entirely on Google Workspace (Apps Script +
Sheets + Calendar + Gmail).

This kit is an **agent skill**: plain-Markdown build specs, in the
open Agent Skills format (`SKILL.md` + `references/`), that an AI
agent turns into the working apps for *your* practice. **It works
with any capable AI agent — it is not tied to one vendor.**
Solo practice? Use the companion **Solo Consult Booking Kit** instead —
same system minus the roster, routing, and calendar-connection app.

## ⚠️ Before anything else — the HIPAA prerequisites

1. **Google Workspace** on the practice's own domain, with **Google's
   Business Associate Agreement (BAA) signed** in the Admin console.
   Personal `@gmail.com` accounts have no BAA and must not run the
   central system.
2. The central system (scripts, workbooks, sending mailboxes) lives
   in **one practice Workspace account** with 2-Step Verification on.
3. **Decide your provider-calendar policy:** providers connecting
   calendars owned by practice Workspace accounts keeps everything
   inside the BAA. Providers connecting *personal* calendars is
   workable — the system sends only generic, minimum-detail events to
   those calendars — but those calendars sit outside the BAA, and the
   practice must document that as its own risk decision.

No software is "HIPAA certified." Full details: `SKILL.md` (top) and
`references/security-and-hipaa.md`.

## The five apps you end up with

| App | Who uses it | What it does |
|---|---|---|
| Public Booking | Clients | One booking page; routes by fit, books real slots, emails + manage link |
| Connect Your Calendar | Providers (once) | Provider shares their calendar with the practice account and registers it — self-service, no manual steps |
| Manage Availability | Providers | Weekly/date-specific consult hours, time off, accepting toggle, booking settings, "what clients can book" panel |
| My Consults | Providers | Their consults, full details, mark no-show (admin sees all) |
| Consult Admin | Practice admin only | Availability oversight + edit-on-behalf, email templates & booking rules, stats/audit/exports |

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | Main playbook: prerequisites, setup interview, build order, hard rules. Read first. |
| `PROMPT.md` | Copy-paste starter prompt for chat-based agents. |
| `references/architecture.md` | Components, the three data stores, routing + availability math, timers. |
| `references/booking-app-spec.md` | The public booking app: wizard, routing, emails, settings keys, setup functions. |
| `references/connect-your-calendar-spec.md` | The provider calendar-connection app, its booking-app API, OAuth verification, and the manual-sharing fallback. |
| `references/provider-apps-spec.md` | Manage Availability + My Consults: the shared PIN scheme, submissions model, consult views. |
| `references/consult-admin-spec.md` | The admin console's three views. |
| `references/security-and-hipaa.md` | Risk analysis, scope justifications, incident response. Keep with your compliance files. |
| `references/setup-and-deploy.md` | Deployment order, provider onboarding, cutover, day-to-day administration. |
| `references/test-checklist.md` | End-to-end tests to pass before cutover. |

## Use it with any AI agent

You need an agent that can write and revise code files across several
steps. Pick the route that matches yours:

**A. Native skill support** (e.g. Muse, Muse, other Agent
Skills tools): install this folder where your tool keeps skills, then
ask it to use the `group-consult-booking-kit` skill.

**B. Coding agent with a workspace** (e.g. Cursor, Windsurf, Copilot,
Replit): unzip the kit into a project folder, open it, and send the
starter prompt in `PROMPT.md`.

**C. Chat-only agent** (e.g. ChatGPT, Claude.ai, Gemini): start a new
conversation, upload **all** `.md` files in this kit, then paste the
starter prompt from `PROMPT.md`. The agent interviews you, writes the
app files in chat for you to save, and walks you through pasting them
into Google Apps Script and deploying — the Google sign-in,
authorization, and deploy clicks are the practice admin's to make, on
any platform.

**What to expect on every route:** the agent confirms the
prerequisites (including the provider-calendar policy), asks the
setup interview once, builds and tests before any deploy, onboards
providers (calendar connection + hours) before cutover, and keeps the
old booking links live until the test checklist passes. If an agent
tries to skip the BAA, hardcode your roster into the page, or go live
without `checkSetup()` passing for every provider, stop it — the
kit's hard rules say not to.

**No agent?** The specs are complete enough to hand to a human
developer as a build brief.

## What it is not

- Not a general scheduler: **initial consultations only.** Ongoing
  therapy scheduling stays in your EHR.
- Not payments, SMS, or a waitlist; no third-party services or
  trackers on the booking page.
- Not a substitute for the practice's HIPAA policies, training, risk
  analysis, or Notice of Privacy Practices.
