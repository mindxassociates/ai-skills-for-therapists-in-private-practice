# Setup Checklist

Work through this once, with Muse. About 15 minutes. Do not turn on a recurring schedule until step 5 passes.

## 1. Connect Facebook

- [ ] Your Facebook account is connected in Muse and the Facebook connector works. Test: ask Muse "What Facebook groups am I in that have 'therapist' in the name?" A real list means the connection works.
- [ ] You are a member of every group you want scanned. The tracker can only see groups you belong to.

## 2. List your groups

- [ ] For each group: name, group ID, and the state it implies if it is location-specific.
- [ ] Write them into `config.md`.
- Pitfall: do not guess an ID from a group URL you half-remember. Look each one up and copy it exactly.

## 3. Build your provider profile

- [ ] One block per provider in `references/provider-profile.md`, or the roster-sheet pointer described there.
- [ ] Every field filled from facts you can stand behind, or deleted.
- [ ] Accepting status is current today, not "usually yes".
- [ ] Panels note state differences and billing route (direct vs. platform) where they exist.
- [ ] Sliding scale minimum written down if you have one. This single number prevents the most common bad draft.
- [ ] "Do NOT recommend for" lines written, even if short.
- Pitfall: copying a directory bio wholesale imports claims you may not want in referral threads (old panels, old rates, "now accepting" from last year). Prune as you paste.

## 4. Customize the matching rules

- [ ] Read `references/matching-rules.md` top to bottom once.
- [ ] Set the Medicare and Medicaid default to match your panels.
- [ ] Fill the hard-skip specialty list: services nobody in your practice offers that your groups ask about often.
- [ ] Set any last-resort provider rule and your tie-break priority in `config.md`.

## 5. First manual run

- [ ] Ask Muse: "Run the ISO tracker once now. Show me every match with its draft, and also list the posts you skipped with the filter that removed each one."
- [ ] Read the skipped list. A wrong skip usually means a wrong profile fact. Fix the profile, not the filter.
- [ ] Read each draft as if a colleague posted it about you in public. Would you be comfortable with every claim in it? If not, the profile or the rules need an edit before any schedule exists.
- [ ] Check one permalink by opening it. It should land on the exact post.

## 6. Turn on the schedule (optional)

- [ ] Confirm with Muse, in words: the cadence (recommended every 30 minutes), the days and hours, the timezone, and that off-hours runs stay silent and do not advance state.
- [ ] Confirm where results land (this chat) and that a run with no matches sends nothing.
- [ ] After the first scheduled day, spot-check: did the morning run cover the previous evening? Did any busy thread (over 20 comments) slip through? Report what you find to Muse so the config can be corrected.

## Maintenance (2 minutes, whenever something changes)

- [ ] Panel joined or left, rate change, intake paused or reopened, new state license, new exclusion: tell Muse to update `provider-profile.md` and `matching-rules.md` together and confirm what changed.
- [ ] Group joined or left: update `config.md`.
- [ ] Monthly: ask Muse to re-verify one recent draft against the profile. Staleness creeps in silently.
