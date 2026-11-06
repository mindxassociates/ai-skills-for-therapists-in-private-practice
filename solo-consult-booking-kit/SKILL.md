---
name: solo-consult-booking-kit
description: A HIPAA-supporting initial-consultation booking system for a SOLO therapy private practice, built on Google Workspace + Apps Script + Sheets + Calendar. Use when a solo practice owner wants (1) a public booking page where prospective clients book a free initial consultation against the owner's real calendar availability, with confirmation / reminder / follow-up emails and a private reschedule-cancel link; and (2) one private owner console to set weekly consult hours, date-specific hours and time off, view upcoming consults and mark no-shows, and edit email templates and booking rules. Adapted from a group-practice system (public Booking app + Manage Availability + My Consults + Consult Admin) — the solo edition merges the three staff apps into one console and drops the group edition's calendar-connection app entirely.
---

# Solo Consult Booking Kit — Initial-Consultation Booking for a Solo Practice

## ⚠️ Read this first — the HIPAA prerequisite (before you build anything)

**This system is only HIPAA-supporting if it runs inside a Google Workspace
account with a signed Business Associate Agreement (BAA). Do not build,
deploy, or put real client data into it until all of the following are true:**

1. **You have Google Workspace** (Business Starter, Standard, Plus, or an
   equivalent covered edition) on your practice's own domain — **not** a
   free personal Gmail account (`@gmail.com`). A personal account has no
   BAA available to sign and must never hold this system or its data.
2. **The Google Workspace BAA is signed.** In the Google Admin console
   (Admin → Account → Legal / "Business Associate Amendment" — the exact
   menu name changes over time), review and accept the BAA for Google
   Workspace / Cloud Identity, and keep a record of the date. Signing is
   a one-time click-through by a Workspace admin; if you can't find it,
   stop and resolve that first — do not proceed on the assumption it's
   covered.
3. **Everything lives in that Workspace account.** The Apps Script
   projects, the booking spreadsheet, the calendar that receives
   consults, and the mailbox that sends confirmations must all belong to
   the same Workspace user (you). Do not run any part of this on a
   personal Google account, and do not point bookings at a personal
   calendar — a personal account sits outside the BAA.
4. **Account hardening is on:** 2-Step Verification enforced for the
   account (passkeys / Advanced Protection are better), a strong unique
   password in a password manager, and recovery options you control.

Software cannot be "HIPAA certified," and this kit does not make a
practice HIPAA compliant by itself. It is built with HIPAA-supporting
safeguards (data minimization, hashed expiring manage links, generic
calendar events, retention sweep, audit log — see
`references/security-and-hipaa.md`), and it runs on a vendor (Google)
that will sign a BAA. Compliance also requires your own risk analysis,
policies, training, and a Notice of Privacy Practices. If any
prerequisite above is missing, the agent's first job is to help the
owner fix that — not to build the apps.

## Purpose

Give a solo clinician the booking system a group practice uses, without
the group machinery:

- **Part A — Public Booking app.** A public web page (embedded on the
  practice website) where a prospective client answers a short fit
  check (state, payment, who the consult is for, language), sees only
  genuinely open slots — your declared consult hours minus your real
  calendar's busy times, time off, and existing bookings — and books a
  free initial consultation (15 minutes by default; configurable).
  The client gets a confirmation email with an .ics file and a private
  reschedule/cancel link; you get a minimal notification. Reminders
  (~24h before) and post-consult follow-ups run on a timer.
- **Part B — Owner Console (one app, three views).** A private,
  PIN-gated app only you use, merging what a group practice splits
  across three apps:
  - **My Consults** — upcoming / past / cancelled consults, full
    details on click, mark a past consult as no-show.
  - **Availability** — set weekly consult hours (split days allowed),
    date-specific hours, time off, accepting-new-clients on/off, and
    booking settings (one consult-frequency cap, minimum notice,
    buffers, slot increment); see your resolved availability and the
    next 7 days of open slots exactly as the booking page computes
    them.
  - **Settings & Tools** — edit every email template and booking rule
    without touching code, view booking stats and the audit trail,
    export audit / bookings CSV (never the manage tokens).

Reference implementation: two Google Apps Script web apps backed by
**one** spreadsheet and your own Google Calendar. No third-party
booking service, no analytics, no trackers.

## What the solo edition deliberately drops (group → solo)

- **No "Connect Your Calendar" app.** In a group practice that app
  exists for one reason: each provider, signed in as *themselves*,
  shares *their* calendar with the practice's central account at
  "Make changes to events" and registers the calendar ID back with the
  booking system. A solo owner **is** the script owner and the calendar
  owner — the booking app already runs as you, with owner access to
  your calendar. There is nothing to share and nothing to register.
  Setup is just: put your calendar's ID in the Config tab (your primary
  calendar's ID is simply your email address; or create a dedicated
  "Initial Consultations" calendar in the same Workspace account and
  use its ID), then run the built-in `checkSetup()` and confirm it
  reports `accessRole=owner` and `freebusy=OK`.
