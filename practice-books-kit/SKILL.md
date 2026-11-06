---
name: practice-books-kit
description: Monthly bookkeeping and payroll for a therapy private practice (solo or group). Use when the practice owner wants to (1) turn bank and credit-card statements into a filled monthly profit-and-loss workbook using a fixed chart of accounts, with every transaction classified, internal transfers excluded, and the month tied out to the penny; and/or (2) build and deploy a companion "Practice Books" web app that runs monthly contractor/employee payroll (1099 + W-2 estimates) and shows a read-only visual dashboard of the P&L (charts, trends, category mixes). Reference implementation: Google Sheets + Google Apps Script, but the workflows are written to work with any spreadsheet/app stack the agent can drive.
---

# Practice Books Kit — Bookkeeping + Payroll for a Therapy Private Practice

## Purpose

Give a private-practice owner a complete, repeatable money system with two parts:

- **Part A — Monthly bookkeeping.** Feed the agent the month's bank and card
  statements. The agent classifies every transaction into a fixed chart of
  accounts and fills one month column of a profit-and-loss (P&L) workbook,
  then proves the month ties out before reporting it.
- **Part B — The Practice Books app.** A small admin-only web app the agent
  builds and deploys for the owner: monthly payroll for 1099 contractors and
  W-2 employees (pay runs, stubs, year-end summaries), plus a read-only
  Finances dashboard that visualizes the P&L workbook from Part A.

The two parts reinforce each other: the app's Contractor Expenses can be
reconciled against the P&L, and the dashboard means the owner always sees
current numbers without opening the workbook.

## Handing this to your agent (for the colleague receiving this kit)

Give your AI agent this **entire folder**, then:

1. Answer the setup interview below — the agent should ask you these
   questions once, before doing anything else.
2. Confirm the chart of accounts in `references/categories.md` — keep the
   names and order unless a category truly doesn't apply to your practice;
   the agent should confirm it with you before the first fill.
3. Hand over one month of statements and let the agent do a first fill.
   Review its reconciliation and judgment-call list; correct anything once,
   and the agent records your ruling as a standing rule for future months.

## Setup interview (collect once, write down, reuse every month)

The agent must collect — and never guess — the following before the first
fill or app build:

- **Practice:** legal name, owner name, state(s) of operation, entity type.
- **Accounts** (last 4 digits are enough as labels):
  - Primary business checking (where payer income lands).
  - Payroll subaccount, if the practice uses one to pay contractors.
  - Tax/savings subaccount, if any (transfers to it are internal).
  - Business credit card(s).
  - Owner's personal/wealth accounts that receive transfers (needed to
    recognize owner's draws).
