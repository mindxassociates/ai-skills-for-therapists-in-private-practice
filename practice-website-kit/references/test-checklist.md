# Test checklist

## The CMS save test (first, per collection)

- [ ] Through PagesCMS (not the repo): edit one word in a provider bio → save succeeds (no extension error) → commit visible in the repo → deploy green → change live on the site.
- [ ] Same for a blog/resource post, including creating a **new** post end-to-end in the CMS (filename generated correctly from the slug field, cover image uploaded through the CMS media library, FAQs entered, draft on → not live; draft off → live).
- [ ] Reload the CMS and save again — config caching isn't masking a broken template.
- [ ] A deliberately bad entry (missing required field) is stopped by the CMS form or fails the build — and the live site stays on the last good build either way.

## Build and deploy

- [ ] `npm run build` passes locally from a clean checkout.
- [ ] Cloudflare production build green on the main branch; preview deploy works on a test branch.
- [ ] Custom domain + `www` both serve over HTTPS; the non-canonical variant redirects; canonical tags match the choice.
- [ ] Old-site URLs that exist anywhere (directory profiles, print) have `_redirects` to living pages.

## Content and correctness

- [ ] Every provider profile's facts (credentials, states, languages, fees/panels) match the practice's source of truth — checked name by name, not sampled.
- [ ] Booking buttons/embeds work, and each embed has a working fallback link.
- [ ] Contact page (and every contact-inviting page) shows the crisis block in every site language.
- [ ] Fees & insurance page is date-stamped and current.
- [ ] Language switcher (if bilingual) lands on counterpart pages; counterpart-missing links fall back gracefully; second-language provider names are the providers' own.
- [ ] No placeholder text, no invented claims, no lorem ipsum anywhere reachable — search the built site for the placeholder markers used during the build.

## Discovery and performance

- [ ] Sitemap lists every live page (including newest post + provider) and no drafts; RSS validates and shows recent posts.
- [ ] `llms.txt` / `llms-full.txt` reflect current content.
- [ ] Structured data validates on home, one profile, one article (with FAQ schema matching the visible FAQs).
- [ ] Mobile pass on a real phone-sized viewport: tap targets, header nav, booking flow reachable in ≤2 taps from home; Lighthouse performance on home is green or the exceptions are named and accepted.
- [ ] Total image weight on home is in the low hundreds of KB; favicon is small.

## Ownership

- [ ] Domain, GitHub, Cloudflare all under practice accounts with 2FA; the handoff table in `maintenance-and-handoff.md` is filled with real names/accounts; the agent's own access, if any remains, is intentional and listed.
