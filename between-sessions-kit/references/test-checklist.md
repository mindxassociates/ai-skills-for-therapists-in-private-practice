# Test checklist

Two gates, both required: the automated harness (fast, every deploy) and the live click-test (slower, every behaviour change). Served-HTML marker checks sit between them — they prove delivery, never behaviour.

## Harness (mock workbook, exact client call shapes)

Run with the practice timezone pinned (`TZ=<practice zone>`); date fixtures are timezone-sensitive and a red suite under UTC proves nothing.

- **Gate:** correct PIN → session; wrong PINs count up; 5th failure locks 15 min; correct PIN while locked still refused; gate payload lists names only (no IDs in labels, no PIN material anywhere).
- **Scoping:** provider B cannot read/edit/delete provider A's client, assignment, or result (standard not-found); bad token refused on every function.
- **Clients:** create (partial data OK, blanks preserve on edit); edit in place changes fields and preserves ClientID + tokens (a link issued before the edit still resolves after); archive → unarchive round-trip; delete cascades with correct counts and leaves other clients' rows untouched; deleted client's token no longer resolves; post-delete engine run sends them nothing.
- **Assignments + window:** each pattern (once / daily / weekly / every-N / custom) × each end rule; creation inside the window writes the capped count in **one bulk write** and reports the true series total; window-walk top-ups are contiguous with unique epochs and stop exactly at the end rule; paused/ended gain nothing from expansion; DST seam: weekly wall time pinned across spring-forward, epoch shifts correctly.
- **Engine + crediting:** due instance sends (right language, right link, alias when present); not-yet-due doesn't; early submission flips the earliest pending instance; submission after send flips the sent one; engine never emails covered work, including a legacy uncredited result (and backfills its link); failure path retries then marks Failed at the attempt cap; adherence reads 100% on fully-done work.
- **Transport legality (the release gate):** every provider-facing payload is recursively free of `Date` objects and non-finite numbers, **with live-shaped fixtures** — Date objects in date-shaped cells, empty score cells, real timestamp serials. Review + summary + detail payloads specifically.
- **Review:** flagged (crisis-note) submission appears in the flagged queue and the dashboard count; mark-reviewed stamps and clears both; detail returns prompt → answer pairs with no raw JSON anywhere.
- **Catalog sweeps:** every item renders through the real payload builder with zero spec-language hallmarks in descriptions + prompts; every chat-routed item carries authored steps; translation completeness (names, descriptions, step prompts, choice options parallel); every category resolves a translation; gentle-note items carry their translated note and the payload carries it.
- **Strings:** EN/second-language key parity across the server table and both embedded HTML tables.
- **Customs:** draft saves and round-trips through the builder data path; draft is not assignable; published appears in the owner's library (and everyone's, if practice-shared) with its description; retired leaves the library; published fork-on-edit keeps the original assignable version intact.
- **Watchdog:** seeded stalled instance (> 3h, Active, uncovered) → exactly one admin email, IDs only; covered / paused / ended / recent / future instances → no alert; heartbeat audit row written on alert *and* clean runs.
- **Backups (mocked Drive):** Sunday gating; copy naming; folder create/reuse; retention keeps exactly the newest 4 and trashes (never hard-deletes) the rest; audit row per run; a Drive failure audits and does not break housekeeping.
- **DOM smoke:** both views boot; null-payload and transport-failure modes render visible in-view errors (never a silent blank); wizard step flow + payload deep-equals the expected shape; delete confirm card flow; language pill switches all chrome and persists per the precedence rules.

## Live click-test (real deployment, throwaway data only)

Use a clearly-labelled test client under the practice's own test address; delete it (cascade) when done and say what the cleanup left behind.

1. **Sign in** as a provider; dashboard counts read zero/sane.
2. **Timezone flow:** create the test client in a different timezone than the practice; assign a weekly item; the wizard sentence names the client's zone; the summary shows zone-labelled times.
3. **Speed proof:** assign a daily no-end item; creation completes in seconds and the result card states the window count **and** the full series total; tap-to-copy puts the full URL (with `?t=`) on the clipboard.
4. **Early submission:** open the client link, complete the item *before* its scheduled time; provider side shows the instance Completed, adherence undiluted, and the result in Review with readable prompt → answer pairs. For a flagged item: it flags, and Mark reviewed clears it in place.
5. **Edit flows:** edit the test client's email + timezone; reopen a pre-edit client link — it still loads. Edit a draft custom exercise and confirm it stays the same draft; publish it, confirm it appears in the assign library, retire it.
6. **Archive/unarchive** the test client without leaving the Clients screen; **delete** it and confirm the row disappears immediately (no tab re-click).
7. **Public surface:** the index page lists the whole catalog; two client pages opened anonymously render in both languages after the pill switch (titles, prompts, choice options), and the choice persists to the next page.
8. **Parity:** every catalog slug's public page returns 200/indexable; no orphan public pages; any retired item 404s on both sides.
