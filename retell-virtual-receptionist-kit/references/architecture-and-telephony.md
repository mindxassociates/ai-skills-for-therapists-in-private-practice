# Architecture and telephony

## Components

```text
Caller
  -> public number or directory tracking number
  -> Retell phone number / approved telephony route
  -> Retell agent (prompt + knowledge base + provider directory)
       -> availability / booking function
          -> secure bridge
             -> practice booking backend and calendars
             -> confirmation emails and lead/CRM hooks owned by the booking backend
       -> post-call analysis webhook
          -> secure bridge
             -> structured call log
             -> optional admin notification and call-log dashboard
```

Keep the responsibilities separate:

- **Retell** conducts the call and extracts structured outcomes.
- **The roster** supplies facts about clinicians and the practice.
- **The booking backend** owns calendars, availability rules, booking records, confirmation messages, rescheduling, and cancellation.
- **The bridge** translates between Retell and the booking backend, authenticates requests, enforces server-side guards, and logs analyzed calls.
- **The practice admin** owns routing changes, privacy settings, and review of failures.

## One front door

For a group, one central receptionist is usually simpler than one agent or number per clinician:

- callers who ask for a clinician can be matched directly;
- general callers can be matched by state, need, and preference;
- directory listings can retain separate public tracking numbers while sharing one backend destination;
- call volume and cost can be reviewed in one log.

A solo practice uses the same design with a one-person directory. Separate agents are justified only when the practices, languages, compliance boundaries, or booking backends are genuinely separate — not merely because there is more than one clinician.

## Phone-route choices

Choose the route with the practice owner before buying anything. Verify each option in the vendor's current documentation and dashboard; telephony features change.

| Route | How it works | Check carefully |
|---|---|---|
| Retell-purchased number | Buy a number in Retell and attach it to the agent | Carrier/region, monthly and minute cost, inbound/outbound use, SMS support, number ownership and release rules |
| Directory backend number | A directory shows its own tracking number and forwards to your receptionist number | The public number usually does not change; update and read back the backend destination on each listing |
| Forwarding from an existing line | The practice's current voice service forwards calls to the Retell number | Conditional vs. unconditional forwarding, caller ID behavior, voicemail conflicts, after-hours rules |
| SIP trunk or existing carrier | Connect an existing telephony provider to Retell | BAA coverage, codec and transfer behavior, SMS ownership, who troubleshoots failures |
| Porting | Move the practice number into the selected environment | Timeline, downtime, SMS migration, emergency-service records, and whether porting is reversible |

Do not choose a number primarily because it looks similar to an existing number. Decide in this order: reliability, BAA/compliance path, required functions, ownership/control, caller experience, then cost and appearance.

## SMS is a separate capability

A voice number does not necessarily send or receive texts. Before the prompt mentions texting, verify all four:

1. the number supports SMS in the relevant country;
2. the Retell plan or add-on enables it;
3. the agent has a tested send-SMS tool;
4. inbound texts, if promised, reach a monitored destination.

If any check fails, configure the verbal fallback: the receptionist gives the booking link or instructions aloud and offers the practice's ordinary web or email path.

## Transfers, voicemail, and fallback

An AI receptionist still needs an escape path. Decide and test:

- administrative escalation destination;
- what happens when the agent or bridge is down;
- whether a transfer is warm, blind, or not offered;
- where after-hours clinical-urgency callers are directed, consistent with the practice's policies;
- whether failed calls land in a human-monitored voicemail or callback queue.

Never configure a transfer destination from a clinician's personal number found online. Use only numbers the practice owner supplies and approves for publication to the agent.

## Booking integration choices

### Bridge to an existing booking backend — the reference design

Use this when the practice already has booking rules, multiple calendars, provider-specific limits, confirmation templates, or a CRM hook. The bridge contract in this kit is written for that case. Google Apps Script is one practical bridge host for Google Workspace practices, but the contract is host-neutral.

### Retell built-in tools or integrations

Retell's available tools change over time. A built-in calendar integration may be enough for a solo practice with one calendar and simple rules. Before relying on it, map it against the bridge contract: minimum notice, caps, duplicate detection, multiple calendars, time-off precedence, language-specific confirmations, failure behavior, and test cleanup. Any unmet item is either added server-side or accepted explicitly as a limitation.

### No live booking

Message-and-callback and information-only modes are valid pilots. The agent must know which mode it is in. Do not let it collect a preferred time in language that implies the time has been reserved.
