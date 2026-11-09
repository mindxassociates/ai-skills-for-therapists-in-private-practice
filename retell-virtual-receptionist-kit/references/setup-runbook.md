# Setup runbook

Work in order. Do not change public routing until the final section.

## 1. Lock the design decisions

Record the answers from the setup interview in a setup sheet the owner can review:

- booking mode for the pilot;
- languages and voice;
- phone route and SMS decision;
- human fallback;
- crisis and emergency wording;
- booking backend and bridge host;
- call-log owner and admin viewers;
- optional per-call notifications;
- cost handling and attribution resolver;
- directory listings reserved for cutover.

Flag every unknown as a placeholder. An agent must not fill a gap by copying another clinician's facts.

## 2. Verify accounts and agreements

1. Create or confirm the Retell workspace under a practice-owned account, with strong authentication and recovery controlled by the practice.
2. Execute Retell's BAA before live client calls if the practice will use Retell for health-care calls. File the signed agreement with the practice's vendor records.
3. Repeat the BAA check for any separate carrier, trunk provider, booking vendor, or add-on that will handle protected health information.
4. Confirm who can administer Retell, the telephony route, the bridge, and the booking backend. Remove test or personal accounts that should not retain access.
5. Set data-storage, retention, and redaction choices now, following `privacy-and-safety.md`, so test calls use production-like settings.

## 3. Compile the provider directory

Build the directory from the named source of truth, not from memory or marketing copy alone. Use the schema in `prompt-and-provider-directory.md`.

For each clinician, the owner or roster maintainer confirms:

- display name and credentials;
- alternate names, pronunciations, and non-English names where relevant;
- states or other jurisdictions served;
- age groups and client types;
- specialties and populations;
- spoken languages;
- published self-pay rates;
- contracted panels used for matching;
- accepting status and future start dates;
- booking link or provider identifier used by the backend;
- exceptions that change the standard offer.

Resolve contradictions before writing the prompt. If a website bio and roster disagree, the roster wins only if the interview named it as the source of truth; otherwise stop and ask the owner.

## 4. Prepare the knowledge base

Use public, practice-approved material only:

- public practice and clinician profile pages;
- services, fees, insurance, telehealth, and FAQ pages;
- the compiled provider directory;
- public policies the receptionist is expected to state.

Audit imported or crawled pages for stale clinicians, superseded fees, contradictory license states, and pages that invite callers to submit clinical information to the wrong channel. The agent should say it does not have a fact rather than reconcile contradictions by guessing.

## 5. Build the Retell agent

1. Create one agent for the practice unless the architecture decision says otherwise.
2. Configure the approved languages and voice. Test accented speech, clinician names, state names, dates, and email addresses in every launch language.
3. Load the prompt sections from `prompt-and-provider-directory.md`:
   - identity and opening;
   - practice facts;
   - provider matching and gates;
   - insurance and fees;
   - booking-flow precedence;
   - existing-client handling;
   - crisis;
   - confidentiality;
   - name confirmation;
   - capability limitations and fallback.
4. Add the knowledge base and provider directory.
5. Add only tested tools. For live booking, add availability and booking functions pointing to the bridge. Add transfer or SMS tools only when their routes are ready.
6. Configure post-call analysis fields the call log needs:
   - requested clinician;
   - matched or preferred clinician;
   - outcome;
   - existing-client request;
   - booking result or reference, if the backend returns one.
   Keep fields structured and non-clinical.
7. Save a restore point: export or copy the prompt, function definitions, tool list, knowledge-base inventory, and agent settings before publication.

## 6. Build the call log

Create a practice-owned spreadsheet or database with the columns in `bridge-contract.md`. The bridge creates or verifies the log structure on first use where practical.

Access rules:

- practice admin and the people who reconcile cost or investigate failures only;
- no broad sharing link;
- no transcripts, summaries, recordings, diagnoses, or session content pasted into the log;
- a retention rule the owner chooses and documents.

Optional: build a read-only call-log dashboard over the same data for filtering and provider totals. The dashboard is a viewer, not a second source of truth.

## 7. Build and deploy the bridge

Follow `bridge-contract.md`. In outline:

1. Create the bridge in a practice-owned environment.
2. Store its shared secret in the bridge and booking backend's protected configuration — never in code, the prompt, a spreadsheet cell, or chat.
3. Give the bridge only the permissions it needs. A bridge that only reads calendars/availability and writes a structured log should not also send mail. If admin email notifications are wanted, let an existing mail-capable backend send them, or scope and test a separate notification step deliberately.
4. Deploy to a stable endpoint. Record the deployment/version process so updates do not silently change the URL Retell uses.
5. Run the setup self-check: configuration present, calendars readable, log writable, booking endpoint reachable, wrong-secret request rejected.
6. Register the availability, booking, and webhook endpoints in Retell. Keep the exact function schemas and the agent's tool descriptions aligned with the bridge contract.

## 8. Publish a testable agent version

1. Publish the agent version intended for testing.
2. Reopen the agent and read back the published version, prompt, tools, function URLs without exposing secrets in your report, post-call fields, and privacy settings.
3. Attach the test phone number to that agent.
4. Confirm the number's inbound and outbound behavior and any SMS limitation.

A saved draft is not a live agent. A settings-only publish can advance the version without changing prompt content; report which one changed.

## 9. Test before cutover

Run all of `testing-and-go-live.md`. The minimum bar:

- bridge unit or harness tests pass;
- function tests use Retell's actual payload envelope;
- the text-simulation battery passes in every launch language;
- one test booking is created, verified in the backend and notifications, then cleaned up through the approved method;
- a wrong-secret request fails closed;
- a simulated bridge outage produces the chosen fallback, not a false booking.

## 10. Cut over one route at a time

For each directory listing, website number, forwarding rule, or main line:

1. Record the current destination and owner.
2. Change only that route to the receptionist.
3. Save and read it back.
4. Place or simulate the approved verification check for that route.
5. Keep the prior route documented and recoverable until the practice accepts the new route.

Do not announce completion from a settings save alone. The route is complete when it has been read back and exercised.
