---
name: apps-script-build-checklist-kit
description: A pre-deploy build checklist for Google Apps Script web apps, built from recurring real-world defects. Use when building or reviewing an Apps Script web app and you want to avoid the expensive repeat mistakes — manifest scopes that silently break mail or spreadsheet access (including the MailApp send_mail trap), top-level variables colliding with browser globals like `history`, PIN-gate argument-shape and hash mismatches, forms that lose work on partial save, records joined by display name instead of a stable ID, buttons with no busy feedback or no restore on failure, missing triggers after a paste or migration, HtmlService doGet failures, and spreadsheet timezone shifts on timestamps.
---

# Apps Script Build Checklist Kit — Ship It Without the Repeat Defects

Run this checklist **before** every deploy of a new or changed Apps
Script web app, and grep the finished source for the failure strings
named here. Every item below is a defect that has actually shipped
and cost real debugging time; the fix is cheap at build time and
expensive in production. Where a rule mentions your own practice's
values (a header, a palette, an ID scheme), the checklist tells you
what to decide — it never supplies someone else's values.

## 1. Declare every scope — twice

- Give `appsscript.json` the **full**
  `https://www.googleapis.com/auth/spreadsheets` scope whenever the
  code calls `SpreadsheetApp.openById`. The readonly scope makes every
  such call throw.
- **The MailApp trap:** when an app sends mail through `MailApp`,
  declare `https://www.googleapis.com/auth/script.send_mail` in the
  manifest. `gmail.send` covers `GmailApp` **only** — it does not
  cover MailApp. Missing `script.send_mail` means every MailApp call
  throws, and try/catch email blocks swallow the failure into a log
  line, so submissions appear to succeed while **no email is ever
  sent**. If the app uses both mail APIs, declare both scopes,
  always.
- Declare `gmail.settings.basic` as well when the app sends from a
  send-as alias through GmailApp. Without it the alias attempt throws
  and mail falls back to the bare account address with no display
  name.
- List every scope the app uses on the Cloud project's OAuth consent
  screen under Data Access, matching the manifest exactly. The
  verification tooling reads the console-declared scopes, so an app
  with none declared there wrongly reads as needing no verification.

## 2. Never declare a window-global name at the top level

- Never name a top-level variable, `let`/`const`, or function
  `history`, `location`, `document`, `window`, `name`, `status`,
  `event`, `origin`, `top`, `parent`, `self`, `length`, or any other
  browser window global — and be wary of shadowing callable built-ins
  (`open`, `close`, `print`, …).
- Why this is critical: `window.history` and its kin are unforgeable.
  A top-level `var history = [...]` silently does **not** create your
  variable; later uses throw; and a throw at the top of a `<script>`
  block kills the **rest of that block** — including the sign-in gate
  or picker init below it — leaving a form dead with no error shown.
  Name step-tracking arrays something like `stepHistory` instead.
- Before deploy, scan every staged HTML file for these collisions —
  with an AST-based scanner if you have one, otherwise by grepping
  top-level declarations against the global list above — and fix every
  critical hit. Also flag uses like `history.<member>` that are not
  real History API members.
- A served-HTML string check is **not** verification for an
  interactive app. After deploying a gate or picker change,
  click-test it in a real browser (field enables, list opens, typing
  filters, selection lands) before calling the deploy done. Some
  browser behaviors — native drag interference is another example —
  simply do not reproduce in simulated DOM test environments.

## 3. Keep the branding white-labeled

- Never call `alert`, `confirm`, or `prompt` in a white-labeled web
  app. The browser stamps the native dialog with the hosting origin,
  which breaks the branded experience and confuses users. Build
  confirmations as in-page cards with explicit Confirm and Cancel
  buttons, in every language the app serves.
- **Copy your own portal header verbatim from your reference app** —
  pick the one existing app in your fleet whose header is correct,
  and copy its header markup and styles exactly for every new
  staff-facing app. Do not improvise a new header per app; header
  drift is a recurring correction, and "close" is not the standard.
