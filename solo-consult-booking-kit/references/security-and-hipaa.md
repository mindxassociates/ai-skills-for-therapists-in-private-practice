# Security & HIPAA-Support Notes — Solo Consult Booking Kit

This document supports the practice's HIPAA compliance program; it
does not certify the system as "HIPAA compliant" — no software is.
Give a copy to the owner at handoff, have them keep it with their
risk analysis, and review it at least annually and after any major
change.

## Prerequisite (restated — it gates everything)

The system is HIPAA-supporting **only** inside a Google Workspace
account with a **signed BAA**: Workspace on the practice's own domain
(never a personal `@gmail.com` account), BAA accepted in the Admin
console, and the script projects, workbook, consult calendar, and
sending mailbox all owned by that same Workspace user. 2-Step
Verification (preferably passkeys / Advanced Protection) enforced.
Anything outside that account — above all a personal calendar or a
personal mailbox — is outside the BAA and must not touch this system.
For a solo owner this is simpler than for a group: there are no other
people's accounts involved at all, which is also why this edition
needs no calendar-connection app.

## System summary

- Two Apps Script web apps (public Booking; PIN-gated Console),
  executed as the owner, in the owner's Workspace account.
- Data stores, all in that account: the booking workbook
  (Config / Availability / AvailabilityLog / TimeOff / Appointments /
  Settings / AuditLog), the owner's Google Calendar (generic consult
  events), and Gmail (confirmation / reminder / notification mail).
- Data held per booking: client name, email, phone, state/city,
  payment type/plan, therapy-language preference, for-whom, a
  free-text goals brief (≤600 chars, with an on-form warning against
  detailed clinical history), prior-therapy yes/no, out-of-network
  affordability, referral source, booking times/zones, a **hashed**
  manage token, and the privacy-acknowledgment timestamp + notice
  version.
- **Not collected:** date of birth, SSN, payment-card data, clinical
  notes. Keep it that way — new intake questions need the owner's
  explicit decision, not an agent's initiative.
- Only vendor: Google (Workspace). No analytics, trackers, or other
  third-party services; the public page loads fonts only.

## Risk analysis

| Risk | Safeguards in place | Residual / action |
|---|---|---|
| PHI over-exposure in calendar events | Generic title ("Initial Consultation — <BookingID>"); description limited to BookingID, phone, language, for-whom; no client attendee; full details only in the Appointments tab / PIN-gated Console | Events created by older/other tools may carry details — not this system's doing; check the consult calendar once at setup |
| PHI over-exposure in email | Owner notifications carry a triage minimum; no client name in any practice email subject; client .ics/Google copies carry no manage link | Email is not end-to-end encrypted — inherent to the channel, disclosed in the booking privacy note |
| Manage-link theft / guessing | UUID tokens stored only as SHA-256 hashes (a stored hash can't be replayed); 48h post-appointment expiry; rotation when a new link is emailed; lookup throttling (e.g. 10/token, 200 global per 15 min) | A client who forwards their confirmation forwards the link — same model as commercial schedulers; expiry + rotation bound the window |
| Unauthorized access to the booking record | Workbook private to the owner; apps run as the owner only; full details viewed only through the PIN-gated Console (hashed PIN, 5-try lockout) | Review the workbook's sharing list quarterly — it should list only the owner |
| Owner account compromise (single point of failure: script owner, sheet owner, calendar writer, sender) | Workspace account controls (2-Step Verification; passkeys / Advanced Protection recommended); script project access kept to the owner only | Review Workspace audit logs after any security alert; know the incident steps below before you need them |
| Tampering with booking history | Append-only, sheet-protected AuditLog (BOOKED / CANCELLED / RESCHEDULED / RETENTION_SWEEP, IDs/times only) | The owner could still edit Appointments rows in the sheet directly; the AuditLog makes silent third-party changes detectable, not impossible |
| Error messages leaking internals | Clients see only fixed validation messages or a generic error; raw exceptions go to the execution log only; Console errors likewise generic to anyone without a valid token | — |
| Stale PHI accumulation | Daily retention sweep clears manage tokens 7 days after the appointment and redacts the goals brief after `BookingRetentionDays` (default 90) | The booking record itself (identifiers, payment, times) is retained for practice record-keeping; revisit the period if policy changes |
| Spam / automated abuse | Honeypot field; per-contact + global booking-attempt throttles (fail-open so a cache outage never blocks a legitimate client); LockService against double-booking | No CAPTCHA; revisit if abuse appears |

## OAuth scope justification (give this to the owner verbatim if asked)

Booking app: full `spreadsheets` (open three data areas by ID and
write bookings/audit/retention — readonly cannot `openById` and
cannot write); `calendar` + `calendar.events` (free/busy reads and
inserting/removing the consult event on the owner's own calendar);
`gmail.send` (GmailApp sends client mail, incl. from a send-as
alias); `gmail.settings.basic` **only when an alias is used** (alias
verification goes through the settings API); `script.send_mail`
(MailApp owner notifications — not covered by `gmail.send`);
`script.scriptapp` (time-driven triggers). Console: `spreadsheets`,
`calendar` (free/busy for the availability panel), and the two mail
scopes only if it sends its submission-receipt email. No
external-request scope anywhere: no third-party APIs are called.

## Access control checklist (owner, quarterly)

- Workbook sharing list: owner only.
- Each Apps Script project's sharing: owner only. Deployments are
  always bumped on the existing deployment, never re-minted.
- 2-Step Verification still enforced; recovery email/phone current.
- Console PIN still known only to the owner; reset by clearing the
  Config PIN cells if there's any doubt.

## Incident response (suspected unauthorized access or disclosure)

1. **Contain.** Apps Script editor → Deploy → Manage deployments →
   archive the live Booking deployment to take booking offline. To
   kill every outstanding manage link at once, clear the Appointments
   tab's `ManageToken` column. If the owner account itself may be
   compromised, change its password and revoke sessions in the Admin
   console first.
2. **Assess.** Review the AuditLog tab, the Apps Script Executions
   log, and the Workspace Admin audit log (Drive + login activity
   for the workbook). Identify which bookings' data was involved.
3. **Document.** What happened, when discovered, what data and which
   individuals were affected, what was done — contemporaneously, in
   the practice's incident file.
4. **Notify.** Follow the HIPAA Breach Notification Rule (individual
   notice without unreasonable delay, no later than 60 days after
   discovery; HHS and, for 500+, media notice as applicable) — involve
   the practice's attorney/compliance advisor before notifying. This
   checklist is an operational aid, not legal advice.
5. **Recover & learn.** Restore service on a new version, rotate
   anything exposed, update this analysis with the lesson.

## Open items the owner owns (not the code)

- BAA signed and on file; account on passkeys / Advanced Protection.
- The website privacy policy is a general policy; if the practice
  adopts a formal Notice of Privacy Practices, update the booking
  form's privacy wording/link and bump `PRIVACY_NOTICE_VERSION`.
- Annual review of this document and of the retention period.
