# Data model — the directory sheet

One workbook, one tab. The tab name is configuration (default `Sheet1`); the **header row is the contract** — the directory matches columns by header name, case-insensitively, and accepts the alternate spellings noted below.

## Core columns (in this order, as written by the add forms)

| # | Header | Written by form | Notes |
|---|---|---|---|
| A | `Service Type` | radio choice | One of the configured service types (default `Psychotherapy`, `Psychiatry`). Defines the sheet's sections and the directory's type filter. |
| B | `Provider Name` | text | The duplicate-guard key: unique across the sheet, compared case-insensitively, trimmed. |
| C | `Credentials` | text | e.g. `LCSW`, `LMFT`, `MD, PMHNP`. Free text, displayed as entered. |
| D | `States` | text | Locations licensed/practicing in, as entered (e.g. `TX, FL, NY`). Also accepts header aliases `Location`, `Region`, `Country` in the reader — the directory is not US-only; display values verbatim. |
| E | `Services Offered` | checkboxes, joined | e.g. `Individual Therapy, Couples Therapy`. Powers the service filter; keep the checkbox vocabulary small and consistent. |
| F | `Website` | URL | The card's outbound link. Reader also accepts the misspelling `Webiste` — sheets in the wild contain it. |
| G | `Profile Pic` | URL | Public image URL. Reader also accepts `Profile Picture`, `Photo`. |
| H | `Languages` | text | e.g. `English, Mandarin`. Also accepts `Languages Spoken`. Drives the optional language view (below). |

## Optional columns (reader picks them up if present)

| Header | Effect |
|---|---|
| `Chinese Name` (or the name-column header for your second language) | Display name in the second-language view; falls back to `Provider Name`. |
| `Sliding Scale` | Shown on the card when non-blank. |
| `Priority Level` (or `Priority`) | Display ordering: directory sorts ascending by priority (blanks last), sheet order preserved within a level. Use sparingly — admin-curated featuring, not a ranking of quality. |

## Sheet conventions

- **Row 1 is headers; row 2+ are providers.** Blank-name rows are skipped by the reader.
- **Sections:** rows are grouped by `Service Type` — all rows of one type together. The forms maintain this on insert; the admin maintains it when editing by hand (or just re-sorts when it gets messy — the reader doesn't depend on grouping, only the humans do).
- **No extra tabs of consequence, no formulas in the core columns.** If the admin wants a private notes tab (e.g. "how we know them"), put it in a **separate tab** and understand the boundary: the directory only reads the directory tab, but the workbook is one file — share it with nobody (see `security-and-privacy.md`).
- **Seeding:** launch with 3–5 real, consented colleagues per service type so first visitors see a working directory, not a form letter.

## Curation workflow (admin, in the sheet)

- New submission → admin email arrives → glance at the entry in the sheet → fix typos, confirm the website and photo load, confirm the colleague knows they're listed.
- Wrong or stale entry → edit or delete the row. The directory reflects it on next load.
- Colleague asks to be removed → delete the row, confirm to them. No tombstones, no archive tab needed.
