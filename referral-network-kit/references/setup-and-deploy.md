# Setup and deploy

## Prerequisites

- One Google account for the practice (the admin account) to own the sheet and all projects. A Google Workspace account on the practice domain is the professional choice; the system itself works in any account, and unlike client-data systems there is no BAA requirement here — the directory holds only public professional information.
- The setup interview in `SKILL.md` answered: practice name, admin email, service types, audiences, language view, photo policy.

## Step 1 — the sheet

1. Create the workbook (name it e.g. `Provider Recommendations`) in the admin account.
2. Header row exactly per `references/data-model.md`, core columns A–H in order; add optional columns if chosen.
3. Seed 3–5 consented colleagues per service type.
4. Share it with **nobody**. Copy its ID into each project's config.

## Step 2 — the three projects

Create one Apps Script project per app (`Directory`, `Internal Add Form`, plus `Public Add Form` if chosen). For each: replace `Code.gs`, add `Index.html`, set `appsscript.json` from the kit build. Config constants at the top of each `Code.gs`: `SPREADSHEET_ID`, `SHEET_NAME`, `ADMIN_EMAIL` (forms), `SERVICE_TYPES` (forms).

**Manifest scopes** — if `oauthScopes` is declared, it must cover everything the code calls:

- Directory: `https://www.googleapis.com/auth/spreadsheets` (full — `spreadsheets.readonly` breaks `openById` despite the app only reading).
- Forms: spreadsheets (full) **plus** the send-mail scope for the API the code uses — `https://www.googleapis.com/auth/script.send_mail` for `MailApp`, or `https://www.googleapis.com/auth/gmail.send` for `GmailApp`. A missing mail scope throws inside the try/catch and you get submissions with no notification email — the worst failure mode is a silent one, so send yourself a test submission and confirm the email arrives before calling it done.

## Step 3 — deploy each project

For every project: **Deploy → New deployment → Web app**, with:

- Execute as: **Me** (the admin account)
- Who has access: **Anyone**

Record the `/exec` URLs. If you later change code, deploy a **new version on the same deployment** (Manage deployments → edit → New version) — never create a second deployment and change the URL; everything linking to it (website pages, portals, bookmarks) points at the first URL.

The owner will be asked to authorize on first deploy/run — that's expected; the scopes are the sheet + mail above.

## Step 4 — put it on the website

- Embed each app in its page (iframe / Google Sites embed) at the paths chosen in the interview (e.g. `/referral-network`, `/referral-network/add`), or link the raw `/exec` URLs if the practice has no site yet. The apps allow framing (`ALLOWALL`).
- Link the second-language directory view directly from the practice's second-language pages using `?lang=xx`.
- Give internal clinicians the add-form link where they already work (provider portal/home page) — a form nobody can find collects nothing.

## Step 5 — verify

Run `references/test-checklist.md` end to end, as the submitter and as a visitor, before announcing it.
