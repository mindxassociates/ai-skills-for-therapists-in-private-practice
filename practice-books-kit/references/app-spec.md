# Practice Books App — Build Spec

A small, admin-only web app that runs the practice's monthly payroll and
visualizes its finances. Reference implementation: a Google Apps Script
web app backed by two spreadsheets (its own data workbook + the P&L
workbook from `pl-sheet-spec.md`) and deployed at a stable URL the owner
bookmarks or embeds in their portal. Equivalent stacks are fine — keep
the data model, rules, and gates below.

## Access model

- **Admin-only.** The sign-in gate offers only the owner (in a
  roster-based implementation, the owner's provider ID). Every server
  function re-verifies the caller's token + identity server-side —
  client-side hiding is not security.
- Sign-in: a PIN verified server-side (store a hash, never the raw PIN),
  returning a session token the client presents on every call. Add a
  try-limit lockout (e.g., 5 tries → 15-minute lock); when pruning old
  lockout entries, don't delete entries that are still counting (a prune
  condition that removes zero-timestamp entries makes the lockout never
  accumulate).
- Client/server argument shapes must match exactly. If a client sends
  one object, the server must read that object — write the test harness
  to call server functions in the *client's* exact shapes, or this class
  of bug ships silently.

## Data workbook (auto-created on first unlock)

Tabs and columns:

- **Settings** — `Key | Value`. Practice legal name, pay schedule text,
  pay periods per year, default payment method.
- **People** — `Person ID | Name | Type (1099/W-2) | Status | Pay Basis |
  Pay Rate | Email | Work State | Filing Status | Extra Fed WH |
  Backup WH | Tax Form On File | ACH On File | Start Date | End Date |
  Notes | Private Split %`.
  Flags only for tax form / ACH — **never** full SSN, EIN, or bank
  account numbers.
- **Earnings** — `Earning ID | Person ID | Service Date | Source / Payer |
  CPT | Units | Gross Collected | Provider Share | Notes | Client Type`.
  One row per session/earning event in the pay period.
- **Adjustments** — `Adj ID | Person ID | Run ID | Kind | Amount | Notes |
  Created`. Kinds: reimbursement, bonus, deduction, EHR repayment.
  `Run ID` is blank until a pay run absorbs the adjustment.
- **PayRuns** — `Run ID | Period Start | Period End | Pay Date | Status |
  Total Gross | Total Net | Total Employer Tax | Created | Approved |
  Paid | Notes`.
- **PayLines** — one row per person per run: gross, adjustments,
  deductions, withholding columns (Fed / SS / Med / State), net, employer
  tax columns (SS / Med / FUTA / SUTA), YTD gross/net, payment method,
  payment confirmation.
- **TaxTables** — `Key | Value | Notes`. Editable tax parameters:
  Social Security rate + wage base, Medicare rate + additional-Medicare
  threshold, FUTA rate + wage base, SUTA rate + wage base + state,
  standard deductions. Ship with current-year federal defaults and a
  note that the owner/CPA updates them every tax year. If the schema
  grows later, self-heal on boot: add missing columns to existing
  workbooks without disturbing existing data.

## Pay rules

- **Pay Basis** (per person, set by the owner — never guessed):
  - *Percent* — the person is paid Pay Rate % of gross collected.
  - *Flat* — Pay Rate dollars per session/unit, regardless of gross.
  - *Hourly* — Pay Rate × hours/units.
  - *Salary* (W-2) — Pay Rate per pay period.
- **Client Type** (per earning): Insurance / EAP / Private Pay / Sliding
  Scale.
  - Insurance and EAP earnings use the person's Pay Basis.
  - Private Pay and Sliding Scale earnings use the person's **Private
    Split %** of the amount collected, *when a split is set*; if no
    split is set, fall back to the Pay Basis. (This supports the common
    arrangement where a flat insurance rate doesn't apply to a
    clinician's own private-pay fee schedule, which is split instead.)
- Provider Share is computed when the earning is recorded and recomputed
  server-side whenever a line is edited — never trust a client-supplied
  share.
- **W-2 withholding:** FICA computed exactly with the TaxTables wage-base
  caps (stop Social Security at the base, year-to-date aware); federal
  withholding by the annualized percentage method using the editable
  standard deductions — an **estimate**, labeled as such everywhere it
  appears. Employer taxes (employer FICA, FUTA, SUTA) are costed on the
  pay line but never deducted from the employee.
- **1099 readiness:** flag any contractor whose calendar-year total
  reaches the 1099-NEC threshold ($600) and anyone missing the Tax Form
  On File or ACH On File flags.

## Pay run lifecycle

Runs follow the practice's pay convention (default: **paid on the 1st
for the prior month**; the create-run form defaults to the prior month's
1st–last days with pay date the 1st).

`Draft → Approved → Paid → Locked`

- **Draft:** lines are built from the period's Earnings + all unabsorbed
  Adjustments; the owner can edit lines (server recomputes net).
- **Approved:** required intermediate state — a run cannot jump from
  Draft to Paid. This is the owner's review checkpoint.