- Choose the palette by audience **before** you style: your public
  pages get your public website's flat style; your internal portal
  pages get your portal style. Never carry portal styling (glass,
  gradients, decorative effects) onto a public page, and check the
  served public page for stray portal-style markers before delivery.

## 4. Bake production config into the source of truth

- Keep production values — API URLs, spreadsheet IDs, deployed
  endpoint URLs — in the local source of truth, and deliver them
  there. A fix delivery that reverts a production value to a
  placeholder ships a broken app.
- Compare a checksum (or a direct diff) of every delivered file
  against the local source before handing a delivery over, so a bad
  copy never reaches the deploy step.

## 5. Plan triggers and project migration

- Triggers do not travel with pasted or pushed code. After any fresh
  project setup or migration, run the setup function that installs
  the time-driven triggers by hand, and verify the triggers exist.
  A system with no sweep sends no reminders and runs no cleanup.
- When retiring an old project, delete its triggers **before**
  deleting the project. A deleted project with live triggers behind
  it can double-fire reminders and emails.

## 6. Keep doGet serving the app

- Never pass a custom name to HtmlService `addMetaTag`. Only
  whitelisted names such as `viewport` are allowed; a custom name
  throws and the whole web app serves an error page.
- Pass `doGet` parameters to the page with
  `HtmlService.createTemplateFromFile` and a small dedicated script
  block that assigns each parameter through `JSON.stringify`.
- Grep the HTML for existing template sequences (`<? ... ?>`) before
  using template evaluation, because evaluation would consume them.
- After any `doGet` change, fetch the served `/exec` page and grep
  for the app's markers; call the deploy done only after that passes.

## 7. Give every button feedback — and restore it on failure

- Show the busy state in the **same instant** as the tap or click,
  before any slow work starts: a visible disabled style plus a busy
  label or spinner. Never start a server call before the busy state
  is on screen — work that starts first leaves the user tapping a
  button that looks dead.
- Restore the button on **both** paths — re-enable it and restore its
  label in a shared cleanup step, not only in the success handler.
  Treat a dropped or timed-out response as a failure for cleanup: a
  button re-enabled only on success stays dead for the rest of the
  session after one dropped response.
- On failure, show a short plain sentence; keep technical detail
  behind a collapsible section with a copy action instead of dumping
  a raw log on the user.
- Test the failure path on purpose — force a dropped or timed-out
  response — and confirm the button is usable again before you call
  the build done.

## 8. Save forms without losing work

- Allow **partial save** on any multi-field form, so a person can
  save what they have and return later without losing it.
- Make **blank fields preserve** the values already on file instead
  of overwriting them with empty values.
- Scope each save to the fields it owns, so a generic save never
  overwrites an unrelated field maintained elsewhere.
- Use **one definition of "complete"** that the form, the background
  completeness check, and any admin notification all share — and
  include required documents in that definition when the form asks
  for them. Definitions that disagree produce records that look
  complete in one place and incomplete in another.
- Notify an admin by email only on a **meaningful state change**
  (for example a new document arriving, or a record becoming
  complete) — never on every save. Text-only partial saves stay
  silent.
- After a deploy, tell anyone mid-form to close and reopen the tab
  before continuing: a stale tab runs the old code and can lose new
  work.
- Test the save path with a partial fill, a blank-field refill, and a
  document-only save, reading the spreadsheet back after each one.

## 9. Join records by stable ID, never by display name

- Give every person/record a stable ID in your source-of-truth sheet,
  pass that ID through every call between apps, and store it on every
  record the apps share.
- Never join two records on a display name or a first name. The same
  person legitimately appears under a short form of their name in one
  app and their full name in another, and a name join silently fails
  to match their records.
- Treat a display name as a label for people to read; treat the ID as
  the only key code may match on.
- Add a **tripwire test**: create or list a record whose display name
  differs from the source-of-truth name, and read the joined record
  back before you call the build done.
