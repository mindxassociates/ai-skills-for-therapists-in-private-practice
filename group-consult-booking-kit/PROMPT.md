# Starter prompt — copy, paste, send to your AI agent

Use with any AI agent (skill-based, coding-workspace, or chat-only).
If your agent doesn't load skill folders automatically, upload or
include all of this kit's files first (`SKILL.md`, this file, and
everything in `references/`), then paste the prompt below.

---

Build my group practice's initial-consultation booking system using
the Group Consult Booking Kit I've given you.

Work in this order, and don't skip steps:

1. Read `SKILL.md` in full, then every file in `references/`, before
   writing any code.
2. First confirm the HIPAA prerequisites at the top of `SKILL.md`
   with me: Google Workspace on the practice domain with the BAA
   signed, one practice account owning the central system, and our
   provider-calendar policy decision (Workspace calendars, or
   personal calendars accepted and documented). If any of that is
   missing, help me fix it first — do not build around it.
3. Ask me the kit's setup interview, all at once, and write my
   answers down. Never guess a provider's licensed states, panels,
   languages, or email wording — a provider with unverified roster
   data must simply not be routed to.
4. Build the five Apps Script apps to the specs in `references/` —
   Public Booking, Connect Your Calendar, Manage Availability, My
   Consults, Consult Admin — as paste-ready files per project
   (`Code.gs`, HTML files, `appsscript.json`). Build in the kit's
   order (Booking first; Connect needs the Booking app's URL). Follow
   the hard rules: full spreadsheets scope; both email scopes if you
   call both mail APIs, plus the settings scope for aliases; the
   shared PIN scheme; no hardcoded roster facts; generic calendar
   titles; hashed, expiring manage tokens; no native dialogs.
5. Test with local harnesses that call server functions in the exact
   shapes the clients send. Then give me the deploy and
   provider-onboarding steps from `references/setup-and-deploy.md`
   and walk me through `references/test-checklist.md` with test
   bookings — including `checkSetup()` passing for every provider
   before cutover. The Google sign-ins, authorizations, and deploy
   clicks for the practice account are mine; tell me exactly what to
   click and what to expect.
6. Keep our existing booking links live until the checklist passes
   end to end. Report failures as failures, with the actual state —
   never report a step as done because you started it.

Start by confirming you've read the kit and asking me the setup
interview.

---