- **Paid:** marking a run Paid (a) stamps the absorbed adjustments with
  the Run ID, (b) writes **one row per person** to the separate **Payout
  History workbook** with columns `Date | Name | Email | Amount |
  Provider ID` (this workbook feeds any provider-facing payout view and
  the P&L reconciliation), and (c) emails the owner a run summary
  (period, per-person net, totals). The app does **not** move money —
  the owner pays from the bank and can record confirmations per line.
- **Locked:** closed for edits; corrections go in the next run as
  adjustments.

Supporting views/exports: printable pay stubs per line; a year-to-date
pay register; quarterly net totals; CSV exports of the register, a
1099-NEC summary (with the ≥$600 and missing-flag callouts), and a W-2
summary.

## Finances tab (read-only P&L visualization)

The app reads the P&L workbook (`pl-sheet-spec.md`) and **never writes
to it**.

Reader contract:

- Identify the workbook by an ID stored in the app's configuration (set
  at build/setup time).
- Year tabs are the tabs whose names match a 4-digit year; default to
  the latest, with a year switcher.
- Locate the sections by the **exact row labels** `Total Revenue` and
  `Total Expenses` (and the net row by its `Net Income` prefix):
  category rows are the labeled rows between the header and `Total
  Revenue` (revenue) and between `Total Revenue` and `Total Expenses`
  (expenses). Don't hardcode row numbers — inserted categories must not
  break the reader.
- Parse accounting-format values liberally: real numbers pass through;
  strings like `"$ 1,282.90"` → 1282.90, `"$ (29.95)"` → −29.95,
  `"$ -"` / blank → 0. Rows may be short (missing trailing cells) —
  treat missing as 0, and sum months yourself rather than trusting the
  Summary column.
- Chart expenses as positive magnitudes; compute net as revenue −
  expenses per month. A month "has data" if its revenue or expenses are
  nonzero; YTD sums run through the last such month. Also compute the
  **prior year's** monthly totals and its same-period YTD for
  comparisons.

Charts and displays (hand-rolled SVG is fine; keep them dependency-free
and printable):

1. **Stat cards:** revenue YTD; expenses YTD + net margin %; net income
   YTD + average per month + same-period prior-year comparison (delta);
   best month by net.
2. **Revenue vs. expenses** grouped monthly bars with the net as an
   overlaid line/dots.
3. **Net income trend** area/line chart, with the **prior year's monthly
   net overlaid as a dashed line**.
4. **Revenue donut** and **expense donut**: YTD category shares, center
   total, legend with $ and %. Skip zero categories; a single category
   and an all-zero year must still render sanely.
5. **Stacked monthly revenue bars:** top 5 revenue categories + "Other"
   per month, with legend — shows source mix shifting over the year.
6. **Cumulative net income** area chart (running YTD net).
7. **Monthly net-margin bars:** net ÷ revenue % per month, negatives
   visually distinct.
8. **Full P&L table** mirroring the sheet layout (categories × months +
   Summary), expenses shown in accounting parentheses style.
9. All charts re-render from the loaded payload on year switch — no
   extra server calls per chart.

## Performance and robustness lessons

- **Load finances lazily.** Reading a second workbook at unlock makes
  sign-in feel broken. Boot with payroll data only; fetch finances when
  the Finances tab is first opened, with a visible loading state.
- **Guard first-boot workbook creation with a lock.** If the data
  workbook is auto-created when a stored ID is missing, wrap the
  check-and-create in a script lock — otherwise an impatient owner's
  repeated unlock clicks race and create a pile of duplicate workbooks.
- **Busy states on long calls.** Disable the unlock/save buttons and
  show progress ("Unlocking…") until the call returns; restore on
  failure. An unresponsive-looking button invites the repeat clicks
  above.
- A finances read failure must never block payroll: catch it, show a
  "finances unavailable" state in that tab only.

## Deploy gates

1. Local harness tests pass (pay math, lifecycle guards, Paid → Payout
   History write, flags, finances parser) — called in the client's exact
   argument shapes.
2. Push/deploy the code, then **read the deployed content back and
   require a byte-for-byte match** with the tested local files before
   creating a release version. (Skipping this once shipped a stale build
   that looked current.)
3. **Bump existing deployments only** — never create a new deployment
   (new URL) for an update. If several deployments exist, bump them all.
4. After a bump, wait a few seconds and re-list deployments to confirm
   the new version is actually being served; the first list can lag.
   Spot-check the served page for a marker from the new build.
5. Manifest scopes: the app needs full spreadsheet access (opening a
   second workbook by ID fails under a read-only scope) plus send-mail
   for the paid-run summary. Adding a scope later forces the owner to
   re-authorize and can wall the app behind an auth error until they do
   — declare everything needed up front.
6. The owner's one-time authorization (open the project, run any
   function, approve scopes) is manual and expected; until it's done the
   app URL shows an access error.

## Boundaries

Restating SKILL.md because builders forget: the app calculates and
records only — no tax e-filing, no money movement, no full
SSN/EIN/bank numbers (on-file flags only), W-2 figures are estimates for
CPA verification, finances are read-only.
