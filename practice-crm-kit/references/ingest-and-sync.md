# Ingest and sync — how leads arrive

Four feeds, one discipline: **upsert by the matching order, move stages forward only, log every write to the Sync Log, and never let a CRM failure break the source system.**

## Matching order (all feeds)

1. **Lead ID** — if the event carries one (a deep link, a form field), match on it, with an ownership sanity check (the lead's provider should match the event's provider; mismatch = log and stop).
2. **Email** — exact, case-insensitive.
3. **Phone** — digits-only comparison.
4. **Name + provider** — last resort; log it as a weak match so a human can eyeball it in Data Quality.

No match → create (stage per the event: an inquiry = New; a booking = Consult Booked). Multiple matches → prefer the most recently updated active lead; log the ambiguity.

## Forward-only stage rule

Rank the pipeline stages. An automatic event may advance a lead or fill in fields, but never move it backward: a rescheduled-booking event landing on a Started lead updates the consult fields and logs `Forward-only-held`; it does not resurrect the lead onto the active board. Exits are sticky for automation — only a human moves a lead out of an exit stage.

## The feeds

### 1. Booking upsert

On booking create / reschedule / cancel, the booking system calls the CRM's upsert (a shared helper in the booking project, or a token-checked POST to the CRM) with: name, email, phone, language, state, payor, concern category, provider, consult time, booking ID. Result: lead created at Consult Booked (or matched lead advanced to it). The hook is wrapped so **any failure is caught, logged, and the booking proceeds**.

### 2. Outcome write-back

The post-consult outcome form carries the Lead ID (deep link) or the provider + client identity. On submit, it maps the outcome to a stage — e.g. "intake booked" → Intake Sent (or Started, per practice), "will schedule later" → Consult Held + a follow-up due date, "not a fit" → Not a Fit — and stores the verbatim outcome on the lead. The same shared sync helper pattern as the booking hook, so every front-door system writes the same way.

### 3. Front-door forms

Website contact, directory contact, service inquiry, and client-referral forms create-or-refresh a lead from their **structured fields only** — the message body is not copied (it lives in the inbox/form responses, linked not duplicated). Inquiry types the practice excludes from the pipeline (e.g. clinician supervision inquiries) create no lead; the helper checks the inquiry type first.

### 4. Inbox ingest (hourly trigger)

Reads the practice inbox for two known channels:

- **Directory inquiry notifications** (e.g. Psychology Today–style emails) — parse the structured parts (inquirer name, the profile/provider it came through, stated payor/location when present in the standard layout).
- **Answering-service summaries** (e.g. Smith.ai–style call notes) — only messages the service itself marks as a new lead become leads; a summary without that mark is logged `Skipped` and creates/matches nothing.

Everything else is ignored. Every examined message gets an Ingest Log row (message ID, channel, status, Lead ID) — the log is how you prove the job ran and why a given message did or didn't become a lead. Parsing is **rule-based on sender + subject + known field layout**; when a channel changes its email format, ingest degrades to Skipped rows, never to garbage leads — and the Sync Health panel makes the change visible.

## The shared sync helper

Build the upsert logic **once** as a small canonical code block (matching, forward-only rule, Sync Log write, result object) and copy it into each feeding project, versioned (e.g. `crm-sync-core v2`). Each carrier keeps its own field mapping to the canonical payload. When the core changes, update every carrier in the same pass and note the version in each — copied code that drifts silently is worse than no sharing.

## Sync Log contract

Every automatic write — success, weak match, forward-only hold, or failure — appends: timestamp, source system, event, key type used, Lead ID (or blank), result, one-line detail. **No names, emails, phones, or bodies.** If a write fails, the log row is the alert; check it in the admin Sync Health panel as part of a weekly rhythm.
