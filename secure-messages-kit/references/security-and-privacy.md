# Security and privacy — the honest reference

Keep this document with the practice's compliance records. It describes safeguards that **support** HIPAA compliance. They are not a certification, and no software is "HIPAA certified."

## Where the data lives

| Data | Where |
|---|---|
| Message bodies, subjects, participants, unread counts | The portal workbook (plain text) |
| People records: names, emails, assignments, status, code/PIN/DOB **hashes**, session hashes, terms acknowledgments | The portal workbook |
| Attachment files | The attachments Drive folder (per-thread subfolders, unshared) |
| Attachment metadata | The portal workbook |
| Audit log (timestamps, actor/target IDs, actions, hash chain) | The portal workbook |
| Codes and message content in email | **Nowhere** — codes are hashed at rest; notification emails contain no content |

## The plain statement (include it in your own copy of this file)

Practice administration access, stated plainly: the practice admin can open and read every conversation in the app, and anyone with access to the workbook or the attachments folder can read all message content directly. Messages are stored in plain text in the workbook. In transit, connections run over TLS (HTTPS); at rest, Google encrypts stored data with keys Google manages. That does not make the portal end-to-end encrypted, and this kit never claims it is. Clients and external providers are told in the first-login terms that practice administration can access messages.

**Consequence:** the workbook's and folder's sharing lists are the real access boundary. They stay empty — owner only — permanently, and they belong in the practice's periodic access reviews.

## Controls checklist

- [ ] Sign-in codes, PINs, DOB factors, session tokens: SHA-256 hashes only.
- [ ] 5-try / 15-minute lockout shared across surfaces, with the pruning rule from `access-and-sessions.md` (verify by test, not by reading code).
- [ ] Participant scoping verified on every endpoint, including downloads and thread-by-ID reads.
- [ ] One-email-one-kind enforced on every creation path (composer, admin console, any import).
- [ ] Authorization confirmation required for client-linked external threads.
- [ ] Attachment caps + type whitelist + filename sanitization; files unshared; downloads audited and counted.
- [ ] Hash-chained audit log; admin views of non-participated threads are logged; `verifyAuditChain` runs clean.
- [ ] Security alerts wired: lockout, disabled-account code request, download spike. Alert failures logged, never blocking.
- [ ] Terms gate with versioning; admin-access line present and unpromised-away.
- [ ] Retention decision made, written here, and set in Settings (or explicitly "keep forever").

## Administrator checklist (outside the code)

- [ ] Google Workspace BAA accepted for the organization; copy filed.
- [ ] Passkey / Advanced Protection on the account owning the projects, workbook, and folder; 2-Step Verification enforced org-wide.
- [ ] Workbook shared with nobody; attachments folder shared with nobody (check the actual Share dialogs).
- [ ] No-reply sender alias created and verified in the owning account's send-as settings, and a sender test proves mail goes out under the alias + display name (not the bare account).
- [ ] Cleanup (hourly) and retention (daily) triggers installed and owned by the admin account.
- [ ] Portal Settings reviewed: page URL, alert email, sender alias/name, retention days.

## Incident response

- **Kill all sessions:** clear the Session Hash/Expiry columns in Clients, Providers, and Externals. Everyone signs in again.
- **Disable one account:** admin console (or Status in its tab) — sessions end at once; code requests are refused and alerted.
- **Suspected audit tampering:** run `verifyAuditChain` as admin, note the first mismatching row, **preserve a copy of the workbook before changing anything**.
- **Suspected compromise:** disable the account, kill sessions, review the audit rows for that ID (sign-ins, sends, downloads, admin views), re-enable only after out-of-band identity verification.
