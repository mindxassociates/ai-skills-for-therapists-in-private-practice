# Practice CRM Kit

A **lead-tracking CRM built for a therapy practice**, on Google Workspace + Apps Script + Sheets: every prospective client — from your booking page, your website forms, directory inquiries, and your answering service — lands on one pipeline board, with follow-ups living on each lead, and nothing clinical in it, ever.

## What you get

- **A pipeline board** shaped like a therapy intake actually works: New → Contact Attempted → Consult Booked → Consult Held → Intake Sent → Started, with honest exits (Not a Fit / Declined / No Response / Referred Out).
- **Automatic lead capture.** Your booking system creates/updates the lead when a consult is booked; the post-consult outcome form moves it; website and directory contact forms create or refresh leads; an hourly job turns directory-inquiry and answering-service emails into leads — by rules, without copying message bodies into the CRM.
- **Follow-ups on the lead, not in a separate task app.** Each lead carries a Next Action and due date; an Agenda view shows what's due, overdue, and awaiting a consult outcome.
- **Roles that match a group practice.** The admin sees everything, including internal notes. A provider sees **only their own leads**, never sees the Notes field (stripped on the server, not hidden in the UI), and can self-add leads — which are forced to be theirs.
- **Lifecycle hygiene.** Stale leads auto-archive, deletes are soft with a grace period, stage moves are undoable, duplicates get a merge path, and a sync-health log (no personal data in it) shows every automatic write and whether it worked.

## Who this is for

Group practices losing prospective clients between "they inquired" and "they started" — and solo practitioners who want the same discipline in a single-user version (the roles collapse; everything else still applies).

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build me a practice CRM using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Hard boundaries (read before you build)

- **No clinical notes. Ever.** The CRM tracks the *business* of intake. The moment a client starts, the EHR is the system of record. A lead's Notes field is for intake logistics only.
- **No unattended sending.** The CRM never emails or texts a prospective client on its own. Humans send; the CRM remembers.
- **The workbook is shared with nobody.** Access is through the app, per person, per role.
- Run it in a Google Workspace with a signed BAA if you can — lead data is contact information about people seeking care, and deserves the same handling discipline as the rest of your practice data.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/practice-crm-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
