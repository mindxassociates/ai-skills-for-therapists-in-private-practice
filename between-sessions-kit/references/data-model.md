# Data model — the workbook

One workbook, created fresh for this app, owned by the script account, **shared with nobody**. Header row is row 1 on every tab; all IDs are strings; joins are by ID only. Timestamps are stored as text in the practice timezone **plus** a numeric epoch column wherever sorting/filtering matters — because Sheets will auto-convert date-shaped text into date cells on write, server code treats every date-shaped read as "may be a Date object" (see `build-and-deploy.md`).

## Clients — one row per client **per provider**

The same person seeing two providers is two rows with two ClientIDs; providers never see each other's clients.

`ClientID` (generated, immutable) · `ProviderID` · `FirstName` · `LastName` · `PreferredName` (optional; used in greetings) · `Email` (reminder destination; required before any email reminder can be scheduled) · `Language` (`en` / second-language code — drives client UI + email language) · `CaregiverName` · `CaregiverEmail` (optional; caregiver items may route here) · `Status` (`Active` / `Archived`) · `CreatedAt` · `CreatedByProviderID` · `NotesPrivate` (provider-only; **never** sent in a client payload) · `Timezone` (IANA zone — governs all reminder times for this client; blank = practice zone).

Deliberately absent: no phone-as-messaging field, no demographics. Demographics belong in the EHR.

Edits are **in place**: name, email, language, timezone, caregiver, notes — ClientID and every issued token are untouched, and each value-changing edit writes an audit row naming the changed fields. Hard delete (for test/duplicate rows) cascades by ClientID — instances, then results, then assignments, then the client row — and the audit row recording the counts is written *after* the cascade so the trail survives.

## Assignments — one provider giving one client one item, with one plan

`AssignmentID` · `ProviderID` · `ClientID` · `CatalogSlug` (catalog slug, or a custom exercise's slug) · `Mode` (`InSession` / `Homework`) · `Status` (`Active` / `Paused` / `Ended` / `Completed`) · `SetupJSON` (item setup chosen at assignment — e.g. safety-plan content, exposure target; validated server-side against the item's setup schema) · `MessageCustom` (provider-edited reminder message; blank = system template) · `RecurrenceJSON` (see `reminder-engine.md`; blank for in-session) · `StartDate` · `EndRule` (`None` / `ByDate` / `AfterOccurrences`) · `EndValue` · `TimesOfDay` (comma list of `HH:mm`, read as wall times **in the client's zone**) · `Timezone` (the client's zone, snapshotted at creation) · `TokenHash` (SHA-256) · `TokenPlain` (restricted-workbook only — see `security-and-privacy.md`) · `CreatedAt` · `LangAtAssign` (snapshot of the client's language at assignment).

In-session practice is an Assignment too (`Mode = InSession`, zero instances).

## ReminderInstances — the unit the engine acts on

One row per scheduled send, **materialised ahead** (never computed on the fly at send time), so the provider's Reminders Summary is a plain table read.

`InstanceID` · `AssignmentID` · `ProviderID` · `ClientID` · `CatalogSlug` (the last three denormalised for provider-scoped queries) · `ScheduledFor` (client-zone wall text) · `ScheduledEpoch` (numeric; the engine's due test and all range queries use this) · `Channel` (always `email` — any other value is a validation error) · `Status` (`Not started` / `Sent` / `Completed` / `Skipped` / `Failed`) · `SentAt` · `CompletedResultID` (→ Results when the client completes) · `RandomSlot` (`Y` for affirmation instances, placed randomly inside their window) · `ErrorNote` (last send error, short text) · `Attempts` (engine retry counter).

## Results — one row per completion

`ResultID` · `AssignmentID` · `InstanceID` (blank for in-session / self-initiated completions) · `ProviderID` · `ClientID` · `CatalogSlug` · `CompletedAt` · `AnswersJSON` (the full step answers) · `ScoreTotal` / `ScoreBand` / `ScoreDetailJSON` (only for scored items; blank otherwise — and blank must survive the trip to the browser as `''`, never `NaN`) · `Flag` (blank / `REVIEW` for crisis-adjacent items) · `DurationSec` (timer items) · `LangUsed` (language the client actually completed in) · `ReviewedAt` · `ReviewedBy` (the reviewed stamp that clears the flag everywhere).

Self-monitoring, sleep-log, and exposure items produce **many** Results per Assignment; one-shot items produce one per credited instance.

## CustomExercises

`CustomID` · `Slug` (`exercises/custom-<slug>`; uniqueness checked against catalog + this tab) · `OwnerProviderID` (the author, or the reserved `PRACTICE` owner = shared to all providers) · `TitleEN` / `TitleZH` · `Category` (from the catalog category list) · `Type` · `StepsJSON` (same step schema as the catalog — see `catalog-format.md`) · `Status` (`Draft` / `Published` / `Retired` — only Published is assignable) · `CreatedAt` · `UpdatedAt` · `Description` (shown in the assign library).

Drafts edit **in place** (same ID, same slug, still Draft). Editing a **Published** item forks a new version — assignments already made keep pointing at the version they were given, so results stay interpretable.

## Providers

`ProviderID` · `DisplayName` · `Email` · `Timezone` · `PINHash` (SHA-256 of `ProviderID + ":" + PIN`) · `PINToken`/session fields · `Active` · `FailedCount` · `LockedUntilEpoch`. Seeded from the practice roster or by an admin seed function; if roster-synced, sync adds new providers and disables departed ones but **never** overwrites an existing PIN hash.

## Audit

Append-only: `Timestamp` · `Actor` (ProviderID / `SYSTEM` / `CLIENT:<ClientID>`) · `Action` · `ObjectID` · `Detail` (short; counts and IDs — **no answer content, no email bodies**). The watchdog and backup write their heartbeat rows here, so a silent night is itself visible.

## Config (key/value)

Workbook version · sender display name · crisis copy per language · default reminder template per language · materialisation window days (60) · scheduling horizon days (~370).
