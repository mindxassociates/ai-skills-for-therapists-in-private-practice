# Setup and deploy

## Prerequisites

- Google Workspace on the practice domain, **BAA signed**, 2-Step Verification enforced. (The portal holds real client communications; unlike the directory/CRM kits, this one is not optional-BAA territory.)
- The setup interview answered, including the practice's explicit acceptance of the limits in `security-and-privacy.md`.

## Step 1 — boot the data stores

Portal project created in the admin account. Run the one-time **boot** function once and approve the authorization:

- Creates the portal workbook with all tabs + headers (see `data-model.md`), stores its ID in Script Properties.
- Creates the attachments Drive folder, stores its ID.
- Seeds Settings (page URL blank, retention 0, terms version 1…) and the first admin provider row (no PIN — set at first sign-in).

## Step 2 — manifest scopes (declare them all, up front)

- `https://www.googleapis.com/auth/spreadsheets` — **full** (`openById` breaks on readonly)
- `https://www.googleapis.com/auth/drive` — attachment storage
- `https://www.googleapis.com/auth/script.send_mail` — if the code sends via `MailApp`
- `https://www.googleapis.com/auth/gmail.send` — if it sends via `GmailApp` (and if it sends from an alias via GmailApp, the settings scope `https://www.googleapis.com/auth/gmail.settings.basic` as well — alias verification goes through the settings API; without it the send silently falls back to the bare account address)

A manifest that sends mail but declares the wrong API's scope fails **silently** — codes and notifications just never arrive. Send yourself a code and a notification during setup and confirm both, from the right From, before anything else is called done.

## Step 3 — sender alias

Create the no-reply alias on the script-owning account (e.g. `no-reply@<practicedomain>`), add + verify it under the account's Gmail "Send mail as," set Sender Alias/Name in Settings, and run the sender test. Mail must arrive **From: <Practice Name> <no-reply@…>** — if it arrives from the bare account address, stop and fix the alias/scope before proceeding.

## Step 4 — deploy

- Portal: **Web app, Execute as Me, Access: Anyone** (sign-in is in the app), embedded at the practice's messages page or linked. Admin console: its own deployment, admin-gated server-side, at its own path.
- Later changes: bump the **same deployments** to new versions. Never mint new deployment URLs — every client bookmark and email button points at the first ones.
- **Scope additions later** follow the no-downtime sequence (code first with old manifest, stage scoped manifest, owner re-authorizes in the editor, then version + bump) — see SKILL.md.

## Step 5 — triggers

Install from the setup function (owner-run): **hourly** session/code cleanup, **daily** retention sweep. Verify both on the project's Triggers page and by one manual run each.

## Step 6 — people and go-live

- Providers sign in and set PINs; admin verifies each provider sees only their scope.
- If roster sync is enabled, run it once and confirm new providers appear with blank PINs and departed ones are Disabled — and existing PINs are untouched.
- Send a real client message end-to-end (create-by-messaging), confirm the invitation/notification wording and From.
- Run `references/test-checklist.md`. Scoping failures are go-live blockers, full stop.
