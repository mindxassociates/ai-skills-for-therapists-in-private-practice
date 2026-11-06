---
name: group-consult-booking-kit
description: A HIPAA-supporting initial-consultation booking system for a GROUP therapy practice, built on Google Workspace + Apps Script + Sheets + Calendar. Use when a group practice owner/admin wants (1) a single public booking page that routes each prospective client to the right clinician by state/license, insurance panel, language, age group, and preferences, booking against each provider's real calendar availability; (2) provider self-service apps to connect their calendar, set consult availability, and view their consults; and (3) an admin console to oversee availability, edit email templates and booking rules, and audit bookings. Five Apps Script projects (Public Booking, Connect Your Calendar, Manage Availability, My Consults, Consult Admin) backed by a provider roster and a booking workbook. This is the group edition; solo practices should use the Solo Consult Booking Kit instead, which drops the roster, the routing, and the calendar-connection app.
---

# Group Consult Booking Kit — Initial-Consultation Booking for a Group Practice

## ⚠️ Read this first — the HIPAA prerequisites (before you build anything)

**This system is only HIPAA-supporting if it runs inside a Google
Workspace account with a signed Business Associate Agreement (BAA).
Do not build, deploy, or put real client data into it until all of
the following are true:**

1. **The practice has Google Workspace** on its own domain (Business
   Starter / Standard / Plus or equivalent) — **not** free personal
   Gmail accounts. Personal accounts have no BAA available to sign.
2. **The Google Workspace BAA is signed** in the Google Admin console
   by a Workspace admin, with the date recorded. If you can't find
   where to accept it, stop and resolve that first.
3. **The central system lives in one practice Workspace account**
   (call it the *practice account* — e.g. admin@yourdomain.com): the
   Apps Script projects, the roster workbook, the booking workbook,
   and the sending mailboxes all belong to it, with 2-Step
   Verification enforced (passkeys / Advanced Protection preferred).
4. **Decide your provider-calendar policy explicitly — this is the
   group edition's one structural HIPAA question.** Providers'
   calendars receive consult events, so where those calendars live
   matters:
   - **Best:** every provider has a practice Workspace account and
     connects a calendar owned by it — everything stays inside the
     BAA.
   - **Workable, with eyes open:** providers connect a calendar from a
     personal Google account. That calendar then sits *outside* the
     practice's Workspace BAA. The system minimizes what lands there
     (generic event title "Initial Consultation — <BookingID>",
     call-minimum description, no client attendee, no clinical text),
     but the practice must document this as its own risk decision —
     see `references/security-and-hipaa.md`. Never present this
     configuration as fully BAA-covered.
   Either way, record the decision in the practice's risk analysis
   before the first provider connects.

Software cannot be "HIPAA certified," and this kit does not make a
practice HIPAA compliant by itself. It is built with HIPAA-supporting
safeguards (data minimization, hashed expiring manage links, generic
calendar events, retention sweep, audit log) on a vendor that signs a
BAA. Compliance also requires the practice's own risk analysis,
policies, training, and Notice of Privacy Practices. If any
prerequisite above is missing, the agent's first job is to help fix
that — not to build the apps.

## Purpose — the five apps

- **Public Booking app** (clients). One front door on the practice
  website. A short wizard (location → payment → preferences →
  choose a clinician/time → details + privacy acknowledgment) routes
  the client only to clinicians who fit: licensed in their state, on
  their panel/EAP, serving their age group and language, offering
  sliding scale if they need it. Slots are real: each provider's
  declared consult hours minus their calendar's busy times, time off,
  and existing bookings. Confirmation + reminder + follow-up emails,
  and a private reschedule/cancel link.
