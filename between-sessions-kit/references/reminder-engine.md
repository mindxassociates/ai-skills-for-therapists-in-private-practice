# The reminder engine

## Recurrence model

An assignment's plan is one object; a one-off is just a preset of the same expander (there is no separate code path):

```json
{ "kind": "once | daily | weekly-days | every-n-days | custom-dates",
  "daysOfWeek": [1, 3, 5], "intervalDays": 3,
  "customDates": ["2026-12-01"],
  "timesOfDay": ["07:00", "12:00", "20:00"],
  "endRule": "None | ByDate | AfterOccurrences",
  "endDate": "2027-06-30", "occurrences": 40 }
```

Horizon: up to ~1 year. Multiple times per day are first-class. A custom message on the assignment overrides the system template (template variables: first name, item name, link — only those).

## The client's timezone governs

Assignment dates and times are **wall times in the client's zone**. At materialisation, each wall slot converts to an unambiguous epoch (stored on the instance) using a DST-correct conversion — a weekly 7:00 PM Pacific slot stays 7:00 PM Pacific across the spring-forward, while its UTC instant shifts an hour. Provider surfaces (wizard summary sentence, Reminders Summary, Review timestamps) render times **in the client's zone and label the zone** ("2026-11-23 19:00 PST"). A client with no stored zone resolves to the practice zone — pre-timezone behaviour preserved exactly for legacy rows.

## Materialisation: the 60-day window + nightly top-up

Instances are rows, written ahead — but **not** the whole series at creation:

- At creation, materialise only slots dated within the next **60 days** (client-zone calendar), in **one bulk range write** for the whole batch.
- The result shown to the provider states both numbers: how many are scheduled now **and** the full series total ("61 of 371 in the full series — the rest are added automatically as their dates approach"). Never let the capped count read as the total.
- The nightly expansion walks the window forward: occurrences are counted from the series start, so top-ups land in exact order — no gaps, no duplicates, nothing past the end rule. Paused and Ended assignments are never topped up. The walk is idempotent (AssignmentID + ScheduledEpoch is the uniqueness key), so a re-run creates nothing.
- The seam is testable and must be tested: walk a daily 200-occurrence series across several window positions and assert the final set is contiguous with unique epochs; walk a weekly series across a DST boundary and assert wall time pinned, instant shifted.

Why: creating a daily-for-a-year assignment naively is ~370 individual append calls and minutes of "Creating…" — long enough that providers conclude the button is broken and click again (see the duplicate-assignment incident in `operations.md`).

## Sending

A time-driven trigger runs the engine **every 15 minutes**: select instances with `ScheduledEpoch <= now`, `Status = Not started`, assignment Active, client Active, client email non-blank.

- **Covered-work guard first:** before sending, check whether a Result already covers this assignment's work (the crediting rules below). If covered, mark the instance `Completed`, link the result, send nothing.
- Send via GmailApp from the no-reply alias when present (checked live per run), else the account default + the once-a-day admin notice. The email is entirely in the client's language — subject, body, footer, never mixed — as branded HTML with a plain-text fallback, containing the item name and the assignment link. **No answer data ever appears in email.**
- On success: `Status = Sent`, `SentAt` set. On failure: stays `Not started`, `ErrorNote` written, retried next run; after 4 failed attempts → `Failed` + audit entry. A quota guard stops the run cleanly when daily mail quota approaches — progress is persisted per instance, so a stopped run resumes safely.

## Crediting: early submissions

Clients do homework early — from the copy-link, or an earlier email. The submission path therefore credits an instance at save time:

- If a `Sent` instance is outstanding, it flips to `Completed` (the classic path).
- Else the **earliest pending** instance flips to `Completed` and links the result.
- The dashboard math follows: adherence = Completed ÷ Sent at read time, and fully-done work reads 100%, not 50%-because-one-instance-was-never-sent.
- Legacy results saved before this rule existed (no instance link) are handled by the engine guard above: when the engine reaches their instance, it finds the covering result, marks the instance Completed, and backfills the link — it never emails.

## Affirmations

Affirmation assignments place each occurrence on a random day/time inside its week window (`RandomSlot = Y`), materialised like any other instance so the Summary still shows them. There is no Completed state — an affirmation is sent, not submitted.

## Adherence and the dashboard

Provider dashboard cards, computed at read time (no stored counters to drift): Total Reminders, Overall Adherence Rate (Completed ÷ Sent), Total Clients, Flagged Results (unreviewed only — the count that also drives any portal bell). Marking a result reviewed is the single stamp that clears the dashboard card, the review queue, and the bell together.
