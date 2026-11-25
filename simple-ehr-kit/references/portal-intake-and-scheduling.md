# Client portal, intake, and scheduling

## Portal

- One personal link per client: `<portal-url>?t=<token>`. The token resolves server-side to exactly one ClientID. No accounts, no passwords.
- Portal shows: intake packet (until complete), upcoming appointments with the session's video link, invoices with payment links, superbills and any documents the provider has explicitly released, and the practice's policy/crisis copy.
- The portal never shows clinical notes by default (see clinical-notes.md), never lists other clients, and returns nothing for a guessed or revoked token.
- Revoke/regenerate a token from the client chart; the old link dies immediately. Token loss (client forwards their email, etc.) is handled by regeneration, and the limits of bearer links are disclosed to the practice up front.

## Intake packet

- Forms are rendered from definitions (fields like the note builder: text, choice, date, acknowledgement checkboxes for practice-authored policy/consent documents).
- A client can save partially and return on the same link; a form is only marked complete when its required fields and acknowledgements are present. **Blanks never overwrite existing chart values with emptiness** — a resubmitted form updates only fields the client actually filled, unless the form explicitly marks a field as a correction.
- On completion: responses are stored as a file in the client's Drive folder + an IntakeIndex row; key demographics sync to the Clients row by ClientID; the provider sees an "intake complete" flag on Today/chart, with no PHI in any notification email (name + "intake complete" inside the app only; email, if used, says only that a portal update is waiting).

## Scheduling

- The provider app is the scheduling surface in v1 (plus, optionally, a separate consult-booking system for *prospective* clients — that is a different kit's job; this EHR schedules established clients).
- Creating an appointment writes the workbook row and the Google Calendar event together; if the calendar write fails, the appointment is not half-created — the server reports the failure and writes nothing, or writes the row flagged `CalendarEventID = PENDING` and housekeeping retries/alerts. Pick one behaviour in Settings and test it.
- Each appointment carries its own video link, defaulting from the provider's default. The portal and the reminder read the appointment's link, so a one-off change never leaks into other sessions.
- Clients may, if the practice enables it, *request* a reschedule from the portal. A request changes nothing on the calendar; it flags the provider, who confirms or declines. Never let a portal request move a calendar event directly.
- Cancellations and no-shows are status changes on the row (with the practice's policy applied by the provider), not deletions — billing and the audit trail depend on the history.

## Reminders

- Email only, from the practice's sender alias, sent by an hourly trigger sweep for appointments inside the reminder window that have `ReminderSentAt` empty.
- Content is minimal: practice name, date/time **in the client's timezone, labelled**, and the portal link. No diagnosis, no note content, no invoice amounts in the reminder itself.
- A sent reminder stamps the row, so a re-run never double-sends. If an appointment moves, `ReminderSentAt` clears and the new time gets its own reminder.
