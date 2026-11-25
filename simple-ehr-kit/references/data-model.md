# Data model — the workbook as index

Rule of thumb: **if a human would read it as prose, it is a Drive file. If a screen would list, filter or total it, it is a row.**

## Tabs

### Settings (one row per key, or a small key/value block)
Practice legal/display name, address, phone, timezone, sender alias, reminder hours-before, retention months, backup folder ID, terms version, crisis copy per language. Edited through the app's Settings screen, never by hand-editing code.

### Providers
`ProviderID | DisplayName | LegalName | LicenseLabel | NPI | PinHash | SignInEmail | DefaultVideoLink | Status (Active/Disabled) | IsAdmin`
NPI and license label appear here because superbills need them — supplied by the practice, shown back for confirmation, never invented.

### Clients
`ClientID | ProviderID | FirstName | LastName | PreferredName | DOB | Email | Phone | Timezone | Address | EmergencyContact (short text) | Status (Active/Archived/Discharged) | PortalTokenHash | IntakeStatus | FeeProfileID | CreatedAt | Notes (short admin note only)`
No clinical prose in this tab. Phone is contact data only — v1 sends no SMS.

### FeeSchedule
`FeeProfileID | Label | ServiceLabel | CPT | DefaultMinutes | FeeCents`
Amounts in integer cents, never floating dollars. Multiple profiles allowed (full fee, sliding tiers) — a client points at one profile. The practice supplies every value.

### Appointments
`AppointmentID | ClientID | ProviderID | StartsAtEpoch | EndsAtEpoch | Timezone | Type | Status (Scheduled/Held/Completed/NoShow/Cancelled) | CalendarEventID | VideoLink | NoteID | InvoiceID | ReminderSentAt`
Wall times are entered in the client's/provider's timezone and stored as unambiguous epochs; display converts back and labels the zone.

### NotesIndex
`NoteID | ClientID | ProviderID | AppointmentID | TemplateID | DateOfService | Status (Draft/Signed/Amended) | DriveFileID | ContentHash | SignedAt | SignedBy | AmendmentOf`
The note body is the Drive file. `ContentHash` is computed at signing over the file content.

### NoteTemplates (see clinical-notes.md)
`TemplateID | Label | Status (Active/Retired) | SchemaJSON (in a Drive file if large) | CarryOverFields`

### IntakeIndex
`IntakeID | ClientID | FormLabel | Status | SubmittedAt | DriveFileID`
Form definitions live with the portal code/templates; responses are files.

### Invoices
`InvoiceID | ClientID | ProviderID | AppointmentIDs | IssuedAt | DueAt | TotalCents | PaidCents | Status (Draft/Sent/PartPaid/Paid/Void) | PaymentLink | PaymentMethodLabel | PaymentRef | SuperbillFileID`
One invoice may cover one session (the common private-pay case) or a month of sessions — practice's choice in Settings.

### AuditLog (append-only)
`AtEpoch | ActorKind (Provider/Client/System) | ActorID | Action | RecordKind | RecordID | PrevHash | RowHash`
Actions and IDs only — never note text, never message bodies, never card data (there is no card data).

## Drive layout

```
ChartFiles/
  <ClientID>/           note files, intake files, client uploads
  Generated/            superbill + invoice PDFs
Backups/ (owner-only)   weekly workbook copies, keep last 4
```

Folder and file access is only ever through the app, scoped server-side. The folders are shared with nobody; the practice admin's own access is the stated exception, disclosed in `security-and-privacy.md`.

## Vocabularies are closed

Statuses above are the whole list. A new status is a data-model change, not a free-text entry — free-text statuses break every filter, reminder and report downstream.
