# Security and privacy — the honest limits

Read this with the practice owner before building. If the practice cannot accept the points below, this kit is the wrong tool — say so and stop.

## What the design actually is

- **The workbook is the vault and the exposure.** Client emails, assignment plans (including per-client safety-plan content in setup data), and homework answers live in one Google Sheet. It is owned by the script account and **shared with nobody** — its sharing list *is* the access boundary. The practice admin can open it and read everything; so can anyone who compromises that account. Mitigations are account hygiene (strong auth on the owner account), the sharing rule, and the audit log — not encryption theatre. Data in transit is HTTPS; at rest it is Google's encryption.
- **Token links are bearer credentials.** Whoever holds an assignment link can open that assignment and submit as that client. This is stated to clients implicitly by design and must be stated to the practice explicitly. Bounds that make it acceptable: one token per assignment (never per client), tokens are long random strings stored **hashed**, ending an assignment kills its token, and a token reveals exactly one item for one client — never a list, never other clients.
- **The one plaintext copy.** Recurring reminder emails must contain the working link, and a link cannot be built from a hash. The token plaintext therefore exists in exactly one column of the restricted workbook, used server-side only, never sent in any payload except the client's own reminder emails and the provider's own copy-link for their own client's assignment. If the practice's risk review rejects plaintext-anywhere, the alternative is email-only-once links with no recurring sends — a real functional loss; make the trade consciously.
- **Not end-to-end anything.** Do not describe the system as encrypted messaging, a secure portal, or HIPAA certified — in the UI, in emails, in marketing, anywhere. "HIPAA certified" is banned from every artifact. The accurate sentence: safeguards that support HIPAA compliance inside a Google Workspace with a signed BAA (which is a prerequisite, not an optional extra, if real client data flows through the system).

## Safety rules baked in

- **Not monitored in real time.** Completion screens say the provider reviews results; they never imply live monitoring. Crisis-adjacent items (safety-plan-type) display crisis resources — 988 in the US or the practice's local equivalent, in the client's language — on the item page and the completion screen, and flag every submission `REVIEW` so it waits in the provider's flagged queue (and on the dashboard count / portal bell) until a human marks it reviewed.
- **Safety-plan content is per-client data** (assignment setup), never catalog content, never in an email body.
- **Emails carry no answers.** Reminder emails contain the item name and the link — nothing a client has written, ever. Admin notices (watchdog, alias problems) contain IDs and counts only — no client names, no content.
- **The audit log records actions and IDs** (sign-ins, creates, edits with changed-field names, deletes with cascade counts, flags, reviews, watchdog heartbeats, backups) — never answer content, never email bodies.
- **Scoping is server-side on every call.** A provider's token returns only their own clients' data; guessing another provider's client/assignment/result ID returns the standard not-found (no existence leak). A client token returns only its own assignment. The public self-guided mode returns catalog content only and saves nothing.

## Admin checklist

- [ ] Workbook sharing list = owner only. Re-check after any restore or copy operation (copies inherit folder sharing — keep the backups folder owner-only too).
- [ ] Owner account has strong authentication; the project's authorized scopes are exactly the manifest's (review after any scope change).
- [ ] Sender alias verified live (first engine run), with the fallback notice understood: no alias → mail from the account default + a daily admin notice, never a silent claim.
- [ ] Crisis copy reviewed by a clinician in **every** UI language, and the flag list (which items carry `crisisNote`) reviewed whenever the catalog changes.
- [ ] Client-facing copy reviewed for the honesty lines: bearer-link reality (in the practice's own client communications), not-monitored wording, EHR-is-the-record wording.
- [ ] Backups verified by opening one — a backup that has never been opened is a hope, not a backup.
- [ ] Departed providers disabled in the Providers tab the day they leave (their clients' data stays scoped to rows they can no longer reach).

## Incident posture

If a token link leaks (forwarded email, lost phone): end the assignment — the token dies immediately — and re-issue a fresh assignment/link if the work should continue. If the workbook is ever shared by mistake: unshare at once, review the Audit tab and Drive activity for the window, and treat answer data as exposed for that window. If the owner account is compromised, this system and everything else it owns is in scope — follow the practice's account-compromise plan, not this file.
