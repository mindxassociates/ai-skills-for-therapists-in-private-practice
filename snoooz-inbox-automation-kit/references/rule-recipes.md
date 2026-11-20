# Snoooz Rule Recipes — Solo / Small Practice

Adapted from a live group-practice Snoooz workspace, reduced to what a solo or small practice needs. Replace every [BRACKET] from `../config.md`. Never paste another practice's link, email, or phone number into this workspace.

## Labels and categories — create these first

Gmail labels:

- Snoooz/Responded
- Snoooz/NotResponded
- Snoooz/Forwarded
- Snoooz/EAP

Snoooz categories:

- Inquiries from Prospective Clients
- Billing & Insurance Inquiries
- EAP Referrals
- Existing Client Communications
- Non-Urgent / Promotional

## Rule order

Exclusion rules override everything, at any position. Among inclusion rules only the highest-priority match fires, so keep this order:

1. Google Voice (optional, template, only if the practice opted in — see the warning below)
2. Psychology Today — (primary language)
3. Psychology Today — (second language, if served)
4. Inquiries from Mental Health Directories
5. EAP Referrals, referral-style (only if confirmed in config)
6. EAP Availability Requests (Draft only, only if confirmed in config)
7. Support for Existing Clients
8. Billing & Insurance Inquiries
9. General Inquiries (catch-all, always last)

Settings that held up in the group workspace for reply rules: Always active, Uses AI (except template rules), Reply to Lead's Email (Detected in Message) ON where the rule answers a directory lead, Draft / Send from the email alias OFF, Snoooz branding removed, label Snoooz/Responded, follow-ups off.

## The seven gate blocks

Append these to every prospective-client AI prompt, in this order, with the practice's facts filled in. Keep the wording tight — prompts have a character limit, and a full prompt cannot take a later fix.

Primary-language blocks:

```
Age rule: [CLINICIAN NAME] sees [AGES SERVED FROM PROFILE] only. If the person seeking therapy is outside that range — for example, a parent seeking therapy for a child the practice does not serve — politely decline and do not include the booking link.
Client-type rule: [CLINICIAN NAME] sees [CLIENT TYPES FROM PROFILE] only. If the sender seeks a client type the practice does not offer (for example couples, family, or group therapy, if those are not offered), politely decline and do not include the booking link.
Insurance rule: [CLINICIAN NAME] is in network with [CONFIRMED PANEL LIST FOR THIS PRACTICE, with state limits stated inline — a state-suffixed panel means that state only]. Answer insurance questions only from this list. Never estimate copays, deductibles, or benefits. If their plan is not in network, still invite them to book and mention the private-pay rate [AND, IF CONFIRMED IN CONFIG, that a superbill is available].
Location rule: [CLINICIAN NAME] is licensed for [FORMAT] in [LICENSED STATES/JURISDICTIONS FROM PROFILE] only. If the sender states they are located somewhere else, politely decline and do not include the booking link.
Crisis rule: If the sender mentions suicide, self-harm, or a crisis, open the reply with the 988 Suicide and Crisis Lifeline (call or text 988 in the US) and 911 for emergencies. Give no counseling.
Format rule: [FORMAT WORDING FROM PROFILE — for example: "All sessions are telehealth by video. If the sender asks for in-person therapy, say plainly that sessions are video only and still offer a video consultation."]
Fees rule: Quote fees only if the sender asks about cost, and quote only these rates: initial evaluation $[CONFIRMED] and follow-up sessions $[CONFIRMED]. Do not quote any other number. [SLIDING-SCALE LINE FROM CONFIG — either: "If the sender asks about sliding scale, the floor is $[CONFIRMED FLOOR]. Do not quote below it." or: "Sliding scale is discussed with the clinician directly; do not quote a sliding-scale number."]
```

Then the standing lines that apply to this practice, in this order — include each only if config records it:

```
[GEOGRAPHIC EXCLUSION LINE, if any: "[PRACTICE NAME] does not accept clients located in [COUNTRY/REGION]. Mention this only if the sender explicitly asks about receiving services while located in [COUNTRY/REGION]."]
[EAP EXCEPTION LINE, if any: "[CLINICIAN NAME] does not offer a free consultation to [EAP NAME] clients. If the sender is a [EAP NAME] client, do not invite them to a free consultation; use the next step recorded in config instead."]
```

Second-language blocks: translate the seven blocks and the standing lines into the second language, with these rules — use the clinician's second-language name form from the provider profile in every mention, never the primary-language name; state panel state limits inline just as in the primary language; carry only the second-language booking link; and have a fluent human review the crisis and decline wording before the rule goes live.

