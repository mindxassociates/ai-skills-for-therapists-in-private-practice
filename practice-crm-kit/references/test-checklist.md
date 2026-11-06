# Test checklist

## Permission tests (do these first, as two different providers + admin)

- [ ] Provider A's board, Agenda, and search show only A's leads.
- [ ] Provider A fetches provider B's Lead ID directly → same response as a nonexistent ID.
- [ ] Provider A's payloads (inspect the raw response, not just the page) contain **no Notes field** on any lead.
- [ ] Provider A attempts a write to B's lead, and an admin-only field on their own lead → refused server-side.
- [ ] Provider self-add creates a lead matched to themselves at New, with Notes dropped and system sources refused.
- [ ] Signed-out / expired token: every data call returns only a sign-in response.
- [ ] The workbook's Share dialog shows the owner only.

## Board and lifecycle

- [ ] Drag a card → stage changes, Activity row written, Undo toast reverts it; undo after someone else moved the lead again does **not** revert (guard works).
- [ ] Column counts are true counts while the preview is capped.
- [ ] A lead idle in stage past the limit archives on the sweep; dashboard totals are identical before and after.
- [ ] A Started lead does **not** archive at the generic limit; it archives at the started rule (past-consult window).
- [ ] Delete → lead in Trash with its Activity; restore works; a Trash entry past the grace period purges on the sweep and is unrecoverable.
- [ ] Duplicate pair surfaces in Data Quality; merge keeps the survivor's Lead ID, preserves both Activity histories, and the loser leaves via Trash.

## Feeds (one real event each)

- [ ] Real booking → lead at Consult Booked with consult time + Booking ID; Sync Log row present. Break the CRM hook deliberately (bad token in a test copy) → booking still succeeds; failure is in the log.
- [ ] Outcome form submit → stage moves per the mapping, verbatim outcome stored, follow-up due date set where the mapping says so.
- [ ] Each front-door form → lead created-or-refreshed from structured fields; the message body appears **nowhere** in the CRM; an excluded inquiry type creates no lead.
- [ ] Inbox ingest: a real directory inquiry creates/matches a lead; an answering-service summary **without** the new-lead mark creates nothing and logs Skipped; every examined message has an Ingest Log row.
- [ ] Forward-only: replay an old booking event against a Started lead → fields update or hold, stage does not move backward, log says so.
- [ ] Matching: same person via a second channel (same email) → matched, not duplicated; same name + same phone, different email → matched at the phone step and logged as such.

## Agenda habits

- [ ] A consult whose time passes with no outcome appears in Awaiting Outcome; one tap records the outcome and clears the row.
- [ ] An Intake Sent lead past the stalled window shows the stalled marker; recording contact clears it.