- **Statements:** how the owner will provide them each month (CSV export
  preferred, PDF if that's all the bank offers), and which date column
  governs the month (transaction date, not post date, unless the owner
  rules otherwise).
- **Pay convention:** default is *paid on the 1st of the month for the
  prior month's work*. Confirm or record the practice's actual convention.
- **People and pay terms** (for Part B): every contractor/employee, their
  type (1099 or W-2), and their exact pay terms — percent of collections,
  flat per session, hourly, or salary; any separate private-pay/sliding-scale
  split; any recurring deductions (e.g., an EHR seat fee). **Never guess a
  pay rate.** If a rate is missing, leave it unset and flag it.
- **Off-statement income:** ask explicitly how the practice receives money
  that never touches the bank feed — supervision or rent paid by
  Zelle/Venmo/cash/check, for example. Those payments must be swept in from
  email/payment alerts each month or the P&L will silently understate
  income.

## Part A — Monthly statement-to-P&L workflow

Reference files: `references/categories.md` (chart of accounts +
classification guide) and `references/pl-sheet-spec.md` (workbook layout,
formulas, and the fill procedure). Follow them exactly.

1. **Gather ALL statements for the month.** Primary checking, payroll
   subaccount, every business card, plus the off-statement sweep (step 2).
   If a statement is missing, say so and fill only what the provided
   statements support — name the gap in the report (e.g., "Contractor
   Expenses pending the payroll-account statement") rather than filling
   around it silently.
2. **Sweep for off-feed income.** Search the owner's email/payment alerts
   for the month (Zelle/Venmo "you received money" notices, etc.) and add
   confirmed business receipts to the ledger with their source noted.
   Personal receipts found in the same sweep are excluded and listed.
3. **Parse every transaction** from every statement into one ledger:
   date, source account, description, amount (credits positive, debits
   negative).
4. **Exclude internal money movement — it is neither income nor expense:**
   - Transfers between the practice's own accounts (checking ↔ payroll
     subaccount ↔ tax subaccount).
   - Transfers out to the owner's personal/wealth accounts — these are
     **owner's draws**, never expenses.
   - Credit-card payments (autopay or manual) — the card's *purchases* are
     the expenses; the payment just moves money between accounts.
5. **Classify every remaining transaction** using
   `references/categories.md`. Contractor ACH payments made from the
   payroll account are Contractor Expenses. If a transaction fits no rule,
   put it on the judgment-call list for the report — never drop it
   silently, and never invent a new category without the owner's approval.
6. **Sum by category** into the month's column values (expenses negative).
7. **Write the month column** per `references/pl-sheet-spec.md`: category
   cells only, then the totals formulas, asserting on the write result
   (cell count) before trusting it.
8. **Read back and tie out.** Re-read the written column from the workbook
   and verify against the independently computed ledger:
   - Sum of categorized revenue = total statement credits minus excluded
     items (internal transfers in, card refunds handled per owner's rule).
   - Sum of categorized expenses = total statement debits minus excluded
     items.
   - Every transaction in the ledger is accounted for exactly once:
     categorized, excluded-with-reason, or listed as unclassified.
   If the tie-out fails, fix it before reporting — do not report a month
   that doesn't reconcile.
9. **Report the month** to the owner: revenue, expenses, net; year-to-date
   totals; the judgment calls made (with amounts) and the owner's rulings
   recorded as standing rules; anything unclassified; any missing
   statements. Keep the report factual and complete — the owner audits
   from it.

### Part A hard rules

- **Actuals only.** Use real transaction amounts from statements. Never
  estimate, average, annualize, or plug a number to make a month "look
  complete." An incomplete month is reported as incomplete.
- **Never overwrite a hand-entered cell.** If the owner has already typed
  a value into a cell you are about to write and it differs from yours,
  keep theirs, flag the conflict in the report, and reconcile in the
  open — a pre-existing entry usually comes from a source you don't have.
- **Expenses are negative numbers** in the sheet; totals formulas rely on
  it.
- **Reimbursements net against the expense, never book as income.** When
  someone repays the practice for a specific cost the practice fronted
  (the classic case: a contractor repaying their seat on the group EHR
  subscription), subtract the repayment from that expense category in the
  month received. Grossing it up as income overstates both sides.
- **Personal transactions are excluded and listed** in the report, not
  categorized "to be safe."
- **Apply the owner's rulings consistently.** When the owner corrects a
  classification once, write the rule down (in your memory/notes for this
  practice) and apply it every month after without re-asking.

## Part B — The Practice Books app

Reference file: `references/app-spec.md` — data model, pay rules, run
lifecycle, finances-reader contract, chart list, and deploy gates. Build
to that spec.

Shape of the work:

1. **Confirm setup-interview data** (people + pay terms especially). Build
   nothing financial on a guessed rate.
2. **Build locally first.** Write the server + client code, and a local
   test harness that stubs the spreadsheet layer and calls every server
   function in the exact argument shapes the client sends. Cover at
   minimum: pay-basis math (percent / flat / private split), run lifecycle
   guards (a run must pass through Approved before Paid), the Paid →
   Payout History write, the 1099 $600 flag, W-2 FICA wage-base cap, and
   the finances parser against accounting-format strings.
3. **Deploy with gates.** Push the code, then read the deployed project
   content back and require a byte-for-byte match with the tested local
   files *before* creating a version — a stale-content deploy looks
   identical to a good one until someone opens the app. Bump **existing**
   deployments to the new version; never mint a new deployment URL (every
   new URL is a link someone has to update, and old URLs keep serving old
   code). After bumping, re-list the deployments to confirm the version
   actually moved (deployment lists can lag a few seconds behind a bump).
4. **Owner authorization is a one-time manual step.** The owner opens the
   project once and approves the scopes (spreadsheet + send-mail). Until
   then the app URL will show an access error — that is expected, not a
   bug.
5. **First-run checklist for the owner:** unlock, confirm the data
   workbook was auto-created, sync/add people, set each person's pay
   basis and rate, then create the first (prior-month) pay run as a dry
   run in Draft and review the lines before approving anything.

### App boundaries (state them to the owner up front)

- The app **calculates and records only**. It does not e-file taxes
  (1099/W-2/941), does not move money or make payments, and does not
  submit anything to any agency. The owner pays people from the bank as
  usual; the app records that it happened.
- **W-2 withholding figures are estimates** (annualized percentage method
  from an editable tax-tables tab) for the owner's CPA to verify — never
  present them as filing-ready.
- **No full SSN/EIN or bank account numbers in the app workbook.** Store
  only "tax form on file" / "ACH on file" flags; full identifiers stay in
  the practice's existing secure systems.
- The app is **admin-only**: an owner sign-in gate (e.g., a PIN verified
  server-side against a roster), and every server function re-checks the
  caller's authorization. Providers never see the app; their own payout
  view, if any, is a separate read-only surface.
- The Finances dashboard is **read-only** — the app never writes to the
  P&L workbook. The monthly fill (Part A) stays the single way numbers
  get into the P&L.

## Operating rules for the agent

- Follow the reference files over improvisation; where a reference and a
  live instruction conflict, the owner's current instruction wins and the
  change gets written down.
- Verify from the artifact, not from your own say-so: read back sheets
  after writes, read back deployed code after deploys, and run the
  harness after code changes.
- When a step fails, report what failed, what state things are actually
  in, and what happens next. Never report a fill, a deploy, or a payment
  run as done on the strength of having started it.