Decline style for every hard gate: one or two warm sentences, a brief reason tied to the gate, no booking link, and the contact email from config if the person wants to ask a follow-up. Do not send a declined sender to a third-party provider directory as a fallback unless the practice has explicitly chosen that pattern in config.

## Recipe 1 — Psychology Today, primary language

- Name: Psychology Today — ([LANGUAGE])
- Conditions: From domain contains msg.psychologytoday.com, AND Message Language = [LANGUAGE], AND the body mentions [CLINICIAN NAME] or the mail is addressed to the practice's Psychology Today listing address. (For a small group with per-clinician listing addresses, one rule per clinician, or one shared rule whose prompt covers every profiled clinician — decide in config.)
- Action: Send Reply (Draft Reply during the review period in config), Uses AI, Reply to Lead's Email ON, label Snoooz/Responded.
- Prompt skeleton:

```
You are the intake coordinator for [PRACTICE NAME], the practice of [CLINICIAN NAME], [CREDENTIALS]. Reply warmly and briefly to this Psychology Today inquiry as the practice, in [LANGUAGE]. [CLINICIAN NAME] is a [LANGUAGES] therapist providing [CLIENT TYPES] [FORMAT] therapy to [AGES SERVED] in [LICENSED STATES]. Specialties include [SPECIALTIES FROM PROFILE]. Approaches include [MODALITIES FROM PROFILE].
If the inquiry is in scope, invite the sender to book a free [LENGTH]-minute initial consultation here: [BOOKING LINK]. Do not invent availability or specific times. Do not provide clinical advice. Sign as [SIGNATURE FROM CONFIG].
[SEVEN GATE BLOCKS, THIS LANGUAGE]
```

## Recipe 2 — Psychology Today, second language

- Name: Psychology Today — ([SECOND LANGUAGE])
- Conditions: same sender conditions, Message Language = [SECOND LANGUAGE].
- Action: same as Recipe 1. The reply carries only the second-language booking link from config.
- Prompt skeleton: same content in the second language, practice name and signature from config's second-language fields, clinician named by the second-language name form, then the second-language gate blocks.

## Recipe 3 — Inquiries from Mental Health Directories

- Name: Inquiries from Mental Health Directories
- Conditions: From domain contains any directory sender the practice confirms in config (Psychology Today's sender domain, plus each additional directory's sender address — add a sender only when a real lead from that directory has arrived).
- Action: Send Reply (Draft during review), Uses AI, Reply to Lead's Email ON, label Snoooz/Responded.
- Prompt: same skeleton as Recipe 1, matched to the language of the incoming message, with the seven gate blocks in that language.

## Recipe 4 — EAP Referrals, referral-style (only if confirmed)

- Name: EAP Referrals — [EAP NAME]
- Conditions: From domain contains [EAP SENDER DOMAIN FROM CONFIG], AND category = EAP Referrals. The two credentialing exclusions below must exist first, because this rule otherwise fires on the EAP's credentialing mail too — in the group workspace it AI-replied to credentialing threads before the exclusions were added.
- Action: Send Reply, Uses AI, label Snoooz/Responded.
- Prompt must include: the practice accepts this EAP's clients (if confirmed), the profile URL from config, the soonest-availability general line from config (never a specific time, and never a claim that no time is available), and, only if config confirms a phone instruction, that instruction with the practice's own number. End with an invitation to reply to the email. Keep the line "Do not provide clinical advice."
- Hard rule: a referral for someone outside the practice's age gate is declined — the age gate applies to EAP referrals exactly as to directory inquiries; do not soften it for EAP.
- If no fit exists on an EAP referral, the group practice chose silence over a hopeless reply. The solo/small-practice equivalent: draft, do not send, and let the clinician decide.

## Recipe 5 — EAP Availability Requests (Draft only)

- Name: EAP Availability Requests — [EAP NAME]
- Conditions: From domain contains [EAP SENDER DOMAIN FROM CONFIG], AND Subject contains [THE AVAILABILITY-REQUEST SUBJECT PHRASE THAT EAP USES — copy it from a real message].
- Action: Draft Reply only, always. Reply to sender, label Snoooz/EAP. Never switch this rule to Send — Snoooz cannot check the calendar, so any availability in the draft is a placeholder for the clinician to replace before sending.
- Prompt: state stable facts only (licensed states, client types and ages served, format, EAP acceptance if confirmed) and leave the availability line visibly marked for the clinician to complete.

## Recipe 6 — Support for Existing Clients

