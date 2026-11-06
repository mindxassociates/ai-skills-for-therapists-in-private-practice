# Test checklist

## Scoping (release gate — all must pass)

- [ ] Client A signs in: sees only A's threads. A's session requesting Client B's thread ID → nothing (same as nonexistent).
- [ ] External E sees only threads E participates in; E cannot list clients, cannot open a client thread they're not on, cannot start a thread with a provider they share no thread with.
- [ ] Provider P sees own clients' threads + threads P participates in; P cannot open another provider's client thread; the admin can — and the admin's open is audit-logged.
- [ ] Attachment download by a non-participant (valid session, wrong thread) → refused; by a participant → works and is audited + counted.
- [ ] Workbook and Drive folder Share dialogs: owner only.

## Sign-in and lockout

- [ ] Client code: wrong code ×5 → locked; correct code during lock → refused; after the window → works. Code older than expiry → refused. Code for a disabled account → nothing sent, admin alerted.
- [ ] DOB step appears only when a DOB is on file; wrong DOBs count toward the same lockout.
- [ ] Provider first sign-in sets a PIN (enter + confirm); wrong PINs lock; admin reset clears the hash and the provider sets a new PIN next sign-in; the admin never sees the PIN.
- [ ] Terms gate: a fresh client sees terms before any thread; bumping the terms version re-blocks an existing client until re-acknowledged.

## Messaging

- [ ] Create-by-messaging: unknown email + consent → record created under the sender, message delivered, invitation sent. Without consent → nothing. Another provider's client email → blocked, nothing created. An external's email in the client composer (and vice versa) → blocked.
- [ ] Failed-validation send creates no record.
- [ ] Client-linked external thread without the authorization confirmation → refused; with it → created; the client reference appears in **no** email and **no** audit row.
- [ ] One-time reply ON: recipient replies once within 24h; second reply refused; reply after 24h refused; composer shows the closed note. Announcement (OFF): reply refused immediately with the announcement note.
- [ ] Broadcast: multi-recipient announcement validates all-or-nothing (one bad recipient → zero threads), caps at the limit, one thread per recipient.
- [ ] Notification email: exact subject shape, **no body/subject/client reference anywhere in it**, correct From (alias + display name), correct language.

## Attachments, audit, retention

- [ ] Oversize file, 4th file, and a `.zip`/`.exe` are each refused with a readable message; allowed types save and appear in the thread.
- [ ] Files in Drive are unshared; the raw Drive link (if obtained) does not open for a non-owner account.
- [ ] Download spike (10 in an hour by one account) → exactly one admin alert that hour.
- [ ] `verifyAuditChain` passes on the live log; hand-edit one audit cell in a **copy** → verification reports that row.
- [ ] Retention (in a test copy with a short period): an idle thread archives (placeholder body, files deleted, read-only); a Legal Hold thread in the same sweep is untouched; with period 0 the sweep changes nothing.
- [ ] Kill-all-sessions procedure works: clear the session columns → every test session is signed out.
