# Architecture

## Components

| Piece | Type | Notes |
|---|---|---|
| Workbook | Google Sheet, script-account-owned, **shared with nobody** | Tabs: Clients, Assignments, ReminderInstances, Results, CustomExercises, Providers, Audit, Config (see `data-model.md`) |
| Apps Script project | One project, **one deployment**, two HTML views | `doGet` routes `?view=provider` to the provider app; anything else is the client app for `?slug=<item>` (or the index). Executes as the owner; clients need no Google login |
| Catalog | Data file in the project, generated from a source `catalog.json` | Content (items, steps, scoring-free content, categories) ships as server-side data; the workbook never stores catalog content. Custom exercises are the one exception — they live in the workbook |
| Client pages | Your public site (directory/portal) or the raw app URL | One page per catalog slug embedding the app in an iframe, passing the query string through; plus an index page and (optionally) the provider app embedded in your provider portal |
| Email | Script account via GmailApp, no-reply send-as alias | Reminder emails + rare admin notices only. The alias is checked at send time; if absent, mail goes from the account default and the admin is told at most once a day — never silently claim the alias was used |
| Triggers | 3 installable, created **once** by a one-time setup function | Engine every 15 min · recurrence expansion nightly · housekeeping nightly (watchdog + Sunday backup). The setup function does **not** de-duplicate — never run it twice |

## Data flow

```
provider ──name+PIN──▶ PROVIDER APP ──┐
                                      ├──▶ workbook (clients, assignments, instances, results, audit)
client ──token link──▶ CLIENT APP ────┘         ▲
visitor ──no token───▶ (self-guided, saves nothing)
engine (15 min) ──▶ due instances ──▶ email (client's language, client's timezone, assignment link)
housekeeping (nightly) ──▶ top-up instances · watchdog scan · (Sunday) workbook backup to Drive
```

- **Every server call is scoped on the server.** Provider functions take a session token and return only that provider's clients/assignments/results — filtering is never left to the client side. Client functions take the assignment token and return only that assignment's item, setup, and language.
- **The client file contains no provider code and vice versa.** Two separate HTML files; the client view physically cannot render a provider surface.
- **Reads that feed a screen return display-ready values** — text for dates, clean numbers for scores — because of the transport rule in `build-and-deploy.md`.

## Tokens and identity

- **Provider session:** the gate lists active providers by display name (the ID is the picker's invisible value — never render IDs or PIN material in the gate payload). `verifyProviderPin({providerId, pin})` checks SHA-256 hex of `ProviderID + ":" + PIN` against the stored hash; success returns a random 32-char session token. 5 failed attempts → 15-minute lockout, counted on the provider row.
- **Client assignment token:** 32 random characters per **assignment** (not per client, not per instance — every reminder email for an assignment carries the same link). Stored as a SHA-256 hash; all validation compares hashes. The plaintext is kept in one column of the restricted workbook because a recurring email cannot be built from a hash — see `security-and-privacy.md` for the honest framing. Ending an assignment kills the token. Tokens do not expire while the assignment is Active.
- **Completion attribution:** a submission credits the earliest open instance for the assignment (the sent one if one is outstanding, else the earliest pending one — clients often do the work early, from the copy-link or a previous email). See `reminder-engine.md`.

## Embedding and the passthrough lesson

Client pages live at hierarchical slugs — `<site>/exercises/thought-log`, `<site>/reminders/take-medication` — each a thin page whose only job is an iframe of the app for that slug. The token arrives as `?t=` on the **page** URL, so the page must forward its query string into the iframe `src`. Hard-won lessons from real CMS behaviour:

- Inline `<script>` in a page **body** may be stripped on save, and a "footer javascript" field may render as visible text instead of executing. The route that works across the tested CMS: a small script in the page's **head-tags** field that, on window load, appends `window.location.search` to the iframe's `src`.
- **Visible page furniture** (language pills, headings) belongs in static body HTML — head-script DOM injection is unreliable for elements that must be seen.
- After creating pages, run a **parity check**: every catalog slug has exactly one live public page (200, indexable), and every public exercise/reminder page maps back to a catalog slug — no orphans, no missing. Removals must delete both sides (catalog *and* page) and verify 404.

If the practice has no directory/CMS, the raw app URL works standalone — use it for testing, and link clients to it directly only if you accept the long URL.

## Design by audience

- **Client surfaces are public-facing**: flat, calm palette; large tap targets; 16px inputs (kills mobile focus-zoom); no native browser dialogs anywhere in either view (confirmations are in-page cards with explicit buttons, in both languages).
- **Provider surfaces** match wherever they live: if the app is embedded in a provider portal, copy that portal's header/design tokens; if standalone, keep the same calm system. One app, two skins is fine — never let the client view inherit portal chrome.
- **Buttons** show a busy state in the same instant as the tap and restore on success, failure, *and* dropped responses; failures render a short plain sentence near the control that caused them (a failure banner at the top of a long form is a failure the user never sees — see the troubleshooting table in `operations.md`).