- **No provider roster workbook and no roster sync.** One clinician =
  one Config row holding name, credentials, licensed states, panels,
  languages, ages served, sliding-scale flag, bio link, time zone,
  calendar ID. No sync job, no provider IDs handed to anyone else.
- **No provider-matching / routing engine.** The group wizard routes a
  client to the right clinician. The solo wizard only checks *fit
  against you*: wrong state, a panel you don't take, an age group you
  don't serve, or no sliding scale when that's required → a clear
  no-fit message with your contact email, never a dead end.
- **No multi-provider anything:** no per-provider PINs in a shared
  roster (one owner PIN, hashed, in the Config tab), no "edit on
  behalf of," no provider filter, no practice-wide time off (your time
  off is just your time off).

## Handing this to your agent (for the colleague receiving this kit)

This kit is **platform-neutral**: it is plain Markdown (the open Agent
Skills format) and works with any capable AI agent — a skill-loading
agent, a coding agent with a workspace, or a chat-only agent with the
files uploaded. `README.md` in this folder has the per-platform
instructions and `PROMPT.md` has a copy-paste starter prompt; either
route ends at the same place:

1. Confirm the HIPAA prerequisite at the top is met (Workspace + signed
   BAA + hardening). If it isn't, do that first.
2. Answer the setup interview below — the agent should ask once,
   before building.
3. Let the agent build and test both apps, run the test
   checklist in `references/test-checklist.md` with test bookings,
   and only then swap your public links to the new booking page.

Keep your old booking link (if any) live as a fallback until the test
checklist passes end to end.

## Instructions for the agent building this (any platform)

- **Work from these files, not from memory of similar systems.** Read
  this file and every reference before writing code. Where a
  reference and the owner's live instruction conflict, the owner's
  instruction wins and the change gets written down.
- **Your deliverable is files + verified steps, whatever your tools
  are.** Produce each project as paste-ready files (`Code.gs`,
  `Index.html`, `Manage.html` where applicable, `appsscript.json`).
  If you have direct access to the owner's Google account or an Apps
  Script API/deploy path, you may deploy — but only with the owner's
  go-ahead, and you still verify from the served result. If you don't
  have that access (most chat agents don't), hand over the files and
  walk the owner through `references/setup-and-deploy.md` click by
  click: the Google sign-in, scope authorization, and deploy actions
  are the owner's to make, and an agent that can't do them should say
  so plainly rather than imply it deployed something.
- **Test in the shapes production uses.** Build a local harness that
  stubs the spreadsheet/calendar layer and calls every server
  function in the exact argument shapes the shipped client sends.
  Run it after every code change, not just at the end.
- **Never require a vendor-specific feature.** Everything here is
  Google Apps Script + Sheets + Calendar + Gmail plus Markdown. If
  your platform offers a convenience (a deploy integration, a file
  tool), use it, but the build must not depend on it — the same kit
  has to work for the next owner on a different agent.

## Setup interview (collect once, write down, never guess)

- **Prerequisite:** Workspace domain, the account that will own
  everything (e.g. you@yourdomain.com), BAA signed (date), 2-Step
  Verification on.
- **Practice:** practice name, your name + credentials as clients
  should see them, practice contact email, notification email (can be
  the same), website URL, privacy-policy URL.
- **Calendar:** primary calendar, or a dedicated consult calendar in
  the same account? Its ID goes in Config. (Recommended: dedicated
  calendar — consult events stay visually separate, and you can share
  *that* calendar's free/busy without exposing your main calendar's
  contents. Either way the app only ever reads free/busy and writes
  generic consult events.)
- **Fit profile (drives the wizard's payment / eligibility options —
  generated from Config, never hardcoded in the page):** states you
  are licensed in; insurance panels, EAPs, and funds you accept (exact
  client-facing names); self-pay and sliding scale (yes/no, and any
  floor wording you use publicly); languages you offer therapy in;
  who you serve (adults / teens / children / couples / families);
  whether you see clients located outside the U.S. (if yes: consults
  are still free, but ongoing therapy is private-pay/sliding only —
  the wizard restricts payment options accordingly).
- **Booking rules (defaults from the reference system — confirm or
  change):** consult length 15 min; booking window 14 days; minimum
  notice 12 hours; slot grid every 30 minutes; buffer 10 minutes
  around busy events; reschedule/cancel cutoff 4 hours; reminder 24h
  before; post-consult follow-up 5 minutes after the consult ends;
  one active consult per client email/phone (duplicate guard on).
- **Availability to seed:** your initial weekly consult hours + time
  zone, so the page has real slots on day one. (You will maintain
  these in the Console afterwards.)
- **Email wording:** confirmation, reminder, and follow-up templates
  (tokens like `{ClientFirstName}`, `{EventDateTime}`,
  `{ProviderName}`); the survey / next-steps link the follow-up email
  points to; the sender name/address (your address, or a send-as alias
  on your account such as hello@yourdomain.com — aliases need one extra
  OAuth scope, see the deploy reference).
- **Branding:** your website's look for the public page (fonts, text
  color, accent color for buttons/links, corner style). The public
  page uses a flat website style — no portal glass/aurora, no Google
  branding, no native browser dialogs.
