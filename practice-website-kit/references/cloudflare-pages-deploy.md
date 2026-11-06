# Cloudflare Pages — deploy and domain

All under the **practice's own Cloudflare account**.

## Connect the project

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → authorize the practice's GitHub and select the site repo. (Authorize the repo, not the whole account's future repos, if the picker offers the choice.)
2. Build settings — use the **Astro preset**, which sets:
   - Build command: `npm run build`
   - Build output directory: `dist`
   - (Root directory blank unless the site lives in a subfolder.)
3. Production branch: the repo's main branch. Save and deploy; the first build should go green in about a minute. A red first build is almost always a content/schema error — read the log; Cloudflare runs the same `npm run build` you run locally, so reproduce locally first.

## Custom domain

1. Pages project → **Custom domains → Set up a domain** → enter the practice domain (and `www`).
2. Smoothest when the domain's DNS is already at Cloudflare (add the domain to Cloudflare first if DNS lives elsewhere — the registrar stays wherever it is; only nameservers move). Cloudflare then creates the records itself.
3. HTTPS is automatic (certificate issued by Cloudflare). Verify `https://<domain>` and the `www` variant both load, and that one redirects to the other consistently — pick the apex or `www` as canonical and make the site's canonical URLs match.
4. If the domain previously hosted another site, confirm the old host is fully out of the path (DNS, redirects) before announcing the URL anywhere.

## Previews and workflow

- Every non-production branch and pull request gets a **preview URL** automatically. Content workflow: draft in the CMS stays invisible (draft flag); code changes go branch → preview → merge. Editors saving on main publish immediately — that's the intended PagesCMS flow, and why the draft flag exists.
- **Rollback:** Pages keeps prior deployments; the dashboard's "Rollback" restores the last good build instantly if a bad deploy ever reaches production. Know it's there before you need it.

## Settings worth touching

- **Environment:** none needed for a pure static build. If the build needs a variable (e.g. a site URL for canonical/sitemap generation), set it in the Pages project for Production *and* Preview.
- **Headers/redirects:** a `public/_redirects` file in the repo handles moved pages (old site URLs → new) — write redirects for every old URL you know exists, especially any printed on directory profiles.
- **Web analytics (optional):** Cloudflare's own privacy-friendly analytics (no cookies) is the default recommendation for a therapy site; adding third-party trackers to pages that route people into care deserves a deliberate decision, not a default. Whatever is chosen, it goes in the handoff doc.
