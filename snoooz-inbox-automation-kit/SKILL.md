---
name: snoooz-inbox-automation-kit
description: "Set up Snoooz.ai email automation for a solo or small therapy practice, adapted from a group-practice pattern: directory and Psychology Today inquiry replies gated on age, client type, insurance/panels, location/license state, crisis, session format, and fees/sliding-scale floor; EAP inquiry handling (send-ready referral replies, draft-only availability requests); existing-client and billing routing; exclusion rules and labels so promotional, notification, credentialing, and self-sent mail never gets an auto-reply; and optional Google Voice text and vacation templates, off by default. Use when a therapist wants to build, check, update, or troubleshoot Snoooz rules for their own practice."
---

# Snoooz Inbox Automation Kit

Adapt a proven group-practice inbox system to a solo or small practice. Snoooz answers directory and website inquiries with the practice's own facts, behind hard gates, while everything that should never get an auto-reply — promotions, system notifications, credentialing mail, the practice's own sent mail — is excluded first.

Group-only machinery does not transfer. A solo or small practice has no shared roster inbox, so per-provider forwarding, provider BCCs, and roster syncs are out; what transfers is the rule pattern: exclusions, gated inquiry replies per language, EAP handling, existing-client logistics, billing routing, and a catch-all — in that priority order.

Work through `config.md` first. Do not build any rule until the fields marked CONFIRM there are answered for *this* practice — especially the solo/small-practice insurance panels, the booking link(s), the contact and billing addresses, the fees and sliding-scale floor, and whether the practice is currently accepting new clients. Facts from any other practice the clinician also works with (a group, an agency, a platform) do not carry over on their own.

## What "done" means

1. `config.md` fully confirmed and `references/provider-profile.md` filled from it — one provider profile per clinician whose inquiries the rules answer.
2. The Gmail labels and Snoooz categories in `references/rule-recipes.md` created before any rule, so every rule can use them on the first pass.
3. Exclusion rules built and active before any reply rule goes live.
4. Reply rules built in recipe order, each prompt pasted from `references/rule-recipes.md` with every bracket replaced, saved, **reopened, and verified** against the recipe.
5. Every prospective-client rule passed a no-send simulation battery (see `references/setup-checklist.md`) in each language it serves.
6. Reply rules started in Draft for the review period chosen in `config.md` and switched to Send only on the practice's explicit go-ahead, one rule at a time — except availability-request rules, which stay Draft permanently.
7. A plain inventory reported back: rule name, order, action, label, live/draft status, simulation results, and anything skipped and why.

## The rule set

- **Psychology Today inquiry replies** — one rule per language the practice serves, each carrying the seven gate blocks in `references/rule-recipes.md`.
- **Mental health directories rule** — directory senders other than Psychology Today (for example, open-listing collectives or identity-based directories the practice is listed on). Add a sender only when a real lead from that directory has arrived.
- **EAP referral handling** — for each EAP confirmed in `config.md`:
  - *Referral-style EAPs* (an EAP emails a case referral expecting a reply): a send-ready reply rule, built only after the credentialing exclusions exist, because the same sender also sends credentialing mail.
  - *Availability-style EAPs* (an EAP emails asking for appointment availability): **Draft only, permanently.** Snoooz cannot see the live calendar and must never invent availability.
- **General Inquiries catch-all** — prospective-client mail that matches nothing more specific. Always last.
- **Existing Client Communications** — logistics only: session video links, rescheduling/cancellation instructions from config. No clinical advice. Billing questions are routed, not answered from memory.
- **Billing & Insurance Inquiries** — a category plus a routing/draft rule. Insurance answers stay soft, come only from the confirmed panel list, never estimate copays, deductibles, or benefits, and still offer the private-pay path with a superbill when the practice is out of network.
- **Exclusions, labels, categories** — the system in `references/rule-recipes.md`, so promotional mail, newsletters, system notifications, EAP credentialing mail, and mail from the practice itself never get an auto-reply.
- **Optional rules, off by default** — a Google Voice text template rule and a vacation auto-reply template rule. Each carries the risks documented in `references/rule-recipes.md` and is built only on its own separate yes.

## Setup workflow

1. **Interview.** Fill in `config.md`, asking one short set of questions at a time. Fill `references/provider-profile.md` from the answers and read corrections back before writing any prompt.
2. **Account.** Sign in to the Snoooz workspace (app.snoooz.ai) with the account the practice chooses — Snoooz sign-in is through Google, so do not look for a Snoooz password. Connect the one inbox inquiries actually arrive in and confirm the sending alias replies will come from.
3. **Foundations.** Create the labels and categories. Add Data Sources for the practice website, directory profiles, and any rates/FAQ page the rules may draw on, and check the imported text once. Data Sources store page text, not link targets, so booking links still belong in the prompts themselves.
4. **Build in order** — per `references/setup-checklist.md`: exclusions first, then Psychology Today per language, Directories, EAP, Existing Clients, Billing, General Inquiries last.
5. **Prompts.** Paste from `references/rule-recipes.md`, replacing every bracketed placeholder from `config.md`. Search each finished prompt for a leftover bracket before saving. Keep each prompt under the Snoooz prompt character limit with room to spare — write tight and cut wording before cutting facts.
6. **Test.** Run a no-send simulation for every prospective-client rule before it goes live: at minimum one in-scope inquiry, one under-age inquiry, one out-of-state inquiry, one client-type mismatch, one crisis mention, and one fee question, in each language the rule serves.
7. **Go live in stages.** Start Psychology Today and Directories in Draft if the practice wants to review tone; switch to Send Reply only on an explicit go-ahead. Availability-request rules stay Draft permanently.
8. **Verify by reopening.** Reopen every saved rule and check prompt text, action, label, schedule, and the Reply to Lead's Email setting. A rule is not done until the reopened version matches what was intended.
9. **Report.** Hand back the inventory described in "What done means," item 7.

