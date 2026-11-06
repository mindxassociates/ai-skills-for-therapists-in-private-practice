# Secure Messages Kit

A **secure client-messaging portal you own**, built on Google Workspace + Apps Script + Sheets + Drive — instead of another monthly subscription. Clients, your clinicians, and outside providers you coordinate with message inside the portal; email is used only for sign-in codes and content-free notifications ("You have received a secure message…") that contain no message text, no subject, and no client details.

## What you get

- **Three audiences, one portal.** Clients sign in with email + a 6-digit code; your providers with name + PIN; external providers (referral partners, prescribers, other treaters) with email + code, seeing **only threads they participate in**.
- **Create-by-messaging.** There's no separate invite flow to manage: when a provider sends a first message to a client's email, the client record is created on send (after a consent gate), and the client simply signs in to read it. Duplicate emails, another provider's client, or an email that belongs to an external account all block cleanly.
- **Attachments** on every thread — validated, capped, stored **unshared** in Drive, downloadable only through the app by a participant, every download audited.
- **An audit log with a hash chain** — sign-ins, sends, admin views, downloads — IDs only, never message bodies, and tamper-evident.
- **Provider controls that respect the client:** a per-send toggle allowing the client one reply within 24 hours, or announcement-only sends (including broadcasts to up to 50 recipients, one thread each).
- **Retention you control:** idle-thread sweep with legal hold, off by default.
- **An admin console** (separate small app): people, threads, audit verification, settings, PIN resets, account disable.

## The honest part (don't skip)

This portal is **not end-to-end encrypted**. Messages are stored as plain text in the practice's workbook; the practice admin can read every thread, and so can anyone with access to that workbook or the attachments folder — which is why both are shared with **nobody**, and why the first-login terms tell clients plainly that practice administration can access messages. What you get is HTTPS in transit, Google's encryption at rest, strong sign-in, scoping, and audit — safeguards that *support* HIPAA compliance inside a Google Workspace with a signed BAA. It is not "HIPAA certified"; no software is. Read `references/security-and-privacy.md` in full before deciding this design fits your practice — for many small practices it does, and it's the same trade-off as most EHR messaging, stated honestly instead of marketed away.

Also know your channels: established clients may still message mainly in your EHR. This portal's natural home is **coordination with outside providers** and as an alternative channel you control — position it that way, don't force a migration.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build me a secure messages portal using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/secure-messages-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
