# Scaling and performance — how this stays fast with many providers

Sheets-based systems rarely die from one big problem. They die from five small ones, repeated on every click. This reference is the kit's defence, in the order that matters.

## 1. Shard by practice (the structural fix)

One installation per practice — see architecture.md. Google quotas (executions, simultaneous runs, fetch/email volumes) and the 10-million-cell workbook ceiling then apply **per practice**, so provider #500 nationally adds zero load to provider #1. Any design that centralises practices reintroduces every problem below at once.

## 2. Keep the index skinny, content in Drive

- Practical slowdown for whole-tab reads begins around **50k–100k rows**. A solo practice writes roughly 1,000 note rows + 1,000 appointment rows a year — decades of index headroom. A 10-provider group writes ~20k rows/year — comfortable for years **if** reads stay narrow, and the archive rule below extends it indefinitely.
- Fat cells are as bad as many rows. Note text, intake prose and documents are Drive files (architecture/data-model). An index row should be well under a kilobyte.

## 3. Archive by year

- Housekeeping offers (and at the practice's chosen month, performs with admin confirmation) a yearly rollover: appointment and note-index rows for closed years are copied to an `Archive_<year>` workbook, verified by row count + hash sample, then removed from the live workbook.
- Archived data stays reachable: the chart's history view reads the archive **on demand, per client**, never as part of a normal screen load.
- Clients discharged beyond the retention window archive the same way, Drive files included, per the practice's retention policy.

## 4. Read narrow, load lazy, paginate

- Boot = instant static shell + **one** call for the Today view (today's appointments for the signed-in provider, unsigned drafts count, unpaid count). Nothing else loads until its tab is opened.
- Every list is paginated (25–50 rows) and filtered server-side by provider, status and date window. "All clients, all notes, all invoices, ever" is never a payload.
- Search runs server-side against the index (ID maps / TextFinder on the name columns), returning matches only.

## 5. Batch and cache — the code rules

- One workbook handle per execution (memoise `openById`); the classic defect is re-opening the same workbook a dozen times inside one call.
- One `getValues()` per tab per call, on the narrowest range that works; filter in memory. Writes in one `setValues()`/`appendRows` batch — never per-cell `setValue()` loops.
- **No formulas over data tabs** — no `QUERY`, `ARRAYFORMULA`, or volatile functions recalculating over thousands of rows on every edit. Compute in script, store values.
- CacheService for static data: templates, fee schedule, provider list, settings. Short TTL (e.g. 10 minutes) with the trade-off stated: a Settings edit may take up to the TTL to appear everywhere.
- Housekeeping (schema ensures, folder checks, session pruning, archive checks) runs on the nightly trigger — never inside the request path.
- Transport discipline: coerce dates to text and numbers through a clean-number path before any payload returns to a view (one `Date`/`NaN` nulls the whole response).

## 6. Write contention

- Providers write to their own clients' rows; notes and audit rows are append-only. Contention is therefore rare by construction.
- A script lock guards only the short critical sections: ID generation and invoice numbering. Never hold a lock across a Drive or Calendar call.

## Thresholds — when to graduate

Stay on this kit while, per practice: active index rows (current year + active clients) stay under ~50k, daily active providers under ~15, and screen loads stay within the practice's patience on the live click-test. Past that, use the repository layer (architecture.md) to move the index behind a real database — the portal, templates and workflows carry over. Treat graduation as a planned migration with full export, not an emergency rescue.