- When an existing app already joins on names, change the join to the
  ID and add the tripwire test **before** the next deploy, not after
  the next mismatch.

## 10. Verify the way production will — argument shapes and PIN gates

- Make every server function accept the **exact argument shape the
  shipped client sends**, or normalize both shapes on the server.
  The classic failure: the client sends one object
  (`{id, pin}`) while the server declares two scalars — every correct
  credential is then rejected. Tests miss it because the harness calls
  the server in the shape the signature suggests, not the shape the
  client sends.
- Drive every harness call through the client's exact call shape.
  A harness that matches production shapes catches real defects; one
  that matches signatures catches none of these.
- Map `null`, `undefined`, and `''` to NaN **before** calling
  `Number()` in clean/normalize functions. `Number(null)` is 0, so an
  unset optional numeric field silently overwrites a kept value
  with 0.
- **PIN-gate contracts:** if PINs are stored hashed, the check must
  hash the typed PIN in exactly the stored scheme — same algorithm,
  same input format (for example ID + separator + PIN), same
  encoding — and compare hashes. A gate that compares a typed PIN
  directly against a stored hash rejects every correct PIN. Document
  your scheme (algorithm, input format, where the hash and any
  session token live, try limit, and lockout duration) in one place,
  implement the gate and its tests from that document, and include a
  known-answer test: a PIN you set yourself must pass, a wrong one
  must fail and count toward lockout.

## 11. Get spreadsheet timezones right before debugging code

- Apps in this stack often write timestamps as wall-time **strings**,
  and Google Sheets converts datetime-looking strings into Date cells
  using the **workbook's** timezone setting (File → Settings), not
  the script's and not the reader's.
- If a workbook's timezone differs from your practice's timezone,
  every stored instant shifts by the difference: panels that format
  dates for display show times hours off, and real-clock comparisons
  (aging, auto-move deadlines) silently run hours early or late —
  while the app code looks guilty and is not.
- Rule: when you create or adopt any workbook the apps write
  timestamp strings into, set its timezone to your practice's
  timezone first, and verify with a timed probe — write a stamp for
  "now," read it back, and confirm the displayed time matches.

## Pre-deploy sweep (last five minutes)

- [ ] Manifest declares every scope the code uses — full spreadsheets
      scope for `openById`; `script.send_mail` if MailApp is called;
      `gmail.send` if GmailApp is called; `gmail.settings.basic` for
      send-as aliases — and the consent screen's Data Access matches.
- [ ] No top-level declaration collides with a browser global
      (`history` first among them); collision scan run and clean.
- [ ] No native dialogs; confirmations are in-page cards; header
      copied verbatim from your reference app; palette matches the
      audience.
- [ ] Production config values are in the delivered files; delivered
      files diff/checksum-match the local source.
- [ ] Triggers installed in the new project and verified; old
      project's triggers deleted before any retirement.
- [ ] `doGet` serves: served page fetched, app markers present.
- [ ] Every button shows busy instantly and restores on success,
      failure, and dropped response (failure path tested on purpose).
- [ ] Forms: partial save works, blanks preserve, one shared
      definition of complete, notifications only on state change.
- [ ] All cross-app joins use the stable ID; differing-display-name
      tripwire test passes.
- [ ] Harness calls use the client's exact argument shapes; PIN gate
      passes its known-answer test; null-safe number handling in
      place.
- [ ] Every workbook's timezone is set to the practice timezone and
      probe-verified.
- [ ] Users with the app already open have been told to close and
      reopen the tab.

## A note on testing interactive apps

Simulated-DOM test environments do not reproduce every real-browser
behavior (native drag, some focus and dialog behaviors, and the
window-global semantics above are faithful in some simulators and
absent in others). Use harness tests for server logic and argument
contracts — and a real browser, click-testing the actual gate,
picker, and form, for anything a user touches. A green harness plus
an untested UI is not a verified app.
