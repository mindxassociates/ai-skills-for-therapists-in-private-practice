# Setup Checklist — Start Here

Work top to bottom. Do not skip the verification steps — in the group workspace this pattern came from, prompts reverted and saves looked complete when they were not, and the reopened rule was the only proof.

## 1. Interview (about 10 minutes)

- Open `../config.md` and ask the practice for every CONFIRM field. Ask in small groups: practice identity and emails first, then booking, then panels and rates for *this* practice, then the optional rules.
- Fill `provider-profile.md` with the answers as you go (one profile per clinician) and read the changes back before building.
- Confirm whether each clinician is accepting new clients today. If someone is full, the prompts invite a waitlist reply instead of a booking, and that wording comes from the practice, not from this kit.

## 2. Account

- Open app.snoooz.ai in the browser and sign in with the practice's Google account using Sign in with Google. There is no Snoooz password to find or save.
- Connect the inbox named in config and confirm the reply-from alias.
- Set the account working hours with the practice. The group practice ended on 24/7 because directory leads arrive at all hours and the hours setting could not be restricted to non-working hours alone for a single rule. Ask the practice's preference rather than copying that choice.
- Remove Snoooz branding in settings if the plan allows it, as the group workspace did.

## 3. Foundations before rules

- Create the five Gmail labels and five Snoooz categories in `rule-recipes.md`.
- Add Data Sources: the practice website, its Psychology Today profile, and its rates or FAQ page if it has one. Open each imported source once and check the text is the practice's and current.

## 4. Build in order

- Build the five exclusion rules first and leave every reply rule in Draft or Paused while you build.
- Build Psychology Today (primary language), Psychology Today (second language, if served), Directories, then the confirmed EAP rules, Existing Clients, Billing, and General Inquiries last.
- Paste each prompt, search it for a leftover [BRACKET], save, reopen, and compare the reopened prompt against the recipe before moving to the next rule.
- Never click Manage Labels inside an unsaved rule dialog. It discards the dialog.
- Check the character count on each prompt after pasting. Leave spare room — a group workspace's primary-language prompt sat at the limit, and a full prompt cannot take a later fix.

## 5. Test with simulations

Run a no-send simulation for each prospective-client rule and check the draft against the gates. Minimum cases, in the rule's language:

- In-scope adult, in a served client type, in a licensed state, asking about cost → invites booking, quotes only the confirmed rates (and the sliding-scale floor only if config says it may be quoted).
- Sender seeking therapy for someone under the practice's minimum age → warm decline, no booking link.
- Sender located in a state the clinician is not licensed in → decline, no booking link.
- Sender seeking a client type the practice does not offer (for example couples therapy, if not offered) → decline, no booking link.
- Sender mentions suicidal thoughts → opens with 988 and 911, no counseling, no booking lead.
- Sender asks for a session format the practice does not offer (for example in-person, if telehealth-only) → format stated plainly, the offered format still invited.
- Sender on an out-of-network plan → accurate panel answer, private-pay rate [and superbill, if confirmed] mentioned, booking still invited.
- Sender from an EAP with a free-consultation exception in config (if any) → no free-consultation invitation; the configured next step instead.
- Sender explicitly asking about care while located in an excluded country/region (if any) → answered correctly. A sender who does not ask → the reply must not mention the exclusion at all.
- Second-language inquiry (if served) → reply in that language, uses the clinician's name form for that language, carries only that language's booking link.

Fix the prompt, not the test, when a case fails, then rerun that case.

## 6. Go live in stages

- Turn exclusions on first. Leave them on permanently.
- Run Psychology Today and Directories in Draft for the review period chosen in config. Read every draft with the practice or report them daily.
- Switch those two rules to Send Reply only on the practice's explicit go-ahead, one rule at a time, and reopen each to verify the change.
- EAP availability requests stay Draft forever. Existing Clients and General Inquiries go live on the same staged pattern. Billing stays Draft or Forward, as chosen in config.
- Optional rules stay off. Google Voice and Vacation each need their own separate yes, after the warnings in `rule-recipes.md`.

## 7. Hand back an inventory

Report to the practice in chat:

- Each rule by name, position, action (Send, Draft, Forward, Label only), label, and status.
- The simulation results, case by case.
- Anything not built and why, including any config field still unconfirmed.
- A one-line entry in a change log in this folder with the date and what went live.

## 8. Keep it true

- When any fact in `provider-profile.md` changes, update the profile, the config, and every affected gate block in every language in the same session, then rerun the affected simulation cases.
- Monthly, skim Snoooz's activity log and a sample of sent replies for wrong invitations, invented availability, or fees quoted from anywhere other than the confirmed rates, and report what you found.
