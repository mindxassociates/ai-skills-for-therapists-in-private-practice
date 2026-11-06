# Therapist ISO Tracker

## Purpose

Monitor the Facebook therapist and referral groups you belong to for new "in search of" (ISO) posts, match them against your practice profile, and produce ready-to-copy reply drafts.

You post the replies yourself. This skill never posts, comments, reacts, or messages on your behalf.

It works for a solo practice (one provider profile) and for a group practice (several provider profiles, or a roster spreadsheet). The only difference is how many profiles are in `references/provider-profile.md`.

## Prerequisites

- Muse with the Facebook connector (`facebook-cli`) connected to your own Facebook account. You must be a member of the groups you want scanned.
- `config.md` in this skill filled in with your group IDs and schedule preferences.
- `references/provider-profile.md` filled in with accurate, current practice facts. Matching is only as good as this file. If it is blank or stale, do not scan.

## Setup (about 15 minutes)

1. Fill in `config.md`:
   - List each Facebook group to monitor, one per line, as `group_id — Group Name`.
   - Find a group ID by asking Muse: "Find the ID for my Facebook group called [name]" or run `facebook-cli groups search --keywords "<group name>"`.
   - Note the state each location-specific group implies (for example, an Austin group implies Texas, a Colorado group implies Colorado).
   - Choose your scan window and cadence. The recommended default is every 30 minutes, Monday to Friday, during your local business hours.
   - Choose your timezone.
2. Fill in `references/provider-profile.md` for each provider who may be recommended:
   - Name, credentials, pronouns if relevant, profile or website URL to link in drafts.
   - States licensed in, telehealth or in-person, ages served, and types of client seen (individual, couples, family).
   - Specialties and modalities, exactly as documented. Do not list a specialty you cannot stand behind in a public thread.
   - Insurance panels, with state and billing route noted where they differ. See the panel notes in `references/matching-rules.md`.
   - Private pay rates, whether you offer sliding scale, and your sliding scale minimum if you have one.
   - Whether you are accepting new clients, your typical availability (including evenings or weekends only if true), and anything you do NOT do.
   - Any provider-specific exclusions, for example "do not recommend for couples work" or "do not recommend when a post requires an experienced clinician".
3. Review `references/matching-rules.md` and change any default that does not fit your practice. The defaults are strict on purpose. Loosen one only when you mean it.
4. Do a first manual scan: ask Muse to "run the ISO tracker once now and show me what you find, including posts you skipped and why". Read the skipped list once. It is the fastest way to catch a wrong profile fact.
5. Optional recurring schedule: ask Muse to set up the scan from `config.md` (for example, "set up the ISO tracker every 30 minutes on weekday business hours"). Confirm the cadence, the hours, and that off-hours runs stay quiet before it is installed.

Detailed walkthrough: `references/setup-checklist.md`.

## Workflow

1. Check the scan window. If the current time is outside the window in `config.md`, stop quietly. Do not scan, do not change state, and do not send a report.

