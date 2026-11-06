# Board and views

## Board (the home screen)

- Kanban columns = pipeline stages, in order; exit stages get their own visually quieter columns (or a collapsed exits row — keep exits visible but out of the way).
- Each card: name, source, matched provider, payor, consult time if booked, next action + due state (overdue is unmistakable), days-in-stage.
- Column preview cap (e.g. first 5 cards + "View more") so a busy practice's board stays fast; the column header shows the true count.
- Drag to move stage — with an **Undo** toast after every move (the undo is guarded: it only reverts if the lead is still in the stage the move put it in). Select mode for bulk stage change / archive / delete (admin), reporting partial success honestly per lead.
- Filters: provider, source, stage, due state, text search. A provider's board is pre-scoped to their leads by the server — the filter can narrow, never widen.

## Agenda

The daily working list, across leads:

- **Follow-ups due** — overdue first, then due today, then upcoming, from each lead's Next Action Due.
- **Awaiting outcome** — leads in Consult Booked / Consult Held whose consult time has passed with no outcome recorded, with **one-tap outcome buttons** (Started intake / Will schedule / Not a fit / No-show…) that record the outcome and move the stage in one action. This row is where consult data goes to die in most practices; make it one tap or it won't happen.
- **Stalled intakes** — leads in Intake Sent with no movement for a practice-set window (default 14 days) get a visible marker.

## Lead detail

- All fields (role-permitting), the Activity history, and the actions: update stage, set next action + due, record a contact attempt (stamps Last Contact At), archive now (admin), delete (admin, soft).
- A **deep link** (`?lead=CRM-####`) opens the detail directly after sign-in — other systems (booking follow-up emails, a messaging portal, the outcome form) link here instead of building their own lead views. The link only works if the signed-in user is allowed to see that lead.

## Dashboard (admin)

- Counts by stage, by source, by provider; conversion between stages over a period; consults held vs. outcomes recorded.
- Aggregates **union Leads + Archive** — archiving is housekeeping, not a statistic change.

## Admin panels

- **Needs attention:** awaiting-outcome count, stalled intakes, follow-ups overdue — the exceptions, not the whole board.
- **Data quality:** likely-duplicate pairs (same email, or same name+phone) with a merge action (survivor keeps its Lead ID; the loser's Activity is preserved on the survivor; the loser leaves through the soft-delete path).
- **Sync health:** recent Sync Log rows — which feeds wrote, matched, held forward-only, or failed — with **no personal data** in the panel.
