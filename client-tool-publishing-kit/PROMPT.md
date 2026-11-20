# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Deploy this bilingual client tool using the Client Tool Publishing Kit in this workspace — GitHub Pages for hosting, a copyright-free cover photo, and a listing in my tools index spreadsheet. Follow `references/deploy-workflow.md` exactly.

1. Run the **setup interview** in `SKILL.md` first — the zip, the URL slug, the title / one-sentence description / keywords in **both** languages, my GitHub owner and Pages custom domain, and my Client Tools spreadsheet with its per-language tabs. Ask for anything missing; never invent titles or descriptions, and don't translate the title word-for-word unless I ask.
2. **Extract and inspect the zip**: confirm `index.html` and the translated page (e.g. `zh/index.html`) are both there and self-contained, and confirm from each file's title/meta which language it is. If the tool appears to send or store anything a visitor types, stop and flag it before deploying.
3. **Create the repo under my GitHub owner and push** (resolve the owner at runtime; confirm `repo` scope first; if a push asks for a username, run `gh auth setup-git` once and retry).
4. **Enable Pages on `main`** via the API, poll until the status is `built`, then verify **both** live URLs return HTTP 200. A 404 means still building — wait and retry, and do not report the tool live until you see 200 on both.
5. **Pick the cover photo** from a copyright-free source (Pexels or Unsplash), download and actually look at it — on-theme, appropriate, no watermark or meme — use its bare stable URL form, and verify it returns `200` with an image content type.
6. **Append one row per language** to my Client Tools sheet (Title, Keywords, Brief Description, Link, Cover Photo — same photo both rows, the translated row linking to the translated URL), then **read both rows back** and confirm them.
7. Report the repo URL, both live URLs, the cover photo and why you chose it, and the two new sheet rows. Do not edit the tool's page content, and do not change the slug.

---
