# Maintenance and handoff

## Day-to-day editing (the whole point)

1. Editor signs in at app.pagescms.org with GitHub.
2. Picks the collection (Providers, Blog/Resources…), edits in the form, saves.
3. The save commits to the repo; Cloudflare rebuilds; live in ~a minute. If the change doesn't appear, check in this order: the commit exists (repo) → the build went green (Cloudflare) → hard-refresh (cache). Not the CMS config — unless *saves themselves* fail, in which case read `pagescms-config.md`'s filename rule first.

Drafts: toggle `draft` on to hide a post/profile without deleting it; off to publish. An editor's pre-publish checklist lives next to the CMS links in the practice's own docs: facts checked against the roster, photo compressed, FAQs filled, links clicked.

## Who owns what (fill in at handoff)

| Thing | Owner account | Recovery |
|---|---|---|
| Domain registration | Practice | Registrar login + renewal billing noted |
| DNS / hosting (Cloudflare) | Practice | 2FA/passkey; backup codes filed |
| Repo (GitHub) | Practice (org or owner account) | Editors listed with write access |
| PagesCMS | Via GitHub sign-in (nothing separate to own) | Losing GitHub access = losing CMS access — protect GitHub |
| Content facts | Practice roster/records (source of truth) | Website edited *from* it, never the reverse |

## Backups, honestly

The Git repo *is* the backup of content and code (full history). Clone it somewhere the practice controls beyond GitHub (an annual archive is enough) and the site can be rebuilt on any static host in an afternoon — that's the portability this stack was chosen for. Cloudflare and PagesCMS are both replaceable layers; the repo + domain are the assets.

## Periodic rhythm

- **Quarterly:** click every booking/embed link; confirm fees/panels pages still match the roster; review draft pile; check the sitemap includes the newest posts; glance at Cloudflare analytics for dead pages (404s) and add `_redirects` for any that matter.
- **On any provider change** (joins, leaves, new license state): profile + home + schema facts move together, same day — a departed clinician lingering on the website is the classic stale-content harm.
- **Annually:** dependency bump (`astro` + packages) on a branch, preview-checked, merged; domain renewal confirmed; access list reviewed (departed staff out of GitHub/Cloudflare).
