---
name: referral-network-kit
description: A referral network for a therapy practice, built on Google Workspace + Apps Script + Sheets. Use when a practice owner wants (1) a public read-only web directory of recommended colleagues (photo cards, search, filters, one-click copy of a provider's details) rendered live from a single spreadsheet; (2) an internal add form their own clinicians use to contribute recommendations; and (3) an optional public add form so community colleagues can add themselves or recommend someone. Duplicate names are rejected, entries stay grouped by service type, and the admin is emailed on every submission. The directory holds professional public information only — never client data.
---

# Referral Network Kit — A Living Referral Directory for a Therapy Practice

## What this system is

Three small Apps Script web apps over **one Google Sheet**:

1. **Directory app** (public, read-only) — renders the sheet as searchable provider cards, live on every page load. No cache, no republishing: edit the sheet and the directory changes.
2. **Internal add form** ("Build Your Referral Network") — your own clinicians add colleagues they recommend.
3. **Public add form** (optional, "Get Recommended") — the same form with public-facing copy, so colleagues in your wider community can add themselves or recommend someone.

Both forms write to the same sheet, with the same validation, duplicate guard, section-grouped insert, and admin notification email. The two-form split exists because the audiences differ: internal contributors are trusted by default; public submissions are leads the admin reviews.

## Instructions for the agent

- Deliverable = paste-ready files per project (`Code.gs`, `Index.html`, `appsscript.json`) + the sheet + a deploy checklist, unless you have approved direct access to the owner's Google account, in which case build and deploy directly and verify from the served pages.
- Run the setup interview first. Never guess the practice name, admin email, service types, or languages — use placeholders and flag every one you used.
- No vendor-specific features are required: plain Google Apps Script (`SpreadsheetApp`, `HtmlService`, `MailApp`) only.
- If your manifest declares explicit `oauthScopes`, declare the scopes for **every** service the code calls: full `https://www.googleapis.com/auth/spreadsheets` for `SpreadsheetApp.openById` (readonly is not enough), and the send-mail scope that matches the API you use (`MailApp` and `GmailApp` need different scopes — check before you ship, because a missing mail scope fails silently inside try/catch and submissions arrive with no notification).

## Setup interview (ask once, before building)

1. **Practice / network name** — shown in the directory title and form headers.
2. **Admin email** — receives every submission notice; also owns all three projects and the sheet.
3. **Service types** — the directory's sections. Default: `Psychotherapy`, `Psychiatry`. Practices often add e.g. `Psychological Testing`, `Coaching` — whatever they actually refer out for.
4. **Audiences** — internal form only, or internal + public? (Public can be added later; the form project is a copy with different copy.)
5. **Second language view?** — if the practice serves a language community, the directory can offer a toggle that shows only providers speaking that language, under their names in that language. Needs: the language, its marker words in the Languages column, and a name column for it in the sheet. Optional; skip if not needed.
6. **Where will it live?** — the apps are built to embed in a website page (Google Sites or any iframe-friendly page) or stand alone at their URLs. Record the intended page paths (e.g. `/referral-network` and `/referral-network/add`).
7. **Photo policy** — profile photos come from a public URL the submitter pastes. Confirm that's acceptable, or plan a placeholder/initials-only directory (the cards fall back to initials automatically when a photo is missing or fails to load).

## Hard rules

1. **The sheet is the single source of truth.** The directory reads it live on every load; there is no sync job, cache, or export step to keep in step.
2. **Professional public information only.** Names, credentials, locations, services, languages, websites, photo URLs. Never client data, never notes about clients, never anything that would embarrass a colleague if the sheet leaked — assume the directory is public, because it is.
3. **Duplicate names are rejected**, case-insensitively, against the whole sheet, in both forms, with a friendly "already in the list" message.
4. **Entries stay grouped by service type.** A new submission is inserted after the last existing row of its service type, not appended at the bottom.
5. **The admin email fires on every successful submission** — and a failed email never fails the submission (wrap it, log it, return success).
6. **Columns are matched by header name, not position**, in the directory reader, with common alternate spellings accepted. Reordering sheet columns must not break the directory.
7. **The directory never writes.** It has no edit path; corrections happen in the sheet or not at all.
8. **List colleagues with their knowledge.** The forms say so, and the admin's submission email is the review point before a listing is treated as settled.

## Build order

1. The sheet, per `references/data-model.md` (headers exactly as specified; seed it with 3–5 known colleagues so the directory isn't empty at launch).
2. The directory app, per `references/directory-app-spec.md`.
3. The internal add form, per `references/add-form-spec.md`.
4. The public add form, if chosen — a copy of the internal form project with the public title, intro copy, and email subject from the same spec.
5. Deploy per `references/setup-and-deploy.md`; verify per `references/test-checklist.md`.

## Reference files

- `references/architecture.md` — components, data flow, and why it's shaped this way
- `references/data-model.md` — the sheet: columns, optional columns, curation workflow
- `references/directory-app-spec.md` — the read-only directory: reader, cards, search, filters, copy gesture, language view
- `references/add-form-spec.md` — both add forms: fields, validation, duplicate guard, grouped insert, admin email
- `references/security-and-privacy.md` — what's public, consent, review, and what never goes in the sheet
- `references/setup-and-deploy.md` — projects, manifests, deployment settings, embedding
- `references/test-checklist.md` — acceptance tests, in order
