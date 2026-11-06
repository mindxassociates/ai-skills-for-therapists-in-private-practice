# Architecture and stack

## The three layers

```
editor ──▶ PagesCMS (web forms) ──commit──▶ GitHub repo ──build──▶ Cloudflare Pages ──▶ visitors
                                              │  ▲
agent/developer ──code + content──────────────┘  └── Astro source, Markdown content, .pages.yml
dynamic systems (booking, directory, forms) ──iframe embeds inside pages──▶ visitors
```

- **Astro** builds the repo into plain HTML/CSS/JS in `dist/`. There is no server, no database, no login on the site itself — which is why it is fast, cheap, and has almost no attack surface or maintenance.
- **PagesCMS** is a hosted editing UI over the same repo: it reads `.pages.yml` from the repo root, renders each content collection as a form, and commits saves back as the editor's GitHub identity. Delete PagesCMS tomorrow and nothing breaks — the content is Markdown in your repo.
- **Cloudflare Pages** watches the repo: every push to the production branch rebuilds and deploys in about a minute; pull requests and other branches get preview URLs. Custom domain + HTTPS are built in.

## What "static" means for a practice

Static is a fit, not a limitation, because a practice website's jobs are all publication jobs: explain services, introduce providers, state fees and panels, answer FAQs, publish resources, and route people to the systems that transact (booking, portal, directory). Those transactional systems already exist (Apps Script apps, an EHR portal, a booking platform) and static pages embed them by iframe — the embed pattern this whole ecosystem already uses.

What static cannot do, and the site must not promise: user accounts, site search over private data, form submissions stored *by the site*, real-time availability rendered natively. Each has an embed/link answer; if a requirement truly needs a backend, it belongs in the transactional system, not the brochure.

## Costs, honestly

- Domain registration: the only recurring cost (registrar's price).
- GitHub: free for public repos; a private repo also works with PagesCMS + Cloudflare.
- PagesCMS: free (open source; hosted app is free to use with your GitHub account).
- Cloudflare Pages free tier: sized for far more than a practice site — hundreds of builds/month and effectively unmetered bandwidth for static assets; per-file size caps exist (compress your media). Commercial use is allowed and there's no branding requirement — the two points that disqualify most "free" website builders for a business.
- Astro: free/open source. No per-seat anything, anywhere in the stack.

## Failure modes to design around

- **Editor breaks the build:** a malformed frontmatter field fails `astro build` and the deploy stops (the live site stays on the last good build — a genuinely kind failure). The content schema catches most of this in the CMS form itself; keep required fields required in `.pages.yml` too.
- **CMS config drift:** `.pages.yml` lives in the repo and is edited like code — changes go through the same review as a page change.
- **Account lockout:** everything hangs off the practice's GitHub + Cloudflare logins. Passkeys/2FA on both, recovery documented at handoff (`maintenance-and-handoff.md`).
