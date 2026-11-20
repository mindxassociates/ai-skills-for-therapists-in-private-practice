---
name: brilliant-directories-publishing-kit
description: Create, restyle, and repair Brilliant Directories directory / SEO landing pages from a styled source file and verify each live page exactly before it goes public. Use when a practice that runs its directory on Brilliant Directories wants (1) new pages created hidden (Only Allow Members) and filled by wholesale body replacement from the source file, never by paraphrase or regeneration; (2) pre-save sentinel gates and independent live verification — exact provider-card list vs. the expected ordered list, at least 3 exact source sentences, hreflang targets character-for-character, structural negatives, the SEO meta description, and structured data; (3) the noindex trap cleared in the right order (flip to Public first, then uncheck Apply NoIndex, NoFollow, Save, Refresh Live Site, verify robots meta reads index, follow); and (4) a stop-and-declare-broken rule when the page editor / Code View is unreliable, plus a monthly live-page sweep.
---

# Brilliant Directories Publishing Kit — Hidden-First, Verified Live

This kit is a publishing *discipline*, not a writing shortcut. The failure it
prevents is specific and has happened repeatedly in real directory work:
a creation pass reports success, every internal gate "passed," and the live
page turns out to be a paraphrase — with reworded sentences, invented
provider names, wrong credentials or fees, and a robots tag that keeps it
out of search entirely. The rules below exist so that cannot ship.

**The core principle: the styled source file is the page. The editor is
only a delivery mechanism. Verification happens on the live URL, by a
separate pass from the one that made the edit, and a worker's own
"all gates passed" report is never evidence.**

## Setup interview (ask once, before any page work)

1. **Your directory** — your Brilliant Directories site URL (e.g.
   `https://directory.example.com/`), your BD admin login URL, and how you
   sign in (your own saved login for that admin — never share credentials
   in chat; the agent works in a session you have already signed in to).
2. **Source of truth** — where the styled source files live (e.g. a folder
   in Google Drive), who approves a source file as final, and the file
   naming convention per page.
3. **Roster source** — the record that decides who is listed on a page
   (your provider roster / records), in what order, with which exact
   names, credentials, fees, and panels. The page never invents or
   "corrects" these.
4. **Page plan** — the pages in this batch: slug, page type (state /
   specialty / payer / city / resource), language, and its hreflang pair
   (the matching page in the other language, exact slug) if any.
5. **Styled template** — the CSS classes your template uses: the
   provider-card element, any lede / table-of-contents blocks that belong
   *outside* the body block, and where per-page CSS lives.
6. **Browser route** — page-body and Code View work needs a wide desktop
   browser window; a narrow/mobile window can stack the editor toolbar
   past the viewport so Code View never activates. Confirm which browser
   session will be used before starting.

## The flow (every new page, no exceptions)

1. **Build the styled source file first**, outside Brilliant Directories,
   and get it approved as final. A repair later is then a fresh wholesale
   replacement, not a hand edit.
2. **Create the page and immediately set Protect Page to
   Only Allow Members.** Nothing public appears before verification.
3. **Replace the body wholesale** from the styled source file. Paste the
   body verbatim — no rewording, shortening, "improving," or regenerating
   any sentence, card, fee, or name.
4. **Work in batches of at most 2 pages.** If an exact copy from the
   source file proves impossible, stop and report — do not paraphrase
   to finish the batch.
5. **Run the pre-save sentinel gates** (below), then save.
6. **Verify the live page exactly** (next section) in a separate,
   independent pass while the page is still hidden.
7. **Only after every content check passes:** flip to Public, clear the
   noindex flag in the order in the noindex section, and run the robots
   check on the live page.
8. **Report done only with the named checks that passed** — page by page,
   not as a batch summary.

## Pre-save sentinel gates (necessary, never sufficient)

Before saving, confirm in the body about to be saved:

- Exact correct strings that **must** be present: the expected provider
  names (exact spelling, exact order), credentials, fees, and at least
  the page's key source sentences, copied character-for-character.
- Known-wrong strings that **must be absent**: any name, credential,
  fee, or phrasing that a previous draft or a template default is known
  to sneak in (keep a per-practice list of these and grow it after
  every incident).

Treat these gates as a *pre-save check only*. A paraphrase can contain
every sentinel substring and still be a rewrite — gates passing is
never the verification.

## Verify the live page exactly (independent pass)

Fetch the live page yourself (raw fetch / curl, not the editor preview,
not a reload of the edit screen) and check:

1. **Provider cards, exactly.** Extract the provider-card elements from
   the served HTML and compare the name list against the expected
   ordered list — exact names, exact order, nobody added, nobody
   missing, nobody renamed.
2. **At least 3 exact source sentences.** Probe at least three complete
   sentences from the approved source file, character-for-character,
   on the live page. A page that only matches by substrings or by
   "saying the same thing" has **failed**.
