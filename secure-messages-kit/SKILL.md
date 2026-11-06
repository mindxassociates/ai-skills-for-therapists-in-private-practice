---
name: secure-messages-kit
description: A secure client-messaging portal for a therapy practice, built on Google Workspace + Apps Script + Sheets + Drive instead of a paid secure-messaging subscription. Use when a practice wants (1) clients signing in with email + 6-digit code, providers with name + PIN, and external providers participant-scoped to only their own threads; (2) message content living only in a practice workbook (shared with nobody) with content-free notification emails; (3) create-by-messaging with a consent gate instead of an invite flow; (4) validated attachments stored unshared in Drive and served only through the app; (5) a hash-chained, IDs-only audit log; and (6) honest limits stated up front — NOT end-to-end encrypted, practice admin can access messages, safeguards support HIPAA compliance inside a BAA-covered Workspace but nothing is "HIPAA certified."
---

# Secure Messages Kit — A Client & External Messaging Portal You Own

## What this system is

Two Apps Script projects over **one workbook + one Drive folder**, all owned by the practice admin account:

1. **Portal app** — where clients, providers, and external providers sign in and message. Threads, messages, people, attachments metadata, settings, and the audit log live in the workbook; attachment files live in the Drive folder, unshared, one subfolder per thread.
2. **Admin console** (separate small app, admin-only) — people management, thread oversight, audit-chain verification, settings, retention sweep. Same workbook, same provider PIN.

Email exists only at the edges: sign-in codes, invitations, security alerts, and **content-free notifications** — a notification says a message arrived and links to the portal; it never carries the body, the thread subject, or a client reference.

## Read this first — the limits, plainly

- **Not end-to-end encrypted.** Message bodies are plain text in the workbook. The practice admin can open and read every thread in the app, and anyone with access to the workbook or the attachments folder can read everything directly. Encryption is HTTPS in transit + Google's at-rest encryption — real, but it does not change the sentence before it.
- Therefore: the workbook and the Drive folder are **shared with nobody**, ever; their sharing lists *are* the access boundary. The first-login terms tell clients that practice administration can access messages — do not soften that line, and do not write terms claiming the admin *won't* look; say access exists, governed by practice policy.
- These are safeguards that **support** HIPAA compliance inside a Google Workspace with a signed BAA. The phrase "HIPAA certified" is banned from every artifact this kit produces.

If the practice cannot accept those three points, this kit is the wrong tool — say so and stop.

## Instructions for the agent

- Deliverable = paste-ready files per project + a one-time `boot` function that creates the workbook, tabs, Drive folder, and seed settings (IDs stored in Script Properties — never hard-code a workbook ID into a fresh build) + checklists. Or build/deploy directly with approved account access, verifying from read-backs.
- Run the setup interview first. Never guess the sender identity, provider list, or retention decision.
- Adding a scope to a live deployment walls the app behind an authorization error until the owner re-grants: sequence it — deploy new code with the **old** manifest first (new-scope calls degrade gracefully), stage the scoped manifest, owner re-authorizes, only then version and bump.

## Setup interview (ask once, before building)

1. **Practice identity** — practice name; notification sender (a no-reply alias on the script-owning account, with a display name); the portal's public page path (embedded page or raw URL).
2. **Providers** — list + stable IDs; they self-set PINs on first sign-in. Confirm the roster source if providers should auto-sync from it (names/status in, departed providers disabled, PINs never touched by sync).
3. **Externals on or off?** — referral partners / outside treaters as participants. If on, client-linked threads will require the sender to confirm an authorization/release is on file, every time one is started.
4. **One-time-reply default** — provider sends can carry "allow one reply within 24 hours" or announcement-only mode. Default in the reference build: one-time reply ON. Announcement mode unlocks multi-recipient broadcasts (≤50).
5. **Terms text** — the practice's first-login terms: not monitored 24/7; not for emergencies (911 / 988); replies within one business day; practice administration access; messages become part of practice records. Versioned — bumping the version re-blocks until re-acknowledged.
6. **Retention decision** — keep forever (default, sweep disabled) or a set period for idle threads, with legal hold per thread. The practice decides and writes it down; the kit ships "off."
7. **Admin console?** — recommended yes for any multi-provider practice.

## Hard rules

1. **Content lives in exactly two places:** the workbook and the attachment files. Never in email, never in logs, never in a second store.
2. **Hashes only** for sign-in codes, PINs, DOB second factors, and session tokens (SHA-256, salted with the record ID). Raw values are never stored or logged.
3. **Participant scoping on the server, on every call.** A client sees only their threads; an external sees only threads they participate in and can never enumerate clients; a provider sees their own clients' threads and threads they participate in; only the admin sees all. Guessing an ID returns nothing.
4. **One email = one account kind.** An address on the Clients list can't be invited as an External, and vice versa; a provider messaging another provider's client's email is blocked and creates nothing.
5. **Create-by-messaging with a consent gate.** A provider's first send to an unknown client email creates the record — only after the consent confirmation, only assigned to that provider, and a send that fails validation creates nothing.
6. **Authorization confirmation for client-linked external threads**, on every thread start, server-checked.
7. **Attachments:** count/size/type caps (default ≤3 files, ≤10 MB each, ≤25 MB per message; PDF/Office/CSV/text/common images; no archives or executables), filenames sanitized, files stored unshared, downloads only through the app by a participant, every download audited.
8. **Audit log is append-only and hash-chained** (each row covers the previous hash + its fields): actors, actions, IDs — never bodies, never client references in external-thread rows. Admin opening a thread they don't participate in is itself logged.
9. **Lockouts shared and pruned correctly:** 5 failed attempts → 15-minute lock across code/DOB/PIN surfaces; pruning must not erase still-counting attempts (a classic bug: prune entries with `until <= cutoff` deletes counters whose `until` is 0 — prune only expired locks and stale counters by age).
10. **Security alerts** to the admin (lockout, code request for a disabled account, download spike) — alert failure never blocks the underlying operation.

## Build order

1. Workbook + Drive folder via boot, per `references/data-model.md`.
2. Sign-in + sessions per `references/access-and-sessions.md`.
3. Messaging (threads, create-by-messaging, reply modes, attachments, notifications) per `references/messaging-features.md`.
4. Audit chain, alerts, triggers (hourly session/code cleanup; daily retention sweep).
5. Admin console.
6. Deploy per `references/setup-and-deploy.md`; verify per `references/test-checklist.md` — scoping tests are the release gate.

## Reference files

- `references/architecture.md` — components, data flow, where content lives
- `references/data-model.md` — workbook tabs, Drive layout, settings
- `references/access-and-sessions.md` — the three sign-ins, lockouts, terms gate
- `references/messaging-features.md` — threads, create-by-messaging, reply modes, attachments, notifications
- `references/security-and-privacy.md` — the honest limits, controls, admin checklist, incident response
- `references/setup-and-deploy.md` — boot, scopes, deploys, sender alias, triggers
- `references/test-checklist.md` — acceptance tests, scoping first
