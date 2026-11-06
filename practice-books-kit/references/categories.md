# Chart of Accounts — Therapy Private Practice

The P&L workbook uses exactly these categories, in exactly this order.
Revenue occupies rows 2–12 of each year tab, expenses rows 13–24. Keep the
names verbatim — the Practice Books app's finances reader and the monthly
fill both key off this layout (see `pl-sheet-spec.md`).

## Revenue (rows 2–12)

| Row | Category |
|-----|----------|
| 2 | Stripe Payout |
| 3 | Ivy Pay |
| 4 | Headway Payout |
| 5 | Lyra Health Payout |
| 6 | CuraLinc Healthcare Payout |
| 7 | Supervision via Zelle |
| 8 | Mobile Check Deposits |
| 9 | EFT from Insurance |
| 10 | Affiliate Marketing (PESI, Appsumo) |
| 11 | Referral Bonuses (Alma, Headway) |
| 12 | Other Income (Interest, Gumroad) |

## Expenses (rows 13–24)

| Row | Category |
|-----|----------|
| 13 | Advertising |
| 14 | Meals |
| 15 | Business Travel |
| 16 | Insurance Payments |
| 17 | Office Expenses |
| 18 | Education/CEUs |
| 19 | Supplies |
| 20 | Utilities |
| 21 | Depreciable Assets |
| 22 | Licenses |
| 23 | Contractor Expenses |
| 24 | Other Expenses |

## Classification guide

Apply these rules to statement descriptions. Where a description is
ambiguous, flag it in the monthly report instead of guessing.

**Revenue**

- A payout from a named platform/payer goes to that platform's row:
  Stripe → Stripe Payout; Ivy (Ivy Pay / Ivy Labs) → Ivy Pay; Headway →
  Headway Payout; Lyra Health → Lyra Health Payout; CuraLinc → CuraLinc
  Healthcare Payout.
- Direct insurance claim payments that arrive as EFT/ACH from a payer
  (e.g., BCBS, UHC/Optum claim payments) → **EFT from Insurance**. If the
  practice later contracts a payer heavily enough to want its own row,
  that's a new-category decision for the owner (see "Changing the chart"
  below).
- Supervision fees received by Zelle (or a similar person-to-person rail)
  → **Supervision via Zelle**. These usually do **not** appear in bank
  exports if the receiving account differs from the business checking —
  sweep the owner's payment alerts (see SKILL.md Part A, step 2).
- Paper checks deposited by phone → Mobile Check Deposits.
- Affiliate commissions (continuing-education affiliates, marketplace
  payouts) → Affiliate Marketing.
- Referral bonuses from platforms (e.g., Alma, Headway referral credits
  paid in cash) → Referral Bonuses. Note: these are sometimes tracked by
  the owner from a source outside the statements; if the statements show
  none, leave the cell empty rather than inventing a figure.
- Bank interest, digital-product sales (e.g., Gumroad), and anything
  genuinely unclassifiable-but-business → Other Income.

**Expenses**

- Psychology Today (and similar directory) profile fees → **Advertising**.
- EHR/practice software subscriptions (e.g., Sessions Health,
  SimplePractice), Google Workspace, e-fax services, password manager,
  corporate filing/registered-agent services, practice phone/internet
  tools → **Office Expenses**.
- Restaurants, coffee, and food with a business purpose → **Meals**.
- Fuel, parking, tolls, mileage-related purchases, rides to business
  sites → **Business Travel**.
- Malpractice and business insurance premiums → **Insurance Payments**.
- CE courses, trainings, conference registration, professional books →
  **Education/CEUs**.
- State license applications and renewals, license verification fees →
  **Licenses**.
- Office consumables and small supplies → **Supplies**.
- Office utilities (internet, phone, electric for a physical office) →
  **Utilities**.
- Durable equipment with a useful life over a year (session camera,
  computer, furniture) → **Depreciable Assets**.
- ACH payments to contractors out of the payroll account (the monthly
  payout run) → **Contractor Expenses**. Use the payroll-account
  statement, and exclude any transfers from that account to the owner
  (draws) or to other practice accounts (internal).
- Anything business that fits nowhere else → **Other Expenses**, with a
  note in the monthly report so the owner can reclassify or approve a
  new category.

**Never categorized (excluded before classification)**

- Transfers between the practice's own accounts.
- Transfers to the owner's personal/wealth accounts (owner's draws).
- Credit-card payments (the purchases are the expenses).
- Personal transactions that happen to land on a business statement —
  excluded and listed in the report.

**Reimbursements**

If someone repays the practice for a specific fronted cost — the classic
case is a contractor repaying their seat on the group EHR subscription —
**net the repayment against that expense category** (e.g., Office
Expenses) in the month received. Never book it as income.

## Changing the chart

This chart is a starting template that has proven workable for a
multi-provider therapy practice. Rules for changing it:

- Keep names and order stable month to month; comparability across
  months is the point of a fixed chart.
- Add a row only with the owner's explicit approval. Insert it inside
  the revenue block (rows 2–12) or expense block (rows 13–24), **before**
  the totals rows, and shift everything below it down — then update the
  totals formulas and this file in the same change.
- If the Practice Books app is in use, its finances reader locates the
  totals by label, so inserted rows are safe as long as the totals rows
  keep their exact labels.
