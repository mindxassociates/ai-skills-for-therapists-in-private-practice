# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Publish / repair Brilliant Directories pages for my practice using the Brilliant Directories Publishing Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — my directory URL and admin login route, where my approved styled source files live, the roster source that decides provider names / credentials / fees / order, the page plan (slugs, types, languages, hreflang pairs), and my template's provider-card and body-block classes. Do not create anything until I have answered, and never invent a provider, credential, fee, or panel.
2. Work in **batches of at most 2 pages**. For each page: create it, set Protect Page to **Only Allow Members** immediately, then fill the body by **wholesale replacement from the approved styled source file** — verbatim, no paraphrase, no regeneration, no "tidying up." Run the kit's pre-save sentinel gates (exact correct strings present, known-wrong strings absent), knowing gates are a pre-save check only, never the verification. If exact copy proves impossible, stop and report instead of paraphrasing to finish.
3. **Verify the live page in a separate pass**, by fetching the served page (not the editor): provider-card name list exactly matching the expected ordered list; at least 3 exact source sentences character-for-character; every hreflang target character-for-character and pointing at a page that exists; structural negatives inside the body block; the SEO meta description checked separately; every structured-data block parsed and valid, with no double-quote characters inside schema text values.
4. Only after all content checks pass: flip Protect Page to **Public For Everyone**, then uncheck **Apply NoIndex, NoFollow** (Page Options → Advanced Options — it stays checked after the flip, and it can't be unchecked while the page is protected), **Save**, run **Refresh Live Site**, and fetch the live page again to confirm the robots meta reads `index, follow`. A page still serving `noindex, nofollow` is not done.
5. If the editor or Code View fails — stray characters inserted, button doing nothing, saves storing the body as text or empty — treat every save from that session as untrusted. At the **second dead end, stop, declare the route broken**, leave the pages hidden, and hand me a packet with the exact source files and steps for my own browser instead of retrying.
6. Report page by page, naming the exact live checks that passed for each one. Do not report a batch as done on a summary, and do not report any page as done on your own gate report alone.

---
