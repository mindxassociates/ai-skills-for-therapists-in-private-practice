# Operations and troubleshooting

## Routine monitoring

Choose a cadence the practice will actually keep — weekly during the first month, then at least monthly.

Review:

- call count, total minutes, and total cost;
- outcomes: booked, message taken, information only, existing-client request, failed gate, failed integration, abandoned;
- calls with no outcome or no attribution;
- average and outlier call cost;
- languages used and any language-specific failures;
- new real inquiry patterns the prompt does not handle;
- bridge errors and booking refusal codes;
- directory or website facts that changed without a corresponding agent update.

Use anonymized patterns to design new simulations. Do not paste real caller names, numbers, email addresses, or clinical details into test prompts or public issue reports.

## Optional call-log dashboard

A read-only admin dashboard over the call log can provide:

- date, clinician, outcome, and text-search filters;
- summary counts, minutes, and cost;
- totals by attributed clinician;
- a monthly billed-to rollup;
- a link from each row to the corresponding call in Retell.

Restrict it to practice administration. The dashboard should read the log, not become a second place where staff edit attribution. Correct attribution in the log or through the practice's documented resolver process, then let totals refresh.

## Change management

For every material change:

1. Capture the current agent version, prompt, function definitions, KB inventory, and bridge deployment/version.
2. Change the source fact first when a fact changed — roster before directory, directory before prompt.
3. Make the smallest prompt or code change that addresses the issue.
4. Re-run the affected bridge tests and simulations, plus the core crisis and confidentiality scenarios.
5. Publish or deploy by updating the existing agent/deployment rather than creating a parallel live route.
6. Read back the published state.
7. Record date, version, what changed, tests, and remaining limitations in the practice's change log.

Do not let a website crawl silently override a corrected roster fact. If the knowledge base refreshes from public pages, audit the changed pages before republishing the agent.

## Monthly cost reconciliation

1. Filter the call log to the month.
2. Resolve unrecognized or ambiguous attributed names.
3. Total duration and cost by attributed clinician and billed-to party.
4. Compare the log total with Retell's invoice or usage total for the same period; investigate material differences before deducting anything.
5. Apply pass-through deductions only under the practice's written cost policy.
6. Treat general, ambiguous, and practice-level calls as overhead unless the policy and resolver say otherwise.

## Troubleshooting

### The agent says a required field is missing

Check the payload shape before changing the prompt. Retell may wrap arguments in an `args` envelope. Reproduce with the exact dashboard payload, inspect the bridge normalizer, and add the case to regression tests.

### Availability returns slots, but booking refuses them

This may be correct. Minimum notice, caps, buffers, free/busy, duplicates, and slot races are checked again at booking time. Report the stable refusal code and caller-safe explanation. Change a rule only if the backend's result contradicts the practice's documented policy.

### The agent offers a clinician in the wrong jurisdiction

Separate name matching from jurisdiction matching. Confirm:

- the caller's physical location, not mailing address or phone area code;
- the directory jurisdiction list;
- full-name-to-code normalization in the bridge;
- whether a website/KB page contradicts the roster.

Fix the source fact, then test the same request in served and unserved jurisdictions.

### A valid service is refused

Test one gate at a time. Change only location, then only client type, then only age. Do not rewrite the provider's record based on the first failing combination; the wrong gate is easy to misidentify.

### Names are transcribed incorrectly

Add approved spoken variants, written forms, and romanizations to the directory. Require spell-back for email addresses and ambiguous names. If speech recognition repeatedly fails for a clinician's name, test alternate prompt wording that asks callers to choose from a short list or spell the name.

### A call is missing from the log

Check in order:

1. Did the call reach the analyzed state?
2. Did Retell send the expected event?
3. Did the webhook authenticate?
4. Did deduplication mistake it for an earlier call?
5. Is the log workbook/database reachable and writable?
6. Did a notification failure get mistaken for a logging failure? They should be isolated.

### Duplicate notifications or rows

The deduplication key is not being honored, or two webhook routes are active. Disable the duplicate route, keep one log writer, and verify with a repeated delivery of the same call ID in a test environment.

### Logged cost looks 100 times too high or low

Compare one call with the Retell dashboard. Correct the cents/dollars normalization, fix affected rows, and verify the next analyzed call. Do not bulk-adjust historical rows until the unit error's date range is established.

### Callers hear an old prompt after an edit

Check:

- Was the draft published?
- Is the phone number attached to the agent and version you edited?
- Did a settings-only publish change the version number without changing prompt content?
- Is a second agent or number still routed somewhere?
- Is the bridge endpoint still pointing at an older deployment?

Read back the live agent, number attachment, functions, webhook, and bridge deployment before concluding that Retell ignored the save.

### The bridge endpoint works locally but Retell calls fail

Compare method, content type, payload envelope, authentication placement, response shape, and timeout. Apps Script and similar hosts can redirect or reject requests in ways a local client tolerates. Test from a neutral HTTP client using the exact Retell-shaped request, without exposing the secret in the test report.

### The receptionist promises a capability it does not have

Remove the promise from the prompt, add the limitation section to the simulation battery, and verify the underlying route before restoring the language. Capability claims — SMS, transfer, voicemail, outbound callback, a language, live booking — each need their own test.

## Recurring audit

A scheduled audit is useful after launch:

1. Review the period's inquiry patterns and call-log anomalies.
2. Run availability checks for two clinicians using Retell's actual payload shape.
3. Confirm a wrong-credential request fails closed.
4. Run the core text-simulation battery.
5. Create, verify, and clean up one test booking.
6. Report counts, cost, pass/fail results, and proposed fixes.

The audit should diagnose by default. Prompt, bridge, privacy, and routing changes need the practice owner's approval unless the owner has granted a narrower standing permission in writing.
