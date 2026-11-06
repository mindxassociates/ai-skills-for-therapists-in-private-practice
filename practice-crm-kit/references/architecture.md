# Architecture

## Components

| Piece | Type | Notes |
|---|---|---|
| CRM workbook | Google Sheet, admin-owned, shared with nobody | Tabs: Leads, Activity, Sources, Archive, Trash, Ingest Log, Sync Log (see `data-model.md`) |
| CRM app | Apps Script web app, Execute as owner | Board + Agenda + detail + dashboard; the only human interface |
| Booking hook | Small upsert function in the booking system (or a token-checked POST endpoint on the CRM) | Fires on booking create/reschedule/cancel |
| Outcome write-back | Hook in the post-consult outcome form | Maps the outcome to a stage move |
| Form hooks | Hook in each front-door form (website contact, directory contact, service inquiry, client referral) | Create-or-refresh a lead from the form's structured fields |
| Inbox ingest | Hourly time trigger inside the CRM project | Rule-based parsing of directory-inquiry + answering-service mail in the practice inbox |

Everything runs under the practice's admin Google account. There is no external service, no runtime AI, and no separate database.

## Roles (enforced on the server)

| Capability | Admin | Provider | Solo owner |
|---|---|---|---|
| See leads | All | Own only (Matched Provider = them) | All |
| See Notes field | Yes | **Never — stripped server-side** | Yes |
| Edit stage / next action / due / last contact | All leads | Own leads | All |
| Edit identity fields, matched provider, notes | Yes | No | Yes |
| Quick-add a lead | Yes, any provider | Yes — forced to themselves, stage New, no Notes | Yes |
| Merge duplicates, archive now, delete | Yes | No | Yes |
| Bulk actions | Yes | No | Yes |
| Sync health / data quality panels | Yes | No | Yes |

Identity comes from the practice's provider roster (or a small built-in user list for a solo build): the gate verifies name + PIN server-side and returns a session token; **every** data call re-checks the token and applies the role filter. There is no "the UI hides it" security anywhere in this system.

## Data flow

```
booking ──upsert──▶ ┐
outcome form ──────▶ │
web/directory forms ▶ ├──▶ LEADS ──▶ board / Agenda / dashboard
inbox (hourly) ────▶ │        │
quick-add ─────────▶ ┘        └──▶ Activity (every change, per lead)
        every automatic write ──▶ Sync Log (no personal data)
stale sweep (daily) ──▶ Archive;  soft delete ──▶ Trash ──purge──▶ gone
```

## Why standalone

The CRM deliberately does **not** live inside a provider home page, a task board, or the booking system:

- Its data has its own sensitivity and retention shape; a separate workbook keeps the sharing boundary clean.
- Its feeds are small hooks in the *other* systems — each system stays the authority for its own event (booking owns bookings; the CRM owns the person-pipeline).
- Follow-ups belong to the lead, so they survive staff and tool changes; a task app would scatter them.
