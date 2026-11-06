# Site blueprint — the pages

Adapt the set to the practice; the musts are the point.

## Home

- One sentence that says who you help, where (states / telehealth), and in what languages — above the fold, in the visitor's language, with the primary action (book a consultation) as the obvious button.
- Trust block: licenses, approach in plain words, insurance/private-pay summary — each linking to its detail page.
- Provider introductions (group) linking to profiles; featured services; a short FAQ teaser; footer with contact, crisis line, and legal links (privacy, terms).

## About / our approach

The practice's philosophy without marketing fog: who it's for, how therapy works here, telehealth logistics, what the first step looks like. This page carries the practice's voice — write it with the owner, never generate generic warmth and ship it.

## Provider profiles (one page per clinician)

- Photo (compressed, real), name + credentials, license states, populations and specialties, approaches, languages, fees or panel summary, booking link for that provider (or the practice booking page).
- Generated from the provider **content collection** — one Markdown file per provider behind a schema — so adding a clinician is a content task, and the profile index stays consistent automatically.
- Every fact here must match the practice's roster source of truth (Hard rule 6).

## Services (one page per service line, if the practice markets them separately)

What the service is, who it's for, what sessions look like, fee/panel notes, related providers, booking action. Resist inventing a page per keyword; write the pages clients actually need.

## Fees & insurance

- Self-pay rates (initial evaluation + follow-up) as the practice publishes them, panels accepted, superbill/out-of-network explanation, sliding-scale policy if any, good-faith-estimate / No Surprises Act notice where applicable.
- Date-stamp the page ("updated <month year>") — stale fee pages erode trust faster than no fee page.

## FAQs

Real questions from real inquiries (the practice's inbox and chatbot logs are the source): cost, insurance verification, telehealth across state lines, cancellation, languages, how booking works. FAQs live in a **collection with a `faqs` frontmatter list** on the relevant pages, so they render both as page content and as FAQ structured data (see `seo-and-performance.md`).

## Blog / resources

- A CMS-managed collection (`posts` or `news` + optionally evergreen `guides`): title, slug, date, description, cover image, body, FAQs, publish toggle.
- This is the section that justifies PagesCMS: a practice that can publish without a developer actually publishes.

## Contact

- Booking action first (embed + fallback link), phone, email, response-time expectation — and the **crisis block**: not monitored in real time; if you're in crisis call/text **988** (US), emergencies **911** — in every site language.
- No free-text "describe your situation" form. If a form exists, it's the practice's routed form app (structured fields, goes to the CRM/inbox), embedded or linked — the static site stores nothing.

## Footer (every page)

Practice legal name, address of record if the practice publishes one, crisis line, privacy + terms, copyright. Group practices: the entity name matches the legal entity on the practice's other records — check, don't assume.

## Multilingual tree (when chosen)

Mirror the full page set under `/zh/` (or the chosen language), translated as content, with its own slugs and its own CMS collections (or a language field + filtered views — pick one model and keep it consistent). The language switcher links counterpart pages, falling back to the other language's home when no counterpart exists. Provider names in the second language use the providers' own names in that language — sourced from the roster, never transliterated by the agent.
