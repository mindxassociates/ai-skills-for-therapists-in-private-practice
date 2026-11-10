---
name: auto-created-listing-takedown-kit
description: "Find and remove auto-created clinician directory pages you never made — scraped profile sites that publish your name, NPI, address, and invented details (like assumed office hours) without consent. Covers discovering pages for a solo clinician or every clinician in a group practice, submitting removal through each site's own route (including Dr. Leonardo's claim-to-delist flow), clicking validation links, filing abuse reports with the FTC, Google, the host, and the registrar, and running a monthly sweep so removed pages stay removed. Use when a therapist finds (or wants to check for) an unauthorized profile, directory page, or NPI-mirror listing."
---

# Auto-Created Listing Takedown Kit

Directory companies scrape the public NPPES registry and auto-publish a "profile" or even a full mini-website for nearly every clinician in the country — no consent, no notice. The pages often contain information the operator simply *assumed*: office hours, "accepting new patients," specialties, even appointment-request widgets for a practice the operator does not run. They rank in Google for your name and mislead prospective clients.

This kit removes them, reports the pattern, and keeps them removed.

## What "done" means

1. **An inventory exists.** Every auto-created page found for the clinician (or for every clinician in the practice) is listed with its URL, what it claims, and whether it was verified as the right person (name **and** NPI match) before anything was submitted.
2. **A removal was submitted through each site's own route** for every page that has one — opt-out tool, delist toggle, contact form, or support email — and every email-validation link was actually opened, because most of these flows finish only after validation.
3. **Pages with no removal route are named as such** (some NPI mirrors publish none) rather than silently skipped.
4. **Abuse reports were filed** for the deceptive ones: FTC, Google Search Quality, the hosting provider, and the domain registrar.
5. **Legitimate listings were left alone** — the practice's own site, directories the practice actively manages (e.g. Psychology Today, insurance panels), and the NPPES record itself.
6. **A recurring monthly sweep is scheduled** to re-check the known URLs, catch re-listings, and scout for new auto-created pages.

## Setup interview (ask once, before filing anything)

1. **Who is covered** — one clinician, or the whole practice? For a group, get the roster: each clinician's legal name, preferred name, NPI, and license states. Legal names matter: pages are usually built from the NPPES legal name, not the name the clinician goes by.
2. **Claim email(s)** — which inbox receives validation emails? Some operators allow only **one claim per email address** (see the Dr. Leonardo reference). For a group, plan a unique address per clinician up front — e.g. a per-clinician address at the practice domain, or plus-addressing — all routed to one admin inbox the agent can check.
3. **Removal reason** — some forms force a reason from a fixed list, and none of the options may be truthful ("Office Closed," "Retired," "Not a Healthcare Organization"…). Decide the practice's standing choice *before* the first submission and use it consistently; never invent a closure or retirement.
4. **What counts as legitimate** — which listings does the practice claim and manage on purpose? Those are excluded from takedowns and from spam reports.
5. **Abuse-report scope** — does the clinician want the full set (FTC + Google + host + registrar) for the worst offender, or removal-only for minor mirrors? Get the complainant details once: legal name, practice legal name, address, phone, contact email.
6. **Recurring sweep** — monthly is the default cadence. Confirm the day, the report destination (chat/email), and that the sweep may re-file removals and spam reports without asking again when a known page resurfaces.

## Hard rules

1. **Verify identity before submitting.** A page is in scope only when the name *and* NPI both match the clinician. Same-name pages belonging to other professionals (a nurse practitioner, a pharmacist, a chiropractor with a similar name) are never touched.
2. **Removal only — never claim-and-keep.** Some flows make you "claim" the listing as the vehicle for deleting it. Claim solely to delist; do not complete a public profile, do not correct-and-keep unless the clinician explicitly chooses that instead of removal, and never pay or subscribe to any upsell (scheduling, patient portal, "premium profile").
3. **Validation links finish the job.** A submission banner saying "check your inbox" means the takedown is *pending*, not done. Open the validation link (check the spam folder — these senders land there) and record the confirmation wording before calling it submitted.
4. **One claim per email where the operator enforces it.** If a submission is rejected because the email was already used on another claim, switch to that clinician's own unique address — do not reuse, and do not abandon the takedown.
5. **Expect suffixed and misspelled URLs.** Auto-generated subdomains and slugs are often mangled (extra letters, "unknown" prefixes for mononymous clinicians). When the obvious URL 404s, use the operator's own provider search **by NPI** before concluding no page exists — and if a thorough search finds no record, report "no page found" as a result, not a failure.
6. **Handle validation tokens exactly.** Copy links byte-for-byte. A stray trailing character (a quote mark from an HTML attribute is the classic) produces "invalid token." If a token fails, extract the clean URL from the raw email and retry once before re-claiming.
7. **Report abuse with evidence, not adjectives.** Each report names the page URL, the clinician's NPI, the specific fabricated facts (hours, specialties, location), the operator's own admission if it publishes one, and the dates the removal was requested. Keep copies and case numbers.
8. **Nothing clinical, ever.** These are public-directory operations. No client information is involved, needed, or sent anywhere.

## Workflow

1. **Scout.** Search the web for each clinician's NPI number, legal name, and preferred name. Check the known offenders first (`references/directory-and-mirror-sites.md`), then general results. Build the inventory; discard same-name/different-person pages with the reason noted.
2. **Remove.** Work the inventory site by site using each site's playbook. Dr. Leonardo — the largest of these operators, with millions of auto-created clinician mini-sites — has its own step-by-step in `references/dr-leonardo-takedowns.md`. Validate every email link the same day.
3. **Report.** File the abuse set in `references/abuse-reports.md` for deceptive pages: FTC, Google Search Quality, the host/CDN (find it from the page's infrastructure), and the registrar (from RDAP/whois). Record every case/reference number.
4. **Verify.** After the operator's stated window (Dr. Leonardo says up to 72 hours after validation), revisit each URL and record gone / still live. Anything still live goes into the next sweep with a re-filed removal.
5. **Sweep monthly.** Schedule the recurring check in `references/monthly-sweep.md`: re-check known URLs, re-file for resurrected pages, scout for new ones, and send one summary report.

## Files

- `references/dr-leonardo-takedowns.md` — the Dr. Leonardo claim-to-delist flow, per-clinician email rule, NPI search, and token gotchas.
- `references/directory-and-mirror-sites.md` — per-site playbooks: Healthgrades, WebMD Care, NPI mirrors and data brokers (npiprofile, npi.usadb, datalabs.health, Topline), and what "no removal route" means.
- `references/abuse-reports.md` — FTC, Google, host, and registrar reports, with copy-ready text blocks.
- `references/monthly-sweep.md` — the recurring sweep: checklist, decision rules, and report format.
