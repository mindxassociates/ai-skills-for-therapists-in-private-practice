# Architecture

## Components

| Piece | Type | Notes |
|---|---|---|
| Portal workbook | Google Sheet, admin-owned, **shared with nobody** | Tabs: Clients, Providers, Externals, Threads, Messages, Attachments, AuditLog, Settings |
| Attachments folder | Google Drive folder, admin-owned, **shared with nobody** | One subfolder per thread; files created unshared |
| Portal app | Apps Script web app, Execute as owner | The only surface clients/externals/providers use |
| Admin console | Second Apps Script web app, admin-only gate | Same workbook, same admin PIN; people/threads/audit/settings |
| Email | Practice Google account (no-reply alias) | Codes, invitations, alerts, content-free notifications only |

Workbook and folder IDs live in the portal project's Script Properties, set by the one-time boot function that creates both — a fresh build has no hard-coded IDs, and the admin console receives the workbook ID as its config.

## Data flow

```
client ──email+code──▶ ┐
provider ──name+PIN──▶ ├──▶ PORTAL APP ──▶ workbook (people, threads, messages, audit)
external ──email+code─▶ ┘            └────▶ Drive (attachment files, unshared)
                                          └────▶ email out: codes + content-free notifications only
admin ──name+PIN──▶ ADMIN CONSOLE ──▶ same workbook
triggers: hourly cleanup (sessions/codes) · daily retention sweep (if enabled)
```

- **Reads/writes** all pass through the app's server functions, which verify the session and scope the payload to the caller's participation — every call, no exceptions for "internal" endpoints.
- **Notifications** are sent after a message saves, from the practice's sender alias, in the recipient's known language when the practice is bilingual (otherwise the practice's default; bilingual when unknown is a safe fallback).
- **Roster sync (optional):** if the practice keeps a provider roster, a timed sync adds new providers (blank PIN — they set it at first sign-in) and disables departed ones. It never touches existing PIN hashes or sessions.

## Why two projects

The admin console has a different audience, a different risk surface, and a slower change cadence than the portal. Separating it means portal work never risks the oversight tools, and the console can be deployed at a less-discoverable path. They deliberately share the workbook and the admin's PIN (one credential, verified against the same stored hash) so administration isn't a second account to manage.
