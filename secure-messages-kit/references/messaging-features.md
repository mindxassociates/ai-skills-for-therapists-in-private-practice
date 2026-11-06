# Messaging features

## Threads and sending

- A thread belongs to its participants; the thread list and every message read are participant-scoped server responses.
- Unread counts are tracked **per side** (a peer thread's two providers have independent counts).
- Provider-to-provider (peer) threads exist for internal coordination: visible only to the two participants (+ admin oversight), carrying no client reference.

## Create-by-messaging (no invite flow)

The portal has **no separate invite/registration flow**. A provider composes a new thread to a client by email address:

1. The composer asks for the **consent confirmation** first (the client has agreed to be contacted here) — no confirmation, no send.
2. On send, the server resolves the email:
   - **Own existing client** → thread created on that record.
   - **Unknown email** → a client record is created, assigned to the sending provider, then the thread + message save, then the invitation/notification email goes out.
   - **Another provider's client** → blocked, nothing created.
   - **An External's email** (or vice versa for externals) → blocked, nothing created. One email = one account kind.
3. A send that fails validation creates **nothing** — records are created only on a validated save, never speculatively.
4. Every creation is audit-logged (IDs only).

Externals are created by the admin (or by messaging one, same resolution rules), and an external's world is narrow: they see only threads they participate in, cannot browse or enumerate clients, and can start a conversation only with the admin or a provider they already share a thread with.

## Client-linked external threads

When a thread will reference a client (coordination about a shared client), the sender must confirm — **on every thread start** — that an authorization/release is on file. Server-checked, not a dismissible hint. The client reference is stored only on the thread row.

## One-time reply and announcements (provider sends)

A per-send toggle in the provider composer (default per the setup interview; reference default ON):

- **Toggle ON — "Allow one-time reply within 24 hours":** the recipient, signed in normally, may send exactly one reply within 24 hours of that message; after replying or after the window, their composer in that thread disables with a plain note. A newer provider message re-evaluates under its own mode. The mode is stored on the message row; only provider sends can carry one (enforced in the save path).
- **Toggle OFF — announcement:** the recipient cannot reply to it at all; their composer shows the announcement note. With the toggle OFF, the composer also accepts **multiple recipients of one kind** (clients, externals, or providers — up to 50): the server validates **every** recipient before creating anything (one invalid → whole send fails, zero side effects), then creates one independent announcement thread per recipient, attachments stored per thread.

The toggle never restricts the sender, and it never creates an anonymous path — the recipient always reads and replies through their normal signed-in session.

## Attachments

- On every thread, for every participant kind. Defaults: **≤3 files per message, ≤10 MB each, ≤25 MB total**; types limited to PDF, Word, Excel, CSV, plain text, and common images; archives and executables refused; filenames sanitized.
- Files land in the thread's unshared Drive subfolder; metadata in the Attachments tab.
- **Download = through the app only**, after a participation check, audited, counted. 10+ downloads by one account in an hour → admin alert (at most one per account per hour).

## Notifications (content-free, always)

After a message saves, the other participants get an email:

- Subject pattern: `You have received a secure message from <Sender Name> from <Practice Name>` — exactly that shape.
- Body: a plain notice + the portal button/link. **No message body, no thread subject, no client reference, no preview — ever**, including for one-time-reply sends (which may add exactly one plain sentence: one reply is allowed within 24 hours).
- Language: the recipient's known language; bilingual when unknown (if the practice is bilingual).
- Sent from the practice's no-reply alias with its display name; if the alias send fails, mail falls back to the account address and the fallback is **logged** (a wrong From is a trust bug, not a detail).

## Retention sweep (optional, off by default)

Daily trigger; when a retention period is set, threads idle longer than it are archived: bodies replaced with a placeholder, attachment files deleted, thread read-only. **Legal Hold** on a thread exempts it. Default `MessageRetentionDays = 0` — keep forever — until the practice makes and records its own decision.