3. **hreflang targets, character-for-character.** Every hreflang href
   must match the expected slug exactly, and the target page must
   exist. A link to a plausible-but-wrong slug is a failure.
4. **Structural negatives.** Inside the styled body block there must be
   **no** top-level heading (`<h1>`), no third-level heading (`<h3>`)
   if your template reserves those for the platform chrome, and no
   lede or table-of-contents block that belongs outside the body.
5. **SEO meta description.** Read it in the SEO Settings tab / served
   `<meta name="description">` separately — body and HEAD-tag sweeps do
   **not** cover it, and a stale description (an old platform, payer,
   or claim) survives both.
6. **Structured data.** Parse every JSON-LD / structured-data block on
   the served page. Keep double-quote characters out of schema *text*
   values: this platform has stripped backslash escapes when serving
   HEAD tags, which turns escaped quotes into broken JSON. Prefer
   single-quoted or quote-free wording inside schema strings, and
   validate the parsed result, not the editor contents.

Report a page as done only after every check above passes on the live
URL. Name the exact checks that passed.

## Clear the noindex flag — in this order

Brilliant Directories checks **Apply NoIndex, NoFollow** for pages
created while protected, and flipping the page public does **not**
clear it. While noindex stands, the page is excluded from the sitemap
and search engines refuse indexing requests for it. The checkbox
cannot be unchecked first, because while a page is Only Allow Members
it is disabled and labelled "(Auto-Applied to Protected Pages)".

Correct order, every time:

1. Flip **Protect Page** to **Public For Everyone**.
2. The checkbox is now enabled (and still checked) — **uncheck
   Apply NoIndex, NoFollow** (Page Options tab → Advanced Options).
3. **Save.**
4. Run **Refresh Live Site**.
5. Fetch the live page and confirm the robots meta tag reads
   `index, follow`:
   `<meta name="robots" content="index, follow">`

A page still serving `noindex, nofollow` after the flip is **not done**,
whatever the editor shows.

## Stop when the editor itself is unreliable

The BD editor's Code View can fail intermittently in automated browser
sessions — clicking it inserts stray characters at the caret, or does
nothing — and saves from those sessions are unreliable in *both*
directions: bodies have been stored as escaped raw HTML text, wiped to
empty, or (on a settings-only save) reverted to earlier content, all
while the session reported success. An editor reload is not evidence:
a body stored as text has the same character count as the intended HTML.

Rules:

- Treat Code View failing, inserting stray characters, or doing nothing
  as an **editor failure**, not an operator error to push through.
- Treat **every save from a suspect session as untrusted** until the
  independent live verification passes.
- **At the second dead end, stop and declare the route broken.** Hand
  the owner a packet — the exact source files plus step-by-step
  instructions for their own desktop browser, or arrange a takeover
  session — instead of burning more attempts on the same route.
- Leave every affected page **hidden** until the content checks pass,
  and not public-ready until the robots check passes after the flip.

## Repair a bad page

- Repair by **wholesale body replacement** from the styled source file.
  Replacement has proven faithful where fresh creation passes rewrote
  the body; small in-editor edits are how errors compound.
- Before replacing the body of an existing page, **capture the full
  current live body as a restore point**.
- Per-page CSS goes in the page-level CSS field as rules only — no
  `<style>` tags — and the markup that uses those classes stays in
  the body.
- Use delete-and-recreate only when wholesale replacement cannot
  restore the page, then run the full hidden-first flow and live
  verification again from the top.
- After a repair, read the saved page back in full in a separate pass
  and diff it against the source file. Keep the page hidden until
  that diff passes.

## Monthly sweep

Once a month, re-fetch every live directory page and re-check:
provider-card name lists against the roster source, robots meta
(`index, follow`), hreflang pairs, structured-data validity, and the
SEO meta descriptions. Pages drift — platform generation, a stray
settings save, a roster change that never reached the page — and the
sweep is what catches an altered page nobody remembers editing.
Record the sweep date, the page count checked, and every mismatch
found and fixed.

## Hard rules (summary)

1. Hidden first, always. Public is the *last* step, after verification.
2. Wholesale replacement from the approved source file. Never
   paraphrase, regenerate, or "tidy up" the source.
3. Batches of ≤ 2 pages, with a stop-and-report order if exact copy
   proves impossible.
4. Sentinel gates are pre-save only. Live verification is independent,
   exact, and done by a separate pass.
5. Flip → uncheck NoIndex → Save → Refresh Live Site → verify robots
   meta on the live page. No exceptions to the order.
6. Second editor dead end = declare the route broken and hand over a
   packet. Do not retry your way out.
7. No page is "done" on a worker's say-so — only on named live checks.
