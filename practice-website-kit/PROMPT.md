# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Build my private practice website using the Practice Website Kit in this workspace — Astro for the site, PagesCMS for editing, Cloudflare Pages for hosting, all under accounts I own.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — practice name and domain, solo or group, provider list, services, languages (including whether a mirrored second-language tree is needed), which dynamic systems must embed (booking, directory, contact), and who will edit content day-to-day. Do not build anything until I have answered, and never invent credentials, panels, fees, or claims — use placeholders and flag every one.
2. Build in kit order: **Astro project + content model** (`references/astro-setup.md`) for the pages in `references/site-blueprint.md`, then **PagesCMS config** (`references/pagescms-config.md`), then **Cloudflare Pages deployment** (`references/cloudflare-pages-deploy.md`), then the **SEO/performance pass** (`references/seo-and-performance.md`).
3. Obey the kit's hard rules: everything lives in a Git repo I own; content is Markdown + frontmatter validated by a schema, never hard-coded into templates; every CMS collection's filename template uses `{fields.slug}` (a bare `{slug}` breaks every save); the site collects no clinical information and every contact path carries the crisis line; dynamic features are iframe embeds of my existing systems, not new backends.
4. Verify like the kit says: after PagesCMS is configured, make a **real test edit through the CMS** (change a word, save, watch it deploy) — a CMS that hasn't saved successfully isn't set up, whatever the config looks like.
5. Walk me through `references/test-checklist.md` at the end and don't call it done until the CMS save test, the custom-domain HTTPS check, and the mobile pass all succeed.

---
