# Client Tool Publishing Kit

Take a finished bilingual client tool — an interactive worksheet, exercise, or psychoeducation page that exists only as a zip file — and put it on the web properly: a public GitHub repo **you** own, GitHub Pages hosting under **your own** custom domain, a copyright-free cover photo, and a listing in **your** tools index spreadsheet, in both languages, verified live before anyone calls it done.

## What you get

- **A repeatable deploy, not a one-off favour** — zip in, live tool out: repo created, Pages enabled on `main`, both language URLs checked for HTTP 200 (a 404 means "still building," never "live").
- **Both languages published and listed** — the English page at `/<slug>/` and the translated page at `/<slug>/<lang>/`, plus one row per language in your Client Tools sheet (Title, Keywords, Brief Description, Link, Cover Photo), read back after writing to confirm they landed.
- **A cover photo you can legally use** — picked from a copyright-free source (Pexels or Unsplash), actually looked at before use, and verified to return an image.
- **Names that don't break later** — the URL slug stays stable; if the tool's display name changes, the rename procedure updates titles and sheet rows without breaking links.
- **Costs:** $0. GitHub Pages on a public repo is free, including a custom domain.

## Who this is for

Therapists and practices that create client-facing tools — or receive them from a builder as a zip — and want a small public library of them (a tools page, a resources section, links sent to clients between sessions) without a platform fee or a developer on call for every new tool. You need a GitHub account and a spreadsheet; the kit handles the rest through your AI agent.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Deploy this client tool using this kit. Start with the setup interview in SKILL.md — don't deploy anything until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent — note this kit needs an agent with shell access and an authenticated `gh` CLI, so a coding-workspace agent is the right route (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Boundaries

- **Public pages collect nothing.** These tools are static pages. Anything a client types must stay in their browser — no forms posting entries, no stored responses. The kit flags a tool that appears to collect data instead of quietly publishing it.
- **Your accounts, your index.** The repo lives under your GitHub owner, the domain is yours, and the spreadsheet is yours — the kit takes all three from its setup interview and hardcodes none of them.
- **Deploy ≠ edit.** The kit publishes the tool as delivered. It does not rewrite hero copy, footers, or in-page wording unless you ask.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address from your browser's address bar, paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
