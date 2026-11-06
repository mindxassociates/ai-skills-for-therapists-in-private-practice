# Starter prompt — copy, paste, send to your AI agent

Use this with any AI agent (skill-based, coding-workspace, or
chat-only). If your agent doesn't load skill folders automatically,
upload or include all of this kit's files first (`SKILL.md`, this
file, and everything in `references/`), then paste the prompt below.

---

Build my solo-practice initial-consultation booking system using the
Solo Consult Booking Kit I've given you.

Work in this order, and don't skip steps:

1. Read `SKILL.md` in full, then every file in `references/`, before
   writing any code.
2. First confirm the HIPAA prerequisite at the top of `SKILL.md` with
   me: Google Workspace on my own domain, the Google BAA signed, and
   everything living in that one account. If any of that is missing,
   help me fix it first — do not build around it.
3. Ask me the kit's setup interview, all at once, and write my answers
   down. Never guess my licensed states, insurance panels, fees,
   hours, or email wording.
4. Build the two Apps Script apps (public Booking app + private Owner
   Console) to the specs in `references/`, as files I can paste into
   Google Apps Script (`Code.gs`, `Index.html`, `Manage.html`,
   `appsscript.json` per project). Follow the kit's hard rules —
   especially: full spreadsheets scope, both email scopes if you call
   both mail APIs, no hardcoded panels/fees, generic calendar event
   titles, hashed manage tokens, and no native browser dialogs.
   Note there is intentionally NO separate calendar-connection app —
   I'm a solo owner, so my calendar needs no connecting.
5. Test what you build with a local harness that calls server
   functions in the exact shapes the client sends, then give me the
   deploy steps from `references/setup-and-deploy.md` and walk me
   through `references/test-checklist.md` with test bookings. The
   Google sign-in, authorization, and deploy clicks are mine — tell
   me exactly what to click and what result to expect at each step.
6. Don't swap my public links or declare us live until the test
   checklist passes end to end. Report failures as failures, with the
   actual state — never report a step as done because you started it.

Start by confirming you've read the kit and asking me the setup
interview.

---