## The seven gates on every prospective-client reply

Apply all seven blocks from `references/rule-recipes.md` to the Psychology Today rules, the Directories rule, and the General Inquiries rule, in this order: **age, client type, insurance, location, crisis, format, fees.**

- **Age, client type, and stated location are hard gates.** An out-of-scope request gets a warm, brief decline and no booking link.
- **Insurance is a soft gate.** Answer only from the confirmed panel list, name a panel only when it matches (a state-suffixed panel means that state only), and when the practice is out of network still invite the person with the private-pay rate and a superbill.
- **Crisis opens the reply.** When a message mentions suicide, self-harm, or crisis: 988 and 911 first (US), no counseling, and do not lead with booking.
- **Format is stated plainly.** If the practice is telehealth-only and someone asks for in-person, say sessions are video only and still offer a video consultation. If the practice offers in-person, use its configured format wording instead.
- **Fees are quoted only when cost is asked about,** and only the confirmed rates from config — including the sliding-scale rule: quote a sliding-scale floor only if a floor is recorded in config *and* config says it may be quoted; otherwise say sliding scale is discussed with the clinician and quote no number.
- **Geographic exclusions are never volunteered.** If the practice does not accept clients located in a particular country or region, that fact appears in a reply only when the sender explicitly asks about receiving services while located there.
- **EAP exceptions are encoded, not remembered.** If a confirmed EAP's clients do not get the free-consultation offer (or get a different next step), record it in `config.md` and put it in the gate blocks as a named exception line.
- **Per-language naming is exact.** In each language's rule, refer to each clinician by the name form recorded for that language in the provider profile, and carry only that language's booking link when the practice has separate links per language.

## Platform lessons (learned in a live group workspace)

- **Respect rule priority.** Snoooz applies only the highest-priority matching inclusion rule, so a reply rule placed above a labeling or routing rule can suppress it. Order rules deliberately and test the overlaps.
- **Exclusions override everything,** regardless of order — but they match only on message attributes such as sender, subject, body, and category. They cannot match on whether the AI found a fit.
- **There is no "AI decides not to reply" setting.** Snoooz has no setting that lets the AI skip a reply when there is no fit. The gate blocks in the prompt are what stop a bad invitation, which is why they are never optional.
- **Template mode, never AI mode, for a Google Voice text rule.** The email-to-SMS gateway delivers only the text before the first blank line, and AI mode ignored the one-paragraph instruction in testing. See the warning block in `references/rule-recipes.md` before building it.
- **Never click Manage Labels inside an unsaved rule dialog.** It discards the dialog and the unsaved prompt with it.
- **Expect no once-per-sender control.** Snoooz has no frequency cap and no stop-after-a-human-reply setting, so any rule that can fire repeatedly on a live thread is a risk the practice must accept explicitly or leave paused.
- **Verify by reopening, every time.** Prompts have reverted and saves have looked complete when they were not; the reopened rule is the only proof.

## What not to copy from another practice's setup

If you are adapting this from a group practice (or any other practice) whose Snoooz workspace you have seen:

- Do not copy its booking links. Use only this practice's links from `config.md`.
- Do not copy its contact details — no email addresses, phone numbers, or EAP call-in numbers from the other practice.
- Do not copy its providers, roster, panel lists, or rates. A panel held through a group or a platform is not automatically a panel of this practice. Only panels confirmed for *this* practice go in its prompts.
- Do not build per-provider forwarding rules, provider BCCs, or a roster sync. Those route a shared group inbox and have no solo/small-practice equivalent.
- Do not name the other practice in replies, except where a directory listing genuinely sits under that practice's name and the clinician asks for it there. The practice name comes from `config.md`.

## Maintenance

- Update `references/provider-profile.md` and `config.md` first when a license, panel, rate, specialty, availability, or contact fact changes, then update the matching gate block in every affected language rule in the same pass.
- Re-run the no-send simulations after any gate-block change, and reopen the affected rules to verify.
- Review draft replies weekly for the first month, then monthly. Look for wrong invitations, missed declines, invented availability, and any fee quoted from somewhere other than the confirmed rates.
- Keep a one-line change log in the skill folder with the date, the rule touched, and what changed, so a later session starts from the live state.

## Reference files

- `config.md` — the blank configuration template; every CONFIRM field is answered before building
- `references/provider-profile.md` — the blank per-clinician profile template that feeds every prompt
- `references/rule-recipes.md` — labels and categories, rule order, the seven gate blocks in a primary language and a second-language form, all rule recipes, exclusions, and the optional-rule warnings
- `references/setup-checklist.md` — the ordered build, simulation battery, staged go-live, and handoff inventory
