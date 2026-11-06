# P&L Workbook Spec — "Financial Performance Dashboard"

One workbook holds the practice's monthly profit-and-loss history. The
layout is fixed so that both the monthly fill (SKILL.md Part A) and the
Practice Books finances reader can rely on it.

## Layout

- **One tab per year**, named with the 4-digit year (`2026`, `2027`, …).
  An optional extra tab (e.g., "Tax Estimates") may exist; it is not
  part of this spec and neither workflow touches it.
- **Column A** — category labels, exactly as in `categories.md`.
- **Columns B–M** — January through December.
- **Column N** — "Summary" (the year-to-date column).
- **Row 1** — header: A1 blank, B1–M1 month names ("January", …,
  "December"), N1 "Summary".

## Rows

| Rows | Content |
|------|---------|
| 2–12 | Revenue categories, in the order given in `categories.md` |
| 13–24 | Expense categories, in the order given in `categories.md` |
| 25 | **Total Revenue** |
| 26 | **Total Expenses** |
| 27 | **Net Income (taxable earnings)** |

The totals labels are exact: `Total Revenue`, `Total Expenses`, and the
net row's label begins `Net Income`. Other tooling finds these rows by
label, not by number — do not rename them.

## Formulas

For each month column X (B–M), on the year tab:

- `X25` = `=SUM(X2:X12)` — total revenue
- `X26` = `=SUM(X13:X24)` — total expenses (negative, because expense
  cells are negative)
- `X27` = `=SUM(X25:X26)` — net income

For the Summary column, every row r in 2–27:

- `Nr` = `=SUM(B{r}:M{r})`

Sign convention: revenue cells hold positive amounts, expense cells hold
**negative** amounts. That is what makes the three formulas above work
with plain sums.

## Number format

Apply an accounting-style currency format to B2:N27 (currency symbol,
thousands separators, two decimals, negatives in parentheses, zero shown
as a dash). The exact format string is platform-specific; what matters is
that humans read parentheses as negative, and any parser must too.

## Greenfield creation

If the workbook doesn't exist yet:

1. Create a workbook named "Financial Performance Dashboard".
2. Create one tab for the current year (and prior years if the owner
   wants history backfilled from statements).
3. Write row 1 (month names + "Summary") and column A (the 23 category
   labels + the 3 totals labels), in the order above.
4. Write the Summary formulas down column N (rows 2–27).
5. Apply the accounting format to B2:N27.
6. Leave all month cells empty until the first fill — do not pre-fill
   totals formulas for months that have no data yet if the owner's
   existing sheets leave them blank; match the convention in §Fill
   procedure step 3 (write them with the month's data).

## Fill procedure (one month)

Inputs: the classified, summed category values for the month (from
SKILL.md Part A), with expenses already negated.

1. **Check the target column first.** Read the month column. It should
   be empty. Any nonblank cell in the category rows is a hand-entered
   value: preserve it, use it in place of (not in addition to) your
   computed value for that category, and flag the difference in the
   report. If the whole month is already filled, stop and ask — filling
   twice is the classic way to double a month.
2. **Write the category cells only** — rows 2–24 of the month column, in
   one write. Categories with no activity get `0` or blank; match how
   neighboring filled months look (a stored `0` displays as a dash in
   accounting format).
   - If a category's amount is knowingly incomplete because a statement
     is missing (classically Contractor Expenses without the payroll
     account statement), leave that cell **blank** — blank says "not yet
     known", zero says "known to be zero" — and name the gap in the
     report. Fill it when the statement arrives.
3. **Write the totals formulas** for the month column (row 25, 26, 27
   per §Formulas). Do not type computed totals as values — formulas keep
   the sheet self-correcting when a cell is later adjusted.
4. **Assert on the write result.** The write call returns how many cells
   were updated; compare against the number you intended (category cells
   + 3 formula cells). A mismatch means the write didn't land as
   expected — investigate before continuing.
5. **Read back the column** (values, unformatted) and compare cell by
   cell against your computed ledger: every category value, and the
   three computed totals (revenue = your revenue sum, expenses = your
   expense sum, net = revenue + expenses).
6. **Check the Summary column** moved by exactly the month's amounts:
   new YTD revenue = prior YTD + month revenue, and likewise for
   expenses and net. This catches a formula range problem that a
   single-column read-back can miss.
7. Only now is the month "filled." Report per SKILL.md Part A step 9.

## Preservation rules

- Never overwrite a nonblank cell the owner entered by hand. Preserve,
  flag, reconcile (SKILL.md hard rules).
- Never edit prior months as part of a routine fill. Corrections to a
  closed month happen only on the owner's explicit instruction (e.g.,
  netting a reimbursement that was initially misbooked), one cell at a
  time, each verified by read-back, and noted in the report.
- When a category row is inserted (see `categories.md`, "Changing the
  chart"), fix the totals and Summary formulas in the same edit and
  re-verify one filled month end to end.
