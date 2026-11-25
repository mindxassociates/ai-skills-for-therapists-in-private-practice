# Between Sessions Kit

A **between-session client homework system you own**, built on Google Workspace + Apps Script + Sheets — instead of a per-seat homework-platform subscription. Providers assign exercises and reminders from a small library; clients open a personal link and do the work in their browser. No client accounts, no app to install, and **no texting**: reminders are email only, on purpose.

## What you get

- **A real library, not a PDF folder.** A catalog of exercises and reminders — chatbot-style cognitive and social-skills practices, journals, self-monitoring logs (emotions / thoughts / behaviours / distress / sleep), breathing and mindfulness timers, affirmations, and simple custom reminders — each a short guided flow the client completes on a phone. The reference build runs 137 items; yours can start with a dozen and grow.
- **Assigning takes under a minute.** A 3-step wizard: pick the item, pick the client, pick the schedule — once, daily, weekly, every N days, or custom dates, multiple times a day, with an end date or an occurrence count, plus an optional custom message. The wizard states the plan back as a plain sentence ("…will get Thought log by email every Mon at 7:00 PM, starting Nov 23 — client's time — Los Angeles") before you confirm, and the result card's link copies on tap.
- **Clients just tap a link.** Each assignment has one personal link. No sign-up, no password, no app. The same library is also browsable as a public self-guided index — visitors can practise on their own; nothing they enter there is saved or sent to anyone.
- **Reminders that respect the client.** The engine runs every 15 minutes and schedules in the **client's timezone**, not yours. If a client does the work *early*, the submission credits the pending reminder — they are never emailed about homework they already finished, and your adherence numbers stay honest.
- **Bilingual, honestly.** A language pill switches the whole client experience (and the reminder emails). Clinical translations are **authored by a human or not shipped** — an item without an authored translation shows the English content with a visible note, never a machine translation dressed up as authored.
- **Review that surfaces what matters.** Submissions land in a review queue with readable prompt → answer pairs (never a raw data dump). Safety-plan-type items flag on every submission and show crisis resources to the client on completion; marking a result reviewed clears the flag everywhere, including a portal notification bell if you run one.
- **Your own exercises, too.** A step builder (text / choice / free-text / rating steps, with descriptions) lets providers draft, publish, retire, and delete custom exercises (deletable only while a draft, retired, or never assigned; once assigned, retire is the only path) — their own, or shared practice-wide. Drafts are editable in place; editing a published item forks a version so existing assignments stay interpretable.
- **Guardrails included.** A nightly watchdog emails the admin if reminders ever get stuck unsent (IDs only — no client names, no content), and the workbook backs itself up weekly, keeping the last four copies.

## The honest part (don't skip)

The personal link **is** the client's credential — anyone who holds it can open that one assignment. That is the deliberate trade for zero-friction access, and it is why links are per-assignment, stored hashed, and killed when an assignment ends. Client emails and homework answers live in one workbook that is **shared with nobody**; the practice admin account can open it, and the kit says so rather than pretending otherwise. The system is **not monitored in real time** and is not a crisis channel — flagged items show crisis resources and queue for review, and the completion copy tells clients their work is reviewed by their provider, not watched live. These are safeguards that *support* HIPAA compliance inside a Google Workspace with a signed BAA; nothing here is "HIPAA certified." And your EHR stays the system of record — this is the between-session layer, not a chart. Read `references/security-and-privacy.md` before deciding the design fits your practice.

Also know the channel decision is structural: **there is no SMS in this system at all** — no provider to configure, no phone numbers collected for messaging. If your clients reliably read email, that is a feature (one less vendor, one less consent surface). If they don't, no kit setting will fix it.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build me a between-session homework system using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/between-sessions-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
