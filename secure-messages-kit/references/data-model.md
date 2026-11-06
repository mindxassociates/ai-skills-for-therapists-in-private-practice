# Data model — portal workbook + Drive

Created by the boot function; headers self-heal on read. Shared with **nobody**.

## Clients

Client ID · Name · Email · Assigned Provider ID · Status (Active/Disabled) · Code Hash · Code Expiry · Session Hash · Session Expiry · DOB Hash (optional, when the practice collects it as a second step) · Failed Attempts · Locked Until · Terms Version + Acknowledged At · Language (when known) · optional Lead ID (if the practice's CRM links the person — internal only, **never** sent to client/external payloads).

## Providers

Provider ID · Name · Email · Pin Hash (SHA-256 of Provider ID + PIN) · Session Hash · Session Expiry · Status · Failed Attempts · Locked Until. Rows may be roster-synced (see `architecture.md`); sync never overwrites a Pin Hash.

## Externals

External ID · Name · Organization · Profession · Email · Status · Code/Session hash fields (as Clients) · Terms Version + Acknowledged At. An email exists in exactly one of Clients / Externals — enforced on every creation path.

## Threads

Thread ID · Kind (Client / External / Peer) · Client ID (when client-linked) · Participant IDs · Subject · Created By · Created At · Last Message At · per-side Unread counts · Legal Hold (yes/no) · Archived (by retention) flag. The client reference lives **only** on this row — never in emails or audit rows.

## Messages

Message ID · Thread ID · Sender ID + kind · Body · Created At · One-Time-Reply Mode (`YES` / `NO` / blank for client/external sends and legacy) · Attachment count. Bodies exist here and nowhere else (plus the attachment files themselves).

## Attachments

Attachment ID · Message ID · Thread ID · File Name (sanitized) · MIME type · Size · Uploader ID · Drive File ID · Created At · Download count. The file itself sits in the thread's Drive subfolder, unshared.

## AuditLog

Timestamp · Actor ID + kind · Action (sign-in, code request, send, download, admin view, disable, retention…) · Target IDs only · Prev Hash · Row Hash. Hash = SHA-256 over previous hash + the row's own fields; a `verifyAuditChain` function (admin-only) reports the first mismatching row. Tamper-**evident**, not tamper-proof — say so.

## Settings (key/value)

Portal Page URL · Alert Email · Sender Alias · Sender Name · Message Retention Days (0 = keep forever, sweep off) · Terms Version · Roster sync config (source, interval, last run) · Response Note (the "replies within one business day" line shown in the portal).

## Drive layout

`Client Portal Attachments/` (root, unshared) → one subfolder per Thread ID → the thread's files, named with the sanitized original filename. Nothing in this tree is ever shared, published, or linked directly; downloads are streamed through the app after a participation check, and each download writes an audit row + increments the count (the spike alert reads these).
