# Bridge contract

The bridge is the safety boundary between a conversational model and the practice's booking system. Whether it is hosted in Apps Script, a cloud function, or the booking platform itself, preserve this contract.

## Endpoints

### `check_availability`

Input:

- `provider_id` — stable booking identifier;
- optional look-ahead window or date range;
- call language, when localized results or confirmations depend on it.

Success output:

- provider identity;
- a short list of genuinely open consultation slots;
- ISO start and end for each slot;
- a caller-friendly display label with the practice's display time zone.

Rules:

- Resolve weekly availability, date-specific hours, time off, calendar free/busy, existing bookings, buffers, caps, minimum notice, and booking window exactly as the booking backend does. Do not maintain a second, divergent availability algorithm if the backend can be called.
- Time-off and calendar precedence must be explicit and tested.
- If a required calendar cannot be read, return no slots with a machine-readable unreadable-calendar status. Never synthesize availability.

### `book_consult`

Input includes the chosen `provider_id` and `start` value returned by availability, plus only the caller fields the booking backend requires — typically name, email, phone, language, and service location.

The bridge or backend enforces:

- slot is in the future;
- slot is inside the booking window;
- minimum notice is satisfied;
- location and other hard-gate data are in the form the backend expects, with full jurisdiction names normalized to the backend's codes where needed;
- no duplicate active consultation for the same caller and clinician, under the practice's rule;
- no double-booking against confirmed bookings and calendar free/busy;
- clinician caps and buffers still pass at booking time, not only at availability time;
- required calendars are readable;
- integration configuration is present. If it is not, return a distinct `NOT_INTEGRATED` result rather than a false success.

Success output includes the booking reference and the exact clinician, start, end, and display label the agent may repeat.

Failure output uses stable codes plus a short caller-safe explanation. Record the code in the test or incident report; do not expose internal stack traces, endpoint URLs, or configuration details to the caller.

### `call_analyzed` webhook

Retell may send several call events. Log only the event that carries final structured analysis, unless the practice deliberately designs a different event model. Deduplicate on the vendor call ID so webhook retries do not create duplicate rows or duplicate notifications.

## Actual payload shape

Test functions with the payload Retell actually sends, not a convenient flattened approximation. In the reference implementation, Retell placed function arguments inside an `args` envelope alongside call metadata; a bridge that read only top-level fields returned “missing provider” errors even though the dashboard configuration looked correct.

The bridge should:

1. accept the documented/current Retell envelope;
2. normalize it in one place;
3. reject missing required fields with a clear code;
4. include an args-envelope case in its permanent regression tests.

If Retell changes the envelope, update the normalizer and tests together. Do not fix a live incident by making the prompt repeat fields in a second format.

## Authentication and secrets

- Every bridge route requires authentication appropriate to a public web endpoint — a long shared secret, signed request, or vendor-supported equivalent.
- Missing configuration fails closed.
- Wrong credentials return unauthorized and execute nothing.
- The same integration secret may need to exist in the bridge, booking backend, and Retell function/webhook configuration. Store the authoritative copy in a password manager or protected configuration location controlled by the practice.
- Never place the secret in source code, the agent prompt, the knowledge base, a call log, a test fixture with real credentials, or an ordinary report.
- Rotate the secret in one sitting across every location, then run the wrong-secret and happy-path tests. A partial rotation takes the line down.

## Call-log schema

Recommended columns:

| Column | Source or rule |
|---|---|
| Timestamp | Practice time zone |
| Call ID | Retell call identifier; deduplication key |
| From Number | Caller number, if the practice's privacy policy permits storing it |
| Duration (sec) | Retell's duration field, normalized |
| Cost (USD) | Retell's structured combined cost, normalized to dollars |
| Requested Clinician | Structured post-call field |
| Matched Clinician | Structured post-call field |
| Outcome | Structured post-call field |
| Existing-Client Request | Short structured category, not a clinical narrative |
| Attributed Clinician | Attribution rules below |
| Billed To | Practice overhead or the clinician/entity under the practice's cost policy |

Do not write transcripts, call summaries, recordings, diagnoses, or free-text clinical details into this log. If a post-call field can contain caller free text, constrain it to categories or review the privacy consequences before enabling it.

Verify cost units on the first analyzed call. If the logged cost differs from the Retell dashboard by an exact factor (commonly 100×), the payload's cents-versus-dollars interpretation is wrong. Fix the normalizer, correct the test row, and verify the next call.

## Optional admin notification

A per-call email can help a small practice notice failures quickly. Keep it operational:

- send only for a newly logged call, never for a deduplicated retry;
- include time, duration, cost, requested/matched clinician, outcome, and attribution;
- link to the call in the Retell dashboard rather than pasting a transcript or recording into email;
- send from a mail-capable, practice-owned backend; a bridge that does not need mail for its core job should not gain broad mail permissions just for notifications;
- isolate failures so a notification error never prevents call logging.

Make notifications optional. A busy group may prefer a dashboard and weekly digest instead of an email per call.

## Attribution and cost handling

Suggested attribution order:

1. clinician the caller requested;
2. clinician the caller was matched to;
3. clinician named in an existing-client request;
4. practice overhead.

Canonicalize names against the provider directory. A unique full name resolves. An ambiguous surname shared by multiple clinicians does not; leave it for the practice's designated resolver rather than assigning cost to the wrong person.

The practice chooses who is billed for attributed cost:

- solo practice: normally all overhead;
- group: all overhead, all attributed at cost, or a documented mix by clinician/employment model;
- unattributed and ambiguous calls: overhead unless the resolver assigns them.

If costs are passed through, reconcile monthly from the log: resolve ambiguous names first, total cost by billed-to party, and compare the total with Retell's billing for the period.

## Booking-backend handoff

The booking backend remains responsible for:

- creating the booking record;
- calendar event;
- manage/reschedule/cancel mechanism;
- client and clinician confirmation messages;
- CRM or lead creation, if the practice uses one;
- localized confirmation templates.

The bridge should call the backend's supported server-side action rather than imitating those side effects. If the backend has a human/PIN-gated manual-booking path, do not try to mint a human credential in the bridge. Add a separate, authenticated machine action with the same guards and creation tail.

## Test cleanup

Provide an authenticated cleanup or void method for test bookings. It must:

- target one booking by reference;
- be usable only for a booking created by the current test or audit;
- restore the slot;
- never become a general cancellation path for real client bookings.
