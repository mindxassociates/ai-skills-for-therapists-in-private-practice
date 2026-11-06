# Security & HIPAA-Support Notes — Group Consult Booking Kit

This document supports the practice's HIPAA compliance program; it
does not certify the system as "HIPAA compliant" — no software is.
Give a copy to the practice admin at handoff, keep it with the
practice's risk analysis, and review it at least annually and after
any major change.

## Prerequisites (restated — they gate everything)

Google Workspace on the practice domain with a **signed BAA**; the
central system (all five Apps Script projects, Roster + Booking +
submissions workbooks, sending mailboxes) owned by **one practice
Workspace account** with 2-Step Verification (passkeys / Advanced
Protection recommended). **Provider-calendar policy, decided and
documented before onboarding:** calendars owned by practice Workspace
accounts are inside the BAA; calendars on providers' **personal**
Google accounts are **outside** it. The mitigations below (generic
events, minimum descriptions) reduce what a personal calendar holds,
but they do not bring it inside the BAA — if the practice accepts
personal calendars, that acceptance is a documented risk decision by
the practice, owned by the practice.

## System summary

- Five Apps Script web apps: Booking (public, anonymous, runs as the
  practice account), Connect Your Calendar (runs as each provider,
  for calendar sharing only), Manage Availability / My Consults /
  Consult Admin (run as the practice account, PIN-gated).
- Data held per booking: client name, email, phone, state/city,
  payment type/plan, language preference, for-whom, gender
  preference, goals brief (≤600 chars, on-form warning against
  detailed clinical history), prior-therapy yes/no, OON
  affordability, referral source, times/zones, a **hashed** manage
  token, privacy-acknowledgment timestamp + notice version.
- **Not collected:** DOB, SSN, payment-card data, clinical notes.
  New intake questions need the admin's explicit decision.
- Only vendor: Google (Workspace). No analytics, trackers, or other
  third parties; the public page loads fonts only.

## Risk analysis

| Risk | Safeguards in place | Residual / action |
|---|---|---|
| PHI over-exposure on provider calendars | Generic title ("Initial Consultation — <BookingID>"); call-minimum description; no attendee; full details only in Appointments / PIN-gated My Consults | Events from before the hardening, or from other tools, may carry details. **Personal-account calendars are outside the BAA** (see Prerequisites) — policy decision, reviewed annually |
| PHI over-exposure in email | Practice notifications = triage minimum; no client name in any practice email subject; client .ics copies carry no manage link | Email is not end-to-end encrypted — inherent, disclosed in the booking privacy note |
| Provider impersonation / cross-provider access | Fleet PIN is hashed in the Roster; tokens verified server-side on every call; every provider app scopes data to the verified provider; admin app re-checks admin identity per call | A shared/guessed PIN is the weak point — 4-digit PINs + 5-try lockout + admin reset are the controls; never widen a provider's view "temporarily" |
| Manage-link theft / guessing | UUID tokens stored only as SHA-256 hashes; 48h post-appointment expiry; rotation when re-emailed; lookup throttling | A forwarded confirmation forwards the link — same model as commercial schedulers; expiry + rotation bound it |
| Unauthorized access to the booking record | Workbooks private to the practice account; script projects owned by it alone; quarterly sharing review | Workbook/project sharing lists are the audit surface — review them (below) |
| Practice account compromise (single point of failure) | Workspace controls; project access verified minimal (owner only) | Passkeys/Advanced Protection for the practice account; know the incident steps before you need them |
| Tampering with booking history | Append-only, sheet-protected AuditLog (IDs/times only) | Sheet editors can still alter rows; the AuditLog makes silent changes detectable, not impossible |
| Error leakage | Clients/providers see fixed generic messages; raw exceptions only in execution logs; the Connect API likewise returns generic errors | — |
| Stale PHI accumulation | Daily retention sweep: manage tokens cleared 7 days post-appointment; goals brief redacted after `BookingRetentionDays` (default 90) | The booking record itself is retained per practice record-keeping policy; revisit the period if policy changes |
| Spam / abuse | Honeypot; per-contact + global attempt throttles (fail-open); LockService against double-booking | No CAPTCHA; revisit if abuse appears |
| Departed provider access | Offboarding checklist: disconnect calendar (Connect app or manual unshare), set Roster row inactive, re-sync, clear their PIN cells | Any single step alone leaves a stale path — do all four, then run `checkSetup()` |

## OAuth scope justification (per project)

- **Booking:** full `spreadsheets` (three workbooks by ID, writes);
  `calendar` + `calendar.events` (batched free/busy across provider
  calendars; insert/remove events); `gmail.send` (GmailApp client
  mail incl. alias); `gmail.settings.basic` only when an alias is
  used; `script.send_mail` (MailApp notifications — not covered by
  `gmail.send`); `script.scriptapp` (triggers).
- **Connect Your Calendar:** `calendar` (share/unshare the provider's
  own calendar, acting as them), `script.external_request` (call the
  Booking app's API), `userinfo.email` (identify the accessing
  account). Nothing else — notably no spreadsheets.
- **Manage Availability:** full `spreadsheets`, `calendar`
  (free/busy for its panel), `gmail.send` + `script.send_mail`
  (receipt mail via MailApp).
- **My Consults:** full `spreadsheets` only.
- **Consult Admin:** full `spreadsheets` + `calendar` only.
- The same scopes must be declared on each GCP project's OAuth
  consent screen (Data Access) — verification tooling reads the
  console, not the manifest.

## Access control checklist (admin, quarterly)

- Sharing lists of the Roster, Booking, and submissions workbooks:
  practice account only (plus any explicitly intended staff).
- Each script project: owned by the practice account, no extra
  editors. Deployments always bumped on existing deployments.
- 2-Step Verification enforced for the practice account and provider
  Workspace accounts (where providers have them).
- Departed providers fully offboarded (row per the table above).

## Incident response (suspected unauthorized access or disclosure)

1. **Contain.** Archive the Booking app's live deployment to take
   booking offline. To kill every manage link at once, clear the
   Appointments `ManageToken` column. If the practice account may be
   compromised, change its password + revoke sessions in the Admin
   console first.
2. **Assess.** AuditLog, Apps Script Executions, Workspace Admin
   audit log (Drive + login activity). Identify affected bookings.
3. **Document.** What, when discovered, whose data, what was done —
   contemporaneously, in the practice's incident file.
4. **Notify.** HIPAA Breach Notification Rule (individual notice
   without unreasonable delay, ≤60 days; HHS/media as applicable) —
   involve the practice's attorney/compliance advisor first. This
   checklist is an operational aid, not legal advice.
5. **Recover & learn.** Restore on a new version, rotate what was
   exposed, update this analysis.

## Open items the practice owns (not the code)

- Provider personal-calendar policy (above) — decide, document,
  review annually.
- BAA signed and on file; practice account on passkeys / Advanced
  Protection.
- Connect-app OAuth verification status (operational without it via
  the Advanced click-through; pursue it, don't block on it).
- If the practice adopts a formal Notice of Privacy Practices, update
  the booking privacy wording/link and bump `PRIVACY_NOTICE_VERSION`.
