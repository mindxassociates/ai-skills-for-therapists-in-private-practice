# Therapist ISO Tracker — Configuration

Fill this in before the first scan. Muse reads this file on every run.

## Groups to monitor

List one group per line as `group_id — Group Name — Implied state (if any)`.
Find a group ID by asking Muse to search your groups by name, or run:
`facebook-cli groups search --keywords "<group name>"`

A location-specific group implies that state for posts that name no state. A post that names a state overrides the group's implied state.

```
# Example:
# 1234567890123456 — Therapists in Private Practice — none
# 2345678901234567 — Austin Mental Health Referrals — TX
```

Groups:
```
# (add your groups here)
```

## Schedule

- Scan window (days): Monday to Friday
- Scan window (hours, local time): 08:00 to 17:00
- Cadence: every 30 minutes inside the window
- Timezone: (yours, for example America/Chicago)
- Off-hours and weekend behavior: exit quietly, do not scan, do not change state, do not send a report. The next in-window scan naturally covers everything since the last in-window scan, so a Monday morning scan covers the weekend.

Change the window to fit your life. The cadence and gate matter more than the exact hours: frequent enough that good posts still have few replies, bounded enough that you are not pinged at night.

## Practice mode

- Mode: solo / group (delete the one that does not apply)
- If group: how many providers may be recommended: (see references/provider-profile.md)
- If group: provider priority when fit is comparable (optional — for example, order by availability or by who most needs referrals; name the order here or delete this line):
- Providers who are last-resort only, and the condition for naming them (optional — for example, a practice owner who should only be named when the post requires a panel only they hold and no one else fits):

## Reply preferences

- Draft language: match the language of the post.
- Link to use in drafts: each provider's profile or website URL from the provider profile. Never a scheduling link.
- Comment cap: skip posts with more than 20 comments or replies. (Recommended. Change only if your groups move slower.)
- Mention a second language in drafts only when: the post asks for it or the post is written in it.

## State file

- State location: (leave blank and Muse will keep `state.json` beside this config and tell you where)
- State holds `last_check` (unix seconds) and `seen_ids` (newest first, capped at 500). See `references/state-template.json`.