- **Language(s):** English only, or bilingual? The reference system
  supports a second full language (one translated question set, emails
  in the language the client booked in). Add it only if you actually
  serve clients in that language.
- **Privacy notice:** the short booking-form privacy wording clients
  must acknowledge (what's collected, that email isn't monitored for
  emergencies, crisis line 988 / 911 in the U.S.). Every booking stores
  the acknowledgment timestamp + notice version. Bump the version
  string whenever the wording changes.

## How it fits together (one paragraph)

Both apps run as you (`USER_DEPLOYING`) inside your Workspace account.
The Booking app is public and anonymous: visitors never see the
spreadsheet or any calendar detail — availability is computed from
free/busy only. A booking, made under a script lock so two visitors
can't take the same slot, writes one row to the Appointments tab,
creates a generic-titled event ("Initial Consultation — <BookingID>",
call-minimum description, no client attendee) on your calendar, and
emails the client (confirmation + .ics + private manage link, token
stored only as a SHA-256 hash) and you (triage minimum, no client name
in the subject). A 5-minute timer sends reminders and follow-ups and
runs the retention sweep. The Console is PIN-gated, reads/writes the
same workbook, and is the only place full booking details are viewed.
Full data model and precedence rules: `references/architecture.md`.

## Build order (do not reorder)

1. **Workbook + Booking app** per `references/booking-app-spec.md` and
   `references/setup-and-deploy.md` (create the sheet, run
   `setupSheet()`, `checkSetup()`, `setupTriggers()`, deploy).
2. **Console app** per `references/console-app-spec.md` (PIN gate,
   My Consults, Availability, Settings & Tools) against the same
   workbook.
3. **Test** with `references/test-checklist.md` — real end-to-end test
   booking, double-booking attempt, reschedule/cancel through the
   emailed link, no-fit path, reminder/follow-up by hand.
4. **Go live:** embed the Booking app on your website's booking page,
   swap public links, keep the old link as fallback until you've taken
   a real booking cleanly.

## Hard rules for the agent (these are the expensive lessons)

- **Scopes:** declare the **full**
  `https://www.googleapis.com/auth/spreadsheets` scope whenever code
  calls `SpreadsheetApp.openById` — the readonly scope makes every
  such call throw. If the app sends mail with **both** GmailApp and
  MailApp, declare **both** `gmail.send` and
  `script.send_mail` (`gmail.send` alone does not cover MailApp, and
  the failures get swallowed by try/catch — mail silently never
  sends). Sending from a send-as alias via GmailApp also needs
  `gmail.settings.basic`. The Calendar features need the Calendar
  Advanced Service (v3) enabled in the manifest.
- **Deployments:** after the first deploy, always bump the **existing**
  deployment to a New version. Never mint a new deployment — a new URL
  breaks every embed and link, and the old URL keeps serving old code.
  Read deployed content back / verify served markers before reporting
  a deploy as done; deployment lists can lag a few seconds behind a
  bump, so re-check before concluding it failed.
- **Triggers don't travel with pasted code.** After any fresh project
  setup, run the setup function that installs the time-driven triggers
  and verify they exist. A system with no sweep sends no reminders.
- **Client/server argument shapes must match exactly.** If the client
  sends one object, the server reads one object (or normalizes both
  shapes). Write the test harness to call server functions in the
  exact shapes the shipped client sends.
- **PIN lockout prune:** when pruning lockout state, never delete
  entries that are still counting (entries whose lock timestamp is 0).
  A prune condition like `until <= cutoff` deletes them on every read
  and the 5-try lockout can never accumulate.
- **Numbers:** map `null` / `undefined` / `''` to NaN *before*
  `Number()` — `Number(null)` is 0, which silently overwrites an
  unset optional setting with 0.
- **No native dialogs** (`alert` / `confirm` / `prompt`) in the web
  apps — they stamp the page with a Google origin and break the
  white-label experience. Use in-page confirmation cards.
- **Never hardcode** fit data (states, panels, languages, fees) into
  the page or code. The wizard's options are generated from the Config
  tab on every load, so a panel change is a sheet edit, not a deploy.
- **PHI minimization is baseline, not an upgrade:** generic calendar
  titles, no client attendee on calendar events, triage-minimum
  notification emails, no client name in email subjects, goals brief
  capped (600 chars) with an on-form warning against detailed clinical
  history, generic error text to clients (raw errors only in the
  execution log), hashed + expiring + rotating manage tokens,
  retention sweep, and an append-only AuditLog of IDs/times only.
  See `references/security-and-hipaa.md`.
- **No waitlist.** If no slot or no fit, direct the client to your
  contact email. Don't add a waitlist, payments, SMS, or third-party
  services unless the owner explicitly asks.
- **Verify from the artifact, not from say-so:** read the sheet back
  after writes, read served code after deploys, run the harness after
  code changes, and report failures as failures with the actual state.
