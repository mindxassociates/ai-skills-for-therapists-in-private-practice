# Simple EHR Kit

A **simple private-pay EHR you own**, built on Google Workspace + Apps Script + Sheets — instead of a per-seat EHR subscription with features a private-pay practice never uses. Clients, scheduling, notes, intake, invoices and superbills, in one small system that runs in your own Google account.

## Who this is for — and who it is not for

**For:** solo therapists and small practices paid **directly by clients** — full fee, sliding scale, HSA/FSA — who offer a superbill so clients can seek out-of-network reimbursement themselves.

**Not for:** in-network insurance billing. This system does **not** submit claims, check eligibility, post ERAs, or manage denials, and it is not a workaround for a panelled practice's billing. If most of your revenue is insurance claims, use a claims-capable EHR for that work — or use this kit only for a clearly separated private-pay caseload.

## What you get

- **Today, at a glance.** The provider app opens to today's appointments, unsigned notes and unpaid invoices — not to a data dump.
- **A note builder that fits your work.** Build your own templates (fields, prompts, checkboxes, rating scales), start a note from the appointment in one tap, and **carry over** the previous note's stable sections in one click. Sign and lock when done; corrections are dated amendments, never silent edits.
- **Scheduling without a second calendar.** Appointments live with your Google Calendar, carry your own video link (Zoom / Meet / your choice), and trigger **email reminders** — no native video and no texting vendor to pay for.
- **A client portal with no passwords.** Each client gets one personal link: intake packet on their phone, upcoming appointments, invoices and superbills to download. Intake answers land in the chart — no re-typing paper forms.
- **Private-pay billing, complete.** Invoices from your own fee schedule (kept in Settings, never hard-coded), payment by link through your own processor — card numbers never touch the app — and a **one-click PDF superbill** with the identifiers and codes *you* supply.
- **Your data, exportable.** Export one client's full chart, or the whole practice's, as files you own, at any time.
- **Built to stay fast.** Each practice installs its own copy; the spreadsheet holds only a light index while notes and documents live in Drive; old years archive out of the live workbook; screens load in small pages instead of reading everything. A solo practice has years of headroom, and a small group does too — see the kit's scaling reference for the honest thresholds.

## The honest part (don't skip)

The client's portal link **is** their credential — anyone who holds it can open that client's portal. That is the deliberate trade for zero-friction access, and links are per-client, revocable and stored hashed. Chart data lives in one workbook and Drive folders that are **shared with nobody**; the practice admin account can open and read them, and the kit says so rather than pretending otherwise. The portal is **not monitored in real time** and is not a crisis channel. These are safeguards that *support* HIPAA compliance inside a Google Workspace with a signed BAA; nothing here is "HIPAA certified." Read `references/security-and-privacy.md` before deciding the design fits your practice.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build me a simple private-pay EHR using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered, and confirm with me first that private-pay-only billing fits my practice."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/simple-ehr-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