- Name: Support for Existing Clients
- Conditions: To Recipient or Alias = the existing-client address if the practice keeps a separate one, otherwise category = Existing Client Communications.
- Action: Send Reply, Uses AI, label Snoooz/Responded.
- Prompt content that held up in the group practice, adapted: reply in the client's language (either language the practice serves), help with logistics only, tell clients to join the session video link 5 to 10 minutes early when a video link is the issue, give rescheduling and cancellation links or instructions from config, route every billing, insurance, and fee question to [BILLING CONTACT FROM CONFIG] instead of answering it, and give no clinical advice. If a client is in crisis, the crisis block applies here too.

## Recipe 7 — Billing & Insurance Inquiries

- Name: Billing & Insurance Inquiries
- Conditions: Category = Billing & Insurance Inquiries.
- Action: Draft Reply, or Forward to [BILLING CONTACT FROM CONFIG] if the practice prefers no AI draft. Label Snoooz/Responded when a reply is drafted.
- Prompt: answer only from the confirmed panel list in config, never estimate copays, deductibles, coverage, or benefits, explain that exact benefits depend on the person's plan, mention private pay [AND SUPERBILLS, IF CONFIRMED] where relevant, and invite the person to [CONTACT FROM CONFIG] for a benefits check.

## Recipe 8 — General Inquiries (catch-all)

- Name: General Inquiries
- Conditions: To Recipient or Alias = the main inquiry address from config, category = Inquiries from Prospective Clients, and no higher rule matched.
- Action: Send Reply (Draft during review), Uses AI, label Snoooz/Responded.
- Prompt: Recipe 1 skeleton without the Psychology Today reference, matched to the sender's language, with the seven gate blocks.

## Exclusion rules — build all of these before any reply rule goes live

All are Label Email Only with label Snoooz/NotResponded, Always active. Exclusions override inclusion rules regardless of order.

1. Don't Respond — category = Non-Urgent / Promotional, OR subject contains a Psychology Today availability-check or phone-call notification phrase (copy the exact phrases from real notification mail). Promotional miscategorization is the main false-positive risk, so review its hits weekly at first.
2. No Auto-Reply — Notifications — From is any of the practice's notification senders (EAP platform notifications, booking/EHR notifications, newsletter senders). List this practice's senders from config, not another workspace's list.
3. No Auto-Reply — Own Senders — From = the practice's own email addresses, every alias. A rule must never reply to, or forward, mail the practice sent.
4. No Auto-Reply — EAP Credentialing (sender) — From = [EAP CREDENTIALING SENDER FROM CONFIG], and the equivalent credentialing sender for any other confirmed EAP.
5. No Auto-Reply — EAP Credentialing (subject) — From domain = the EAP domain AND Subject contains [CREDENTIALING SUBJECT PHRASES FROM CONFIG — copy them from the credentialing mail the practice actually receives, e.g., disclosure-form or provider-addition phrases].

## Optional — Google Voice text template (read this warning first)

A group practice ran this rule and then paused it, where it stayed. Build it only if the practice opts in after hearing all of this:

- Snoooz has no once-per-number, once-per-thread, or stop-after-a-human-reply control. The template fired on every new message in a live text conversation a clinician was personally having with a prospective client, which is why it was paused. The only workaround is a manual exclusion rule for one specific sender number at a time.
- Use Template mode only, never Using AI. In testing, AI mode failed silently once and broke the format once. The email-to-SMS gateway delivers only the text before the first blank line, so the template must be a single paragraph with no line breaks, no greeting block, and no sign-off block.
- Exclude system senders from the start. In the group workspace, a directory notification number and an EHR-platform relay number both received the template before exclusions were added for their digit strings in the From address.
- Recipe: Position 1, From domain contains txt.voice.google.com, Category is not Non-Urgent / Promotional, plus one "From specific email address contains none of" condition per excluded number's digit string. Action Send Reply using a saved Template, Reply to Reply-To Address ON, branding removed, follow-ups off, label Snoooz/Responded.
- Template skeleton, one paragraph: "Thank you for texting [PRACTICE NAME]. This number is not monitored for scheduling. To book a free [LENGTH]-minute initial consultation with [CLINICIAN NAME], please visit [BOOKING LINK]. For anything else, [FOLLOW-UP WORDING FROM CONFIG — e.g., "a team member will follow up as appropriate" / "I will follow up as appropriate" for a true solo practice]." Confirm the wording with the practice character for character before saving the template.

## Optional — Vacation auto-reply (template)

- Recipe: Template mode, Always active only inside the vacation dates the practice sets, Send Reply, label Snoooz/Responded, and pause it the day the clinician returns — a stale vacation reply is worse than none. The group practice kept a rule like this paused outside vacation windows for exactly that reason.
- Template content: the dates away, when replies will resume, the booking link if the practice wants consults to self-serve while it is out, and the crisis line (988 and 911) in every version, because out-of-office replies reach people in distress too.
