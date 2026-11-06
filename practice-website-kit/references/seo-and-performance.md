# SEO and performance

## Metadata, per page

- Unique `<title>` and meta description, written for humans first (they're the search-result ad copy). Title/description come from page props or frontmatter — never one global string.
- Canonical URL on every page; Open Graph + Twitter card tags with a real image; per-article social images (a slug→image map or the article's cover) instead of one site-wide default.

## Structured data (JSON-LD), matched to the page

- **Home:** `ProfessionalService` / `MedicalBusiness`-appropriate schema for the practice — legal name, url, phone, area served, languages — only facts the practice publishes and can stand behind.
- **Provider profiles:** `Person` with job title, credentials as published, affiliation to the practice.
- **Posts/guides:** `Article` (headline, date, author, image) **plus** `FAQPage` generated from the same `faqs` frontmatter list the page renders. One source, both outputs — schema that disagrees with visible content is worse than none.
- Validate one page of each type in a rich-results tester before launch.

## Discovery plumbing

- **Sitemap** endpoint that walks every collection (pages, providers, posts, guides, language trees) — new content must appear automatically; a hand-list sitemap goes stale the first month.
- **RSS** for the posts collection, with the discovery `<link rel="alternate">` in the layout so feed readers and aggregators find it.
- **`llms.txt` + `llms-full.txt`** at the site root: a concise practice summary + page index for AI assistants, and the full-text version. Generate them from the same content (a build step or a checked refresh whenever collections change) — AI assistants are now a real referral channel for practices, and they quote what these files say.
- **robots.txt** permissive for a public practice site, pointing at the sitemap.

## Consistency with the rest of the web

Search engines and clients cross-check: the site's name, phone, address-of-record, provider names/credentials, and booking links should match the practice's Google Business Profile and directory profiles (Psychology Today etc.) exactly. Inconsistency here reads as a different or defunct practice. Make the site the reference and fix the listings to match it — or vice versa — but decide.

## Performance rules (phones + anxious visitors)

- **Images:** compress before commit (a page's total image weight in the low hundreds of KB; hero/profile photos resized to the size actually displayed, modern formats where the pipeline allows). An uncompressed multi-MB photo set is the #1 real-world failure of practice sites.
- **Favicon/logo:** small and optimized; a 500 KB favicon is a real thing that has shipped — check yours.
- **JavaScript:** Astro's near-zero default is the point — every script added (chat widgets, trackers, embeds) is a deliberate, named decision. Embeds (booking etc.) lazy-load below the fold where possible.
- **Fonts:** self-host or system-stack; if webfonts, subset and preload the one that matters. No layout shift on the booking button.
- Run a Lighthouse pass on home + one profile + one post before launch; fix what's red, note what's accepted.
