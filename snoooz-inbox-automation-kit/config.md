# Snoooz Inbox Automation — Configuration (Blank Template)

Fill this in with the practice before building any rule. Anything marked CONFIRM must come from the practice, for *this* practice specifically. Facts from another practice the clinician works with — a group, an agency, a platform — do not carry over on their own.

## Practice identity

- Practice display name: CONFIRM
- Practice name in second-language replies (if different from a translation of the display name): CONFIRM, or "translate the display name"
- Practice shape: CONFIRM (solo / small group — if small group, list each clinician whose inquiries the rules answer; each gets a profile in `references/provider-profile.md`)
- Inbox Snoooz is connected to: CONFIRM (the address directory and website leads actually arrive at)
- Reply-from alias Snoooz sends from: CONFIRM
- Contact email to give prospective clients who do not fit: CONFIRM
- Billing contact (email or person) billing questions route to: CONFIRM
- Existing-client contact route, if different from the inquiry inbox: CONFIRM, or "same inbox"
- Phone or voicemail number to give in EAP replies, if any: CONFIRM, or "none — email only"
- Website: CONFIRM
- Profile URLs to link in replies, per language: CONFIRM (one line per directory/profile page, per language if they differ)

## Booking

- Booking link, primary language: CONFIRM — one link, used in every primary-language rule
- Booking link, second language (if served): CONFIRM — if there is only one link, write "same as primary"
- Free consultation offered: CONFIRM (yes/no, length, format — phone or video)
- Free-consultation exceptions: CONFIRM (any client type or EAP whose clients do *not* get the free-consultation offer, or "none")
- Soonest-availability wording for EAP replies: CONFIRM a general line the practice is comfortable with (for example, "the soonest available appointment is usually the next business day") or "do not state any availability wording." Never name a specific time Snoooz cannot see.

## Clinical and business facts

Each clinician's full facts go in `references/provider-profile.md`. Confirm at practice level:

- Accepting new clients right now: CONFIRM (per clinician if they differ; if full, the waitlist wording the prompts should use — from the practice, not invented)
- Insurance panels for THIS practice: CONFIRM one by one, per clinician, with state limits stated inline (a state-suffixed panel means that state only)
- Self-pay rates for THIS practice: CONFIRM (initial evaluation and follow-up, per clinician if they differ)
- Sliding scale: CONFIRM (offered yes/no; floor if any; and whether the floor may be quoted in a reply — if "may not be quoted," prompts say sliding scale is discussed with the clinician and quote no number)
- Superbill offered for out-of-network clients: CONFIRM (yes/no)
- EAPs to build rules for: CONFIRM one by one, and for each: referral-style (send-ready) or availability-style (Draft only). Build a rule only for an EAP that actually sends this practice referrals by email.
- Directories to build rules for: CONFIRM (Psychology Today is the default; add another directory only when a real lead from it has arrived)
- Languages the rules serve: CONFIRM (one Psychology Today rule per language)
- Geographic exclusions: CONFIRM (any country or region whose located clients the practice does not accept, per clinician, or "none." Recorded in the gate blocks; mentioned in replies only when a sender explicitly asks about receiving services while located there)

## Signature

- Reply signature, primary language: CONFIRM (exact text, pasted into prompts as-is)
- Reply signature, second language (if served): CONFIRM

## Optional rules — a separate yes for each

- Google Voice text template rule: NO until the practice says yes, after reading the warning in `references/rule-recipes.md`
- Vacation auto-reply template rule: NO until the practice gives dates and wording
- Draft-first period for Psychology Today and Directories: CONFIRM how many days the practice wants to review drafts before any rule sends on its own
- Account working hours in Snoooz: CONFIRM (directory leads arrive at all hours; ask the practice's preference rather than assuming 24/7)
