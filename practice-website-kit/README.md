# Practice Website Kit

Build your practice website the modern, ownable way: **Astro** (a fast static-site framework) for the site, **PagesCMS** so you or your staff can edit pages and posts in a friendly web form instead of code, and **Cloudflare Pages** for free, fast hosting on your own domain — no website-builder badge, no monthly platform fee, no plugin treadmill.

## What you get

- **A complete practice site blueprint** — home, about, provider profiles, services, fees & insurance, FAQs, a blog/resources section you can actually keep alive, and a contact page that hands off to your booking system.
- **Static where it should be, dynamic where it must be.** The site itself is static files (fast, secure, nothing to hack or patch). Anything interactive — booking, forms, directories — is embedded from the systems that already run it, via iframe.
- **Editing without a developer.** PagesCMS (free, open source) signs in with GitHub and turns your content folders into forms: title, photo, body, FAQs, publish toggle. A save commits to your repo, Cloudflare rebuilds, the page is live in a minute.
- **Real SEO plumbing** — per-page titles/descriptions, structured data (practice + provider + article/FAQ schema), sitemap, RSS, social-card images, and an `llms.txt` so AI assistants describe your practice accurately.
- **Costs:** domain registration only. Cloudflare Pages' free tier is genuinely sufficient for a practice site (generous builds and bandwidth, custom domains, no branding, commercial use allowed).

## Who this is for

Solo and group practices paying a builder platform for a brochure site, or stuck unable to update their own pages. Also practices adding a second language — the blueprint includes a mirrored-language structure (e.g. `/zh/`) instead of machine-translation widgets.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build my practice website using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Boundaries

- **A public website collects no clinical information.** No intake forms, no message boxes that invite people to describe their symptoms to a static page. Contact paths route to your booking/messaging systems, and contact pages carry your crisis line (988 in the US) — a therapy site that skips that is not finished.
- **You own everything:** the domain, the GitHub repo, the Cloudflare account. The kit sets it up that way deliberately — never under a vendor's or a freelancer's account.
- Accessibility and honesty checks are part of the build, not polish: real alt text, working mobile layout, and no claims (credentials, panels, outcomes) the practice can't stand behind.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/practice-website-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
