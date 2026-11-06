# Data model — the CRM workbook

Workbook title: `CRM` (configurable). Shared with **nobody**. Tabs are created and header-checked by the app's setup function (self-healing: a missing tab or header row is recreated; never hand-maintain headers).

## Leads (one row per prospective client)

| Field | Notes |
|---|---|
| Lead ID | `CRM-####`, assigned at creation, never reused, never changes. The through-line other systems cite in deep links and write-backs. |
| First Name / Last Name | As given by the inquirer. |
| Email / Phone | Matching keys (see `ingest-and-sync.md`). |
| Preferred Language | Drives who should reply and in what language. |
| Source | Controlled taxonomy from the Sources tab (booking page, website, each directory, answering service, referral…). Not free text. |
| State | Inquirer's state — license matching happens against it. |
| Age Group / Client Type | Coarse categories only (e.g. Adult / Teen; Individual / Couples / Family) — enough to route, not a clinical picture. |
| Insurance / Payor | What the inquirer named (a plan name, "private pay", an EAP). Never verified benefits data. |
| Concern Category | A short category from a controlled list (anxiety, couples, trauma…) — **a category, never the client's own words**. |
| Matched Provider ID / Name | Who owns this lead. The scoping key for all provider views. |
| Stage | Pipeline stage or exit (see SKILL.md). |
| Consult At | Booked consult date/time when known. |
| Booking ID | The booking system's ID, for cross-reference. |
| Next Steps Outcome | The verbatim outcome from the post-consult form (Booked intake / Will schedule later / Not a fit…) once recorded. |
| EHR Destination / EHR Client Status | Where the client landed once started (which EHR, and their status there) — a pointer, not a record. |
| Next Action / Next Action Due | The follow-up, on the lead. |
| Owner | Who is responsible for the next action (defaults to the matched provider). |
| Thread Link | Link to the originating inbox thread, if any — the human can read the original there; the CRM doesn't copy it. |
| Notes | **Admin-only**, intake logistics only. Stripped from provider payloads server-side. |
| Created At / Updated At / Last Contact At | Timestamps; Last Contact drives stalled detection. |

## Activity (one row per event, per lead)

Timestamp, Lead ID, actor (person or system/feed name), event type (created, stage change, contact attempt, outcome recorded, merged, archived…), and a short detail string. This is the lead's history and the audit trail for automatic moves. No message bodies, no clinical content.

## Sources

The controlled Source list (name + whether it's a "system" source that manual add can't impersonate). The lead form's Source picker is type-to-search with add-if-missing (admin confirms new values into this tab, so the taxonomy grows deliberately, not by typo).

## Archive / Trash

- **Archive:** leads past their in-stage limit, row preserved verbatim + `Archived At`. Dashboard aggregates union Leads + Archive, so archiving never changes the numbers.
- **Trash:** soft-deleted leads (full lead row + its Activity snapshot, `Deleted At`, `Deleted By`). A daily sweep purges entries older than the grace period (default 7 days) — that's when deletion becomes permanent. Restore works any time before purge.

## Ingest Log

One row per inbox message the ingest job examined: timestamp, message ID, channel, subject, status (Created / Matched / Skipped + why), Lead ID. This is how you prove the hourly job is healthy — and how you debug the one message it skipped.

## Sync Log

One row per automatic write from any feed: timestamp, source system, event, matching key type, Lead ID, result (Created / Updated / Forward-only-held / Failed), short detail. **No names, emails, or bodies.** The admin's Sync Health panel reads this tab.
