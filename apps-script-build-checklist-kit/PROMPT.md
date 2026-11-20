# Starter prompt — copy, paste, send to your AI agent

Use this with any AI agent (skill-based, coding-workspace, or
chat-only). If your agent doesn't load skill folders automatically,
upload or include all of this kit's files first (`SKILL.md` and this
file), then paste the prompt below. Include your app's files
(`Code.gs`, the HTML files, `appsscript.json`) as well.

---

Build (or review) my Google Apps Script web app using the Apps Script
Build Checklist Kit I've given you.

Work in this order, and don't skip steps:

1. Read `SKILL.md` in full before writing or judging any code.
2. Ask me for my own standards where the checklist needs them, and
   write my answers down — never invent or borrow another practice's
   values:
   - Which of my existing apps is the reference for the portal header
     (copy it verbatim from that app)?
   - The public palette vs. the internal portal palette.
   - My stable record ID: where it lives in my source-of-truth sheet
     and which apps must carry it.
   - My PIN scheme, if the app has a PIN gate: hash algorithm, input
     format, where the hash and session token are stored, try limit,
     lockout duration.
   - My practice's timezone, for the workbook-timezone check.
3. Build or review against every section, in particular:
   - Manifest scopes: full spreadsheets scope for openById; BOTH
     gmail.send and script.send_mail if both mail APIs are called
     (gmail.send alone does not cover MailApp, and the failure is
     silent); gmail.settings.basic for send-as aliases; consent
     screen Data Access matching the manifest.
   - No top-level variable, let/const, or function named after a
     browser window global — history, location, document, window,
     name, status, event, and the rest. Run a collision scan on the
     HTML and fix every critical hit.
   - No native alert/confirm/prompt; in-page confirmation cards.
   - Buttons: busy state in the same instant as the click, restored
     in a shared cleanup step on success, failure, and dropped
     response alike.
   - Forms: partial save allowed, blank fields preserve on-file
     values, saves scoped to the fields they own, one shared
     definition of "complete," admin email only on a meaningful
     state change.
   - Records joined by stable ID only, never by display name, with a
     tripwire test whose display name differs from the sheet name.
   - Server functions accept the exact argument shapes the shipped
     client sends; the harness calls them in those shapes. Null /
     undefined / '' mapped to NaN before Number().
   - PIN gate hashes the typed PIN in exactly the stored scheme,
     with a known-answer test (a PIN I set passes; a wrong one fails
     and counts toward lockout).
   - Triggers installed and verified after setup or migration;
     doGet uses only whitelisted meta tag names; every workbook's
     timezone set to my practice timezone and probe-verified.
4. Finish with the kit's pre-deploy sweep, item by item, and report
   each item as pass or fail with the evidence (grep results, scan
   output, read-backs). Fix every failure before calling the build
   ready to deploy.
5. Remind me, in your final report, to tell anyone who has the app
   open to close and reopen the tab after the deploy.

Report failures as failures, with the actual state — never report a
check as passed because it usually passes.

Start by confirming you've read the kit and asking me for my
standards in step 2.

---
