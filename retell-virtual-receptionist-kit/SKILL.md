---
name: retell-virtual-receptionist-kit
description: "Set up a Retell AI virtual receptionist for a solo or group therapy practice: one front-door phone line, roster-based provider matching, optional multilingual behavior, live consultation availability and booking through a secure bridge to the practice's booking backend, structured post-call logging, call-cost tracking, privacy and crisis guardrails, free-first testing, and one-route-at-a-time directory or main-line cutover. Use when a therapist wants to build, configure, test, launch, maintain, or troubleshoot a Retell receptionist or connect Retell to an existing booking system."
---

# Retell Virtual Receptionist Kit

Build a phone receptionist around the practice's real systems rather than letting a voice model improvise. Retell handles the conversation; the practice's roster controls the facts; the booking backend controls availability and booking; a small bridge connects them and records a structured, non-clinical call log.

## What “done” means

A completed setup has:

1. A Retell workspace and agent owned by the practice, with the production BAA verified before live client calls.
2. A phone route the practice controls, with SMS, transfer, voicemail, and outbound capabilities stated only after each has been verified.
3. A provider directory generated from the practice's source of truth — one entry for a solo practice, one per clinician for a group.
4. A prompt that applies the practice's hard gates before it invites a booking and uses insurance only as a soft matching fact.
5. If live booking is enabled, a bridge whose server-side guards have passed tests in Retell's actual function-payload shape.
6. A structured call log with duration, cost, outcome, and attribution — and no transcript or clinical content copied into it.
7. A passed simulation and end-to-end booking battery, followed by one-at-a-time routing changes that were read back after saving.

If any item is missing, report the receptionist as a pilot in the booking mode that actually works: live booking, message-and-callback, or information-only.

## Setup interview (ask once, before building)

1. **Practice shape** — solo or group; legal practice name; countries, states, and time zones served; practice hours; who owns the Retell, telephony, and booking accounts.
2. **Callers and languages** — prospective clients, existing clients, referral sources, billing callers, or all of these? Which languages must the agent speak, and which facts or scripts need human-reviewed translation?
3. **Source of truth** — where do provider licenses, ages, client types, specialties, panels, fees, accepting status, and exceptions live now? Name one source that wins when websites or directory profiles disagree.
4. **Booking mode** — live booking, message-and-callback, or information-only for the pilot? What consultation length, booking window, minimum notice, buffers, caps, and cancellation/reschedule paths apply?
5. **Booking backend** — what system owns calendars and confirmations today? Can it expose a secure server-side endpoint, or must the agent use one of Retell's current built-in integrations? Who receives confirmation and failure notices?
6. **Phone route** — new Retell number, existing number, directory tracking numbers, call forwarding, SIP trunk, or porting? Which public numbers stay unchanged? Is SMS genuinely required, and has the selected route been verified to support it?
7. **Human fallback** — where do urgent administrative calls, repeated failures, accessibility requests, and “let me speak to a person” requests go? A tested transfer number, voicemail, callback queue, or published human line?
8. **Crisis policy** — country-specific crisis and emergency numbers, exact wording, and whether the agent should attempt a warm transfer if the practice has a tested route. Default in the US: 988 and 911, no counseling.
9. **Privacy choices** — Retell data-redaction categories, storage and retention settings, call-recording notice or consent requirements in the practice's jurisdictions, who can see recordings/transcripts, and whether admin notifications are wanted.
10. **Existing-client scope** — may the receptionist take reschedule/cancel requests directly, capture a message, direct callers to the client portal/EHR, or some combination? It must not discuss treatment either way.
11. **Cost handling** — solo practices usually absorb all minutes as overhead. Groups choose: all overhead, all attributed at cost, or a documented mix by clinician or employment model. Who resolves an ambiguous attribution?
12. **Directory routes** — list every listing or line that will eventually point to the receptionist: therapist directories, practice website, Google Business Profile, main office number, or voice-service forwarding. These change only at cutover, one by one.

## Hard rules

1. **Facts come from the source of truth.** Never invent or infer a license, state, panel, fee, age group, client type, language, exception, or accepting status. A nearby state, similar specialty, or similar-sounding name is not a substitute.
2. **Hard gates before booking.** Check the caller's physical location, age group, client type, provider accepting status, and format before offering a consultation. Insurance is soft: name only a panel the selected clinician actually has, never estimate a copay, deductible, authorization, or claim outcome, and keep the private-pay path visible.
3. **The backend owns availability.** Offer only slots returned by the booking system. Say a consultation is booked only after an explicit success response. If the integration fails or is not configured, use the chosen fallback — never a verbal promise that sounds like a booking.
4. **Booking rules live server-side too.** Minimum notice, booking window, duplicate active consultations, double-booking, caps, buffers, and unreadable-calendar behavior are enforced by the bridge/backend, not merely requested in the prompt.
5. **Crisis before intake.** On a crisis disclosure, give the configured crisis and emergency resources first, do not counsel, and do not lead with booking.
6. **No clinical access.** The receptionist and bridge do not retrieve diagnoses, notes, treatment plans, another client's schedule, or internal financial, tax, payroll, credential, or system data. Refusals neither confirm nor deny underlying information.
7. **No transcript in the operational log.** Log structured fields only: time, call ID, caller number if the practice's privacy policy permits it, duration, cost, requested/matched clinician, outcome, and billing attribution. Recordings and transcripts stay in Retell under the practice's access and retention settings.
8. **Capabilities must be tested, not implied.** Do not promise SMS, transfer, voicemail, outbound callbacks, or a language the configured agent and phone route have not demonstrated.
9. **Identity must stay truthful.** The agent introduces itself with the practice-approved title — “the virtual receptionist for [Practice Name]” is the pattern — and never claims to be human. Follow the practice's legal and platform requirements for AI and recording disclosure.
10. **Cut over last and one route at a time.** A directory listing, website number, or main line changes only after the test battery passes. Read the saved route back; keep the prior human route recoverable until the new route is proven.

## Build order

1. **Decisions and compliance** — interview, booking mode, telephony route, BAA status, privacy settings (`references/architecture-and-telephony.md`, `references/privacy-and-safety.md`).
2. **Provider directory and prompt** — compile the directory, then build the prompt sections in `references/prompt-and-provider-directory.md`.
3. **Retell agent** — languages, voice, knowledge base, tools, post-call analysis fields, and approved fallback behavior.
4. **Bridge and call log** — implement the contract in `references/bridge-contract.md`; if using a built-in Retell integration instead, map every contract requirement to it and test the gaps.
5. **Testing** — bridge tests, dashboard text simulations, one verified test booking and cleanup (`references/testing-and-go-live.md`).
6. **Cutover and operations** — route one listing or line at a time; monitor costs and failures; run the recurring audit in `references/operations-and-troubleshooting.md`.

## Reference files

- `references/architecture-and-telephony.md` — components, phone routes, directory forwarding, and integration choices
- `references/setup-runbook.md` — the ordered build, from accounts and facts to publication and cutover
- `references/prompt-and-provider-directory.md` — directory schema, prompt sections, matching gates, and multilingual/name rules
- `references/bridge-contract.md` — availability, booking, webhook, call-log, security, and cost-attribution contract
- `references/privacy-and-safety.md` — BAA, redaction, retention, recording, crisis, and access rules
- `references/testing-and-go-live.md` — free-first test battery, end-to-end booking proof, and cutover checklist
- `references/operations-and-troubleshooting.md` — monitoring, optional call-log dashboard, maintenance, and failure diagnosis