2. Load state. Read `state.json` if it exists (Muse keeps it in the skill's working folder or another location you agreed). It holds:
   - `last_check`: unix timestamp of the last completed scan.
   - `seen_ids`: post IDs already seen, newest first, capped at 500.
   If there is no state yet, start from the most recent end of the last business day in your timezone so a Monday scan covers the weekend.

3. Fetch recent posts in each group:
   `facebook-cli groups posts --group-id <id> --sort-by NEW_POSTS --min-timestamp <last_check> --limit 25`
   Do not rely on keyword or text query filtering. It can return zero results even when matching posts exist. Fetch recent posts and filter them yourself.

4. Identify candidates. A candidate is a post that reads as someone seeking a therapist for a client. Look for "ISO", "in search of", "looking for", "seeking", "referral", "recommendations", or "anyone know".
   Skip quietly: self-promotion, job or practicum seekers, posts seeking non-therapist professionals, testing or medication-only requests, event or meetup announcements, peer group or supervision requests, resource-only posts, and posts you have already seen.

5. Filter each candidate against `references/matching-rules.md` using `references/provider-profile.md`, in this order: state, age and population, accepting status, insurance and financial fit, setting and level of care, then specialty and modality fit.
   If no provider survives every filter, skip the post quietly. Do not report it and do not draft around a failed filter.

6. Check the thread before drafting:
   - Count comments or replies. Skip the post if it has more than 20. Exactly 20 is allowed. Busy threads are rarely worth a late reply, and this cap keeps scans honest.
   - Read the comments with `facebook-cli post comments read --post-id <id> --limit 25`. If you, your practice, or a provider you would recommend has already been named or has already replied, skip quietly.
   - Re-read the full post itself before drafting. Do not draft from a snippet or a summary.

7. Draft one reply per qualifying post. See the Output Contract.

8. Update state. Advance `last_check` to the current time and merge the new post IDs into `seen_ids`, capped at the newest 500. Only advance state after a scan that actually ran.

9. Keep a one-line run log if you keep daily notes: how many posts were scanned and how many matches were found. Send nothing to the user on a run with no matches.

## Output Contract

For each match, report:

- The post's full content, quoted verbatim.
- The group name, the post's local date and time, and a one-line summary of what is sought.
- The full permalink: `https://facebook.com/groups/<group_id>/permalink/<post_id>/`
- One draft reply per post, in its own code block, ready to copy and paste.
- Any caveats OUTSIDE the code block, for the user only. Example: "She documents OCD work as CBT-based, not dedicated ERP, so the draft does not claim ERP." Never put a caveat inside the draft and never claim the uncertain thing in the draft to get around the caveat.

Draft rules:

- Approachable and low-key, like a colleague dropping a helpful name in the thread. Not salesy.
- 2 to 4 sentences. Lead with the recommendation. No greeting, no introduction, no sign-off.
- No marketing language, no superlatives or hype ("perfect fit", "excellent", "highly experienced"), and no long specialty lists.
- Name the provider, give one or two plainly worded reasons tied to this post, note the state fit when it matters, and include the provider's profile or website URL.
- Use the profile or website URL, never a scheduling or booking link.
- Vary the opener. Do not start consecutive drafts the same way. Rotate forms such as "I'd recommend ...", "[Name] comes to mind for this — ...", "Sharing a suggestion: [Name] ...".
- Recommend at most three providers in one draft, and only when they fit comparably. Name one when only one fits well.
- Match the language of the post. If your practice works in a second language, mention that language only when the post asks for it or the post is written in it. Never volunteer a language, identity, or cultural specialty the post did not raise.
- Never overstate training, availability, rates, panels, or specialties. Only claim what is in the provider profile.

Good and bad examples: `references/draft-examples.md`.

## Operating Rules

1. Read-only on Facebook. Never post, comment, react, or message, even when the user seems to want it done quickly. Drafts are copy-ready and the user posts them.
2. Only recommend providers in `references/provider-profile.md`. Never invent credentials, states, ages served, panels, rates, or availability.
3. Accepting means accepting. Only recommend a provider whose profile says they are accepting new clients right now. A waitlist, a future start date that has not arrived, or a blank field is not accepting. If a profile carries a dated override (for example, "not accepting until [date]"), the override wins over the accepting field.
4. When in doubt about fit, skip quietly. A missed referral costs nothing. A wrong public recommendation costs reputation and can mislead a person seeking care.
5. Verify before you deliver. Re-read the full post and its comments yourself before presenting a match. A scan summary or a subagent report is a lead, not a verified match.
6. Keep the provider profile current. When licenses, panels, rates, availability, or exclusions change, update `references/provider-profile.md` and `references/matching-rules.md` together, and tell the user what changed.
7. Never disclose why another provider was excluded beyond what the user needs to check the draft. The draft itself carries no explanations and no internal rules.

## Available connectors

Use `muse.connector_search` to find the current connector docs before following recovered instructions.
