# Clinical notes — builder, carry-over, sign-and-lock

## Custom note builder

A template is a list of fields. Field kinds: short text, long text, single choice, multi choice, rating/scale, date, and a fixed-text block (instructions or standard language the practice authors). Each field has: key, label, required?, and **carry-over?**.

- Templates are data (see data-model), edited in the provider app's template editor: add/reorder/retire fields without touching code.
- Retiring a template never deletes it — signed notes must remain interpretable against the template they were written on. Retired = not offered for new notes.
- Clinical wording belongs to the practice. The kit ships field *structure* examples (a generic progress note: subjective / interventions / response / plan; a generic assessment outline) with placeholder prompts the practice must replace with its own language before use.

## Writing a note

1. Start from the appointment (client, provider, date of service pre-filled by ID) or from the client chart.
2. **Carry-over:** one click copies the previous signed note's carry-over fields (e.g. ongoing plan, risk status, standing interventions) into the new draft. Only fields flagged carry-over copy; session-specific fields always start blank. The provider edits before signing — carry-over is a starting point, and the UI labels copied text as copied until edited.
3. Drafts auto-save to the note's Drive file. A draft is visible only to its provider (and the practice admin, per the disclosed admin access).

## Sign and lock

- Signing is an explicit action with a confirmation. On sign: the server renders the final note file, computes its content hash, writes `SignedAt`/`SignedBy` to the index, and freezes the file (no further writes accepted by any server function).
- A signed note is **never edited**. A correction or late addition is an **amendment**: a new file + index row pointing at the original (`AmendmentOf`), dated and signed the same way, displayed with the original in the chart.
- Unsigned-note hygiene: the Today view and a weekly housekeeping report list drafts older than the practice's chosen threshold (e.g. 7 days) per provider — IDs and dates only in any email, never content.

## Treatment plans and reviews

Model a treatment plan as just another template (goals, objectives, review date), with the review date surfaced on the client chart when it passes. Do not build a separate planning subsystem.

## What notes are not

- Not a prescribing, lab, or orders system.
- Not shared with the client by default. If a practice chooses to release a note or summary to the portal, that is an explicit per-document provider action, audit-logged — never an automatic portal feed.
