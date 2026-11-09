# Privacy and safety

Software settings support a compliance program; they do not certify one. The practice owner remains responsible for vendor review, workforce access, notices, and state or national requirements.

## Before live calls

- Execute a BAA with Retell for the production workspace.
- Review every other vendor in the path — telephony carrier or trunk, booking backend, bridge host, email notification sender, analytics, and any transcription or call-scoring add-on — and determine whether a BAA or another agreement is required.
- Use practice-owned accounts. Do not run a production receptionist from a clinician's personal Retell, phone, or cloud account unless the practice has deliberately accepted that ownership risk.
- Decide which staff roles may view live calls, recordings, transcripts, the call log, and the dashboard. Grant the minimum access each role needs.

## Data minimization

The receptionist needs enough information to answer public questions, match a clinician, book or route a consultation, and log an operational outcome. It does not need:

- clinical notes or histories;
- diagnoses or treatment plans;
- insurance member IDs for a normal intake call, unless the practice has a separately reviewed workflow that requires one;
- Social Security or tax identifiers;
- payroll, banking, credential, or contract data;
- another client's information.

Design prompts and post-call fields so callers are not invited to volunteer clinical detail. If a caller volunteers it anyway, the agent should redirect to logistics and avoid repeating sensitive detail back unnecessarily.

## Redaction, storage, and retention

Configure and read back:

- Retell's personal-information redaction categories;
- whether recordings, transcripts, and extracted fields are stored;
- workspace data-storage and retention settings;
- telephony carrier retention, if separate;
- call-log and dashboard retention;
- recording/transcript access and audit controls.

Choose categories based on the information the calls may contain. Names, phone numbers, and email addresses may be operationally necessary for booking and follow-up; that necessity should be a documented choice, not an accidental default. Do not weaken redaction as a routine troubleshooting step. If a third-party verification process sends a code through the receptionist and redaction masks it, stop and choose a safer verification route or obtain explicit owner approval for a time-limited exception with immediate restoration and verification.

## Recording and AI disclosure

Call-recording consent and AI-disclosure duties vary by jurisdiction and by whether the call crosses jurisdictions. Before launch, the practice should confirm:

- the opening disclosure, if any;
- whether consent is one-party, two-party, or governed by another rule for its calls;
- how a caller can reach a human or opt out of the automated path;
- whether directory or carrier rules impose additional wording.

Keep the agent's identity truthful under the approved wording. Never instruct it to deny being automated if asked in a context where denial would be deceptive or unlawful.

## Call log and dashboard access

- Store structured operational fields only.
- Restrict the workbook/database and any dashboard to practice administration and cost reconcilers.
- Do not use a public or “anyone with the link” view.
- Dashboard links back to Retell are preferable to copying transcripts into the dashboard.
- Review access when staff or contractors leave.

## Crisis safety

- Crisis resources are configured before the agent is published.
- The agent gives resources first and does not attempt counseling or a clinical risk assessment.
- A voice agent is not a crisis service. The practice's public pages and phone messaging should not imply that urgent messages left with the receptionist are monitored in real time unless they actually are, by named staff and a tested process.
- Test the crisis scenario in every launch language after any prompt change.

## Incident response

Prepare a one-page runbook with:

- how to detach the number or restore the prior phone route;
- who can disable the agent, bridge, or webhook;
- how to rotate the integration secret;
- who reviews affected call logs and Retell records;
- when callers or regulators must be notified under the practice's policies and applicable law;
- how to preserve the agent version, prompt, and logs needed to investigate.

Test the detach/restore path before launch. A receptionist the practice cannot turn off quickly is not ready for a main line.
