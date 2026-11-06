# Architecture

## Components

| Piece | Type | Audience | Writes? |
|---|---|---|---|
| Directory sheet | Google Sheet, one tab | Admin (edit); apps (read/write) | — |
| Directory app | Apps Script web app, Execute as owner, Anyone | Public | No — read-only |
| Internal add form | Apps Script web app, Execute as owner, Anyone (URL shared internally) | The practice's own clinicians | Yes — one row per submission |
| Public add form (optional) | Apps Script web app, Execute as owner, Anyone | Community colleagues | Yes — same sheet |

All three projects and the sheet live in **one practice Google account** (the admin account). The apps run as that account, so submitters and visitors need no Google sign-in and no permissions on the sheet — the sheet itself is shared with **nobody**.

## Data flow

```
clinician ──▶ internal form ──┐
                              ├──▶ SHEET ──▶ directory app ──▶ public page
community ──▶ public form ────┘        │
                                       └──▶ admin email per submission (review point)
admin edits sheet directly ────────────┘  (corrections, removals, priority)
```

- **Reads:** the directory calls the sheet on every page load (`getDataRange`, header-name column matching) and renders client-side. A sheet edit is visible on the next reload — there is deliberately no cache or sync, so there is nothing to drift.
- **Writes:** a form submission validates server-side, checks for a duplicate name, inserts the row at the end of its service-type section, then emails the admin. Email failure is caught and logged; the submission still succeeds.
- **Curation:** the admin works in the sheet itself — edit a field, delete a row, set a priority. No admin app is needed at this scale; build one only if the network outgrows direct sheet editing (hundreds of entries, multiple curators).

## Why it's shaped this way

- **One sheet, three thin apps** keeps the system understandable by the next agent (or human) who inherits it. Each project is small enough to read in one sitting.
- **Two forms, one destination** separates trust levels without duplicating logic: internal contributors are the practice's own clinicians; public submitters are self-recommendations the admin reviews via the notification email.
- **Public directory, private sheet.** The directory app is the only public surface, and it exposes exactly the columns the cards render — the sheet is never shared or linked publicly.
- **Embed-friendly.** The apps set `XFrameOptionsMode.ALLOWALL` so they can be embedded in the practice website (Google Sites or any page that iframes), which is where clients and colleagues actually look.
