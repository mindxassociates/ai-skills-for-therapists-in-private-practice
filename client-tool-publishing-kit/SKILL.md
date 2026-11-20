---
name: client-tool-publishing-kit
description: Deploy a bilingual interactive client tool (worksheets, self-guided exercises, psychoeducation tools) from a zip to GitHub Pages and list it in a tools index spreadsheet. Use when a therapist wants (1) a tool zip containing an English page (index.html) plus a translated version in a subfolder (e.g. zh/index.html) published as a public GitHub repo under their own GitHub account or organization, with GitHub Pages enabled on the main branch and served under their own custom projects domain; (2) a copyright-free cover photo (Pexels or Unsplash) picked, visually inspected, and verified to return an image; (3) one row per language appended to their Client Tools spreadsheet (title, keywords, description, link, cover photo) and read back to confirm; and (4) verification that both live URLs return HTTP 200 before anything is reported as live. The kit deploys and lists the tool — it does not edit the tool's page content.
---

# Client Tool Publishing Kit — Bilingual Tools to GitHub Pages

Many practices build (or commission) small interactive client tools —
a worksheet, a values exercise, a guided journaling page — as a single
self-contained HTML file, often with a translated version. This kit is
the repeatable last mile: get the tool out of the zip and onto the web
under **your own** GitHub account and **your own** domain, with a cover
photo, listed in **your** tools index spreadsheet, and verified live in
both languages.

The full step-by-step runbook is in `references/deploy-workflow.md`.
Follow it exactly — it is written so any agent with shell access, an
authenticated `gh` CLI, and spreadsheet write access can execute it
end to end.

## Setup interview (ask once, before deploying)

1. **The tool** — the zip file (must contain `index.html` at the root
   and the translated page in a language subfolder, e.g.
   `zh/index.html`), and the URL slug (lowercase-hyphen; it becomes the
   repo name and the URL path, and stays stable once deployed).
2. **The copy, per language** — title, one-sentence description, and
   comma-separated keywords in English *and* in the second language.
   Ask for anything missing; **never invent titles or descriptions**,
   and do not translate the English title word-for-word into the second
   language unless the owner asks — use the rendering they supply.
3. **Your GitHub** — the account or organization the repo will live
   under (resolved at runtime, never assumed), with the `gh` CLI
   authenticated and holding `repo` scope, and your GitHub Pages custom
   domain (e.g. `https://projects.example.com/<slug>/`), confirmed from
   the Pages API rather than assumed.
4. **Your tools index** — your Client Tools spreadsheet, its tab names
   (one per language, e.g. `Tools` and the second language's tab), and
   its columns (conventionally: Title | Keywords | Brief Description |
   Link | Cover Photo).
5. **Cover photo guidance** — any topical direction from the owner
   ("something calm, no faces"), or their own supplied image. Otherwise
   the agent picks a copyright-free photo per the runbook.

## Workflow (summary — details in the runbook)

1. **Collect inputs** from the setup interview. Ask for anything
   missing; never invent copy.
2. **Extract and inspect the zip.** Confirm both HTML files exist,
   are self-contained, and that each file's `<title>` / meta description
   matches its language.
3. **Create the repo and push.** If a plain `git push` later asks for a
   username, run `gh auth setup-git` once, then push again.
4. **Enable Pages on `main`** via the API and poll until built. Verify
   **both** live URLs return HTTP 200. A 404 means still building —
   wait and retry; never report a tool live early.
5. **Pick and visually verify a copyright-free cover photo**
   (Pexels or Unsplash), and confirm its URL returns `200` with an
   image content type.
6. **Append one row per language** to your Client Tools sheet, then
   read both rows back to confirm titles, links, and cover URL.
7. **Report** the repo URL, both live URLs, the cover choice and why,
   and the new sheet rows.

## Output contract

- A public GitHub repo `<your-owner>/<slug>` exists, is pushed, and
  Pages reports `built` on `main`.
- `https://<your-projects-domain>/<slug>/` and
  `https://<your-projects-domain>/<slug>/<lang>/` both return
  HTTP 200.
- One new row in each language tab of your Client Tools sheet with
  Title, Keywords, Brief Description, Link, and Cover Photo; the
  cover URL returns `200` with an image content type (e.g.
  `image/jpeg`).
- The final report names the repo URL, both live URLs, the cover
  photo and why it was chosen, and confirms the sheet rows.

## Operating rules

1. **Resolve the GitHub owner at runtime** (e.g. `gh api user`), and
   confirm the token's `repo` scope before creating anything. Do not
   hardcode an owner, a domain, or a spreadsheet ID anywhere — they
   come from the setup interview, every time.
2. **Keep the URL slug stable once deployed.** A later rename changes
   the tool's *display name* only (see the runbook's rename procedure),
   never the slug — unless the owner explicitly asks for a full URL
   change and accepts that the old Pages URL stops working.
3. **Use the bare, stable URL form for the cover photo** that your
   photo source provides (for Pexels, the
   `images.pexels.com/photos/<id>/…` form), and **look at the image**
   before using it — on-theme, appropriate, no watermark, no meme,
   no misleading stock cliché.
4. **Do not edit the tool's page content** (hero copy, footer, in-page
   wording) unless the owner asks. This kit deploys and lists; it is
   not an editing pass.
5. **Both languages, every time.** A deploy is not done when only the
   English page is live, and the listing is not done when only one
   tab has its row.
6. **Clinical boundary:** these tools are public web pages. They must
   collect nothing clinical and store nothing a client types — if a
   tool asks for input, it stays in the visitor's browser. Flag any
   tool that appears to send or store client entries before deploying
   it, and let the owner decide.