- **Connect Your Calendar** (providers, one-time). Each provider,
  signed in as *themselves*, picks the calendar their schedule lives
  on and shares it with the practice account at "Make changes to
  events," registering it with the booking system — no manual
  sharing steps, no admin touching provider accounts. **Yes, the
  group edition includes this app** — it is the piece that makes a
  multi-provider system self-service at all. (The solo edition omits
  it because a solo owner already owns the calendar the booking app
  runs on; in a group, the booking app runs as the practice account
  and has *no* access to anyone's calendar until they share it.)
  Manual calendar sharing remains an equivalent fallback.
- **Manage Availability** (providers). Weekly consult hours (split
  days allowed), date-specific hours, time off, accepting-new-clients
  toggle, and auto-saved consult booking settings (one frequency cap,
  minimum notice, buffers, slot step) — plus a "My Current
  Availability" panel that shows the provider exactly what clients
  can book, computed the same way the booking page computes it.
- **My Consults** (providers). Each provider sees their own upcoming /
  past / cancelled consults, full details on click, and can mark a
  past consult as no-show. The practice admin sees everyone's, with a
  provider filter.
- **Consult Admin** (admin only). Oversight console: every provider's
  effective availability with edit-on-behalf, all email templates and
  booking rules (writing to the booking workbook's Settings tab — no
  redeploys for wording changes), and an Admin Tools view (practice
  snapshot, privacy/retention panel, audit trail, CSV/PDF exports —
  manage tokens are never exported).

Backing stores: a **Provider Roster** workbook (the practice's source
of truth for who its clinicians are), a **Booking workbook**
(providers mirror, availability, appointments, settings, time off,
audit log), and a small **Manage Availability submissions** sheet.
Reference implementation: Google Apps Script throughout. No
third-party booking service, no analytics, no trackers.

## Handing this to your agent (for the colleague receiving this kit)

This kit is **platform-neutral** plain Markdown (the open Agent
Skills format) and works with any capable AI agent — skill-loading,
coding-workspace, or chat-only with the files uploaded. `README.md`
has the per-platform routes; `PROMPT.md` has a copy-paste starter
prompt. Either way:

1. Confirm the HIPAA prerequisites above (including the
   provider-calendar policy decision). If they aren't met, do that
   first.
2. Answer the setup interview below — the agent should ask once,
   before building.
3. Let the agent build and test, run `references/test-checklist.md`
   with test bookings on a test provider, complete provider
   onboarding (calendar connections + availability), and only then
   swap the public links.

Keep the old booking links (per-provider scheduler links, if any)
live as a fallback until the checklist passes end to end — the usual
cutover is: individual provider links → the single practice booking
page.

## Setup interview (collect once, write down, never guess)

- **Prerequisites:** Workspace domain; the practice account that will
  own everything; BAA signed (date); 2-Step Verification enforced;
  the provider-calendar policy decision (Workspace-only calendars, or
  personal calendars accepted + documented).
- **Practice:** practice name, contact email, notification email,
  client-email sender (address or send-as alias + display name),
  website + privacy-policy URLs, the portal/website pages where
  provider apps will be embedded or linked.
- **Roster data (the routing engine's fuel — exact, per provider):**
  provider ID (short code, e.g. P001-style — your own scheme, never
  reused after someone leaves), name, credentials, work email;
  licensed states; contracted panels/EAPs/funds in client-facing
  names, **state-suffixed where a panel only applies in one state**
  (a panel listed for TX must not make the provider appear for that
  panel in FL); languages; ages served; client types
  (individual/couples/family); gender (for client gender-preference
  matching); sliding scale yes/no; whether they serve clients located
  outside the U.S.; bio links; accepting-new-clients status.
  **Never guess a panel, a state, or a rate-adjacent fact.** A
  provider with no verified data is simply not routed to.
- **Owner-defined routing rules** beyond the roster facts, if any
  (e.g. "Provider X does not take Lyra referrals," "Provider Y is
  never matched for sex-therapy inquiries"). These live in the
  booking workbook's RoutingRules tab, not in code.
- **Booking rules (defaults — confirm or change):** free consult,
  15 minutes; booking window 14 days; minimum notice 12 hours;
  slot grid every 30 minutes; buffer 10 minutes; reschedule/cancel
  cutoffs 4 hours; reminder 24h before; client follow-up 5 minutes
  after the consult ends (survey/next-steps link); provider follow-up
  likewise (with any providers the admin wants excluded, e.g. the
  owner); one active consult per client email/phone.
- **Email wording:** confirmation, reminder, follow-up templates for
  clients (tokens `{ClientFirstName}`, `{EventDateTime}`,
  `{ProviderName}`) and provider reminder/follow-up templates; the
  survey/next-steps URLs; per-language sets if bilingual.
- **Languages:** English only, or bilingual? The reference system
  supports one additional full language (same question set translated,
  provider names in that language from the roster, all client emails
  in the language the client booked in). Add it only if the practice
  actually serves clients in it.
- **Branding:** the practice website's flat look for the public page
  (fonts, ink color, accent color); provider apps use the practice's
  internal portal style. No Google branding, no native dialogs,
  anywhere.
- **Privacy notice:** the booking-form privacy wording clients must
  acknowledge; every booking stores timestamp + notice version. Bump
  the version whenever the wording changes.

## Build order (do not reorder)

1. **Roster + Booking workbook + Booking app** (the app's setup
   functions seed the workbook from the roster) —
   `references/booking-app-spec.md`, `references/setup-and-deploy.md`.
2. **Connect Your Calendar** — it needs the Booking app's `/exec` URL
   baked into its code —
   `references/connect-your-calendar-spec.md`.
3. **Manage Availability, My Consults, Consult Admin** against the
   same stores — `references/provider-apps-spec.md`,
   `references/consult-admin-spec.md`.
4. **Provider onboarding:** each provider connects a calendar and
   submits consult hours; run the booking app's `checkSetup()` until
   every provider reports writer access, free/busy OK, ≥1 hours
   block.
5. **Test** (`references/test-checklist.md`), then **cut over** the
   public links to the single booking page.

## Hard rules for the agent (the expensive lessons)

- **Scopes:** full `https://www.googleapis.com/auth/spreadsheets`
  whenever code calls `SpreadsheetApp.openById` (readonly throws).
  Apps that send mail via **both** GmailApp and MailApp declare
  **both** `gmail.send` and `script.send_mail` — `gmail.send` alone
  leaves every MailApp call throwing into a try/catch, and mail
  silently never sends. Send-as aliases via GmailApp also need
  `gmail.settings.basic`. Calendar features need the Calendar
  Advanced Service (v3) in the manifest. The Connect app is the one
  exception-shaped project: it deploys as **User accessing**, with
  `calendar`, `script.external_request`, and `userinfo.email` — and
  those scopes must also be declared on its GCP project's OAuth
  consent screen (Data Access), or verification tooling will wrongly
  report that no verification is needed.
- **Deployments:** after first deploy, always bump the **existing**
  deployment to a New version. Never mint a new deployment — a new
  URL breaks every embed, and the old URL keeps serving old code.
  Verify from served content, not from the push; deployment lists can
  lag a few seconds behind a bump.
- **Bake production config into source.** Live values (workbook IDs,
  the Booking app URL inside the Connect app) live in the local
  source of truth. A redeploy from a template with placeholder config
  silently breaks a working system — this exact failure has happened.
- **Triggers don't travel with pasted code.** Run each project's
  trigger setup after a fresh setup and verify the triggers exist.
- **Client/server argument shapes must match exactly,** and test
  harnesses must call server functions in the client's exact shapes.
  Two production apps once rejected every correct PIN because the
  client sent one object and the server expected two scalars.
- **The fleet PIN scheme (all provider apps share it):** one 4-digit
  PIN per provider; stored in the Roster only as a SHA-256 hash of
  `ProviderID:PIN` (Roster column AG) with a random session token in
  AH; 5 wrong tries → 15-minute lockout; when pruning lockout state,
  never delete still-counting entries (lock timestamp 0) or the
  lockout can never accumulate. The admin resets a PIN by clearing
  the provider's AG/AH cells. Every server function re-verifies the
  token server-side.
- **Numbers:** map `null`/`undefined`/`''` to NaN before `Number()` —
  `Number(null)` is 0 and silently overwrites unset settings.
- **No native dialogs** (`alert`/`confirm`/`prompt`) — in-page
  confirmation cards, in every language the app serves.
- **Never hardcode** roster facts (states, panels, languages) into
  pages or code. Payment options and eligibility are generated from
  the Providers tab on every load: adding a provider is a roster row
  + a sync, not a deploy.
- **PHI minimization is baseline:** generic calendar titles,
  call-minimum event descriptions, no client attendee, triage-minimum
  practice notifications, no client name in email subjects, goals
  brief capped at 600 chars with an on-form warning, generic client
  errors (raw errors only in execution logs), hashed + expiring +
  rotating manage tokens, retention sweep, append-only AuditLog of
  IDs/times only. See `references/security-and-hipaa.md`.
- **Consult hours ≠ therapy hours.** Nothing in this system changes
  ongoing therapy scheduling; that stays in the EHR, by hand.
- **No waitlist.** No fit or no slot → direct the client to the
  practice contact email (and to name their preferred clinician).
- **Verify from the artifact:** read sheets back after writes, read
  served code after deploys, run the harness after changes, and
  report failures as failures with the actual state.

## Instructions for the agent building this (any platform)

- Read this file and every reference before writing code. Where a
  reference and the admin's live instruction conflict, the admin's
  instruction wins and the change gets written down.
- Your deliverable is paste-ready project files (`Code.gs`, HTML
  files, `appsscript.json` per project) plus verified steps. If you
  have direct, admin-approved access to the practice's Google account
  or an Apps Script deploy path, you may deploy — verifying from the
  served result. If not (most chat agents), hand over the files and
  walk the admin through setup click by click; the Google sign-ins,
  scope authorizations, and deploy actions belong to the practice
  account holder. Say plainly which mode you're in.
- Everything here is Apps Script + Sheets + Calendar + Gmail plus
  Markdown. Platform conveniences are fine to use but the build must
  not depend on any vendor-specific feature — the same kit must work
  for the next practice on a different agent.
