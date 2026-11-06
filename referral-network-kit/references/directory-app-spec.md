# Directory app spec — the public, read-only directory

One Apps Script project: `Code.gs` (reader), `Index.html` (cards + search + filters), `appsscript.json`. Deployed **Execute as: owner**, **Access: Anyone**, `XFrameOptionsMode.ALLOWALL` for website embedding.

## Server: `getProviders()`

- Opens the sheet by ID (config constant), reads the full data range.
- **Matches columns by header name**, case-insensitive, trimmed, with aliases: `Website`/`Webiste`; `Profile Pic`/`Profile Picture`/`Photo`; `States`/`Location`/`Locations`/`Region`/`State/Province`/`Country`; `Languages`/`Languages Spoken`; `Priority Level`/`Priority`. Missing optional columns return `''`, never throw.
- Skips rows with a blank provider name.
- Returns one object per row, **in sheet order**: `serviceType, name, credentials, states, services, website, pic, languages, slidingScale, priority`, plus `chineseSpeaking`-style flag if the language view is enabled (compute server-side from the Languages value against the configured marker list).
- No caching, no writes, no email. A page load is a sheet read — that's the freshness guarantee and it's acceptable at directory scale.

## Client: rendering

- **Cards in a responsive grid.** Each card: photo (rectangular, ~4:3, `object-fit: cover`, top-anchored), name, credentials, service type, location, services, languages, sliding-scale line if present, and a "Learn more" link to the website.
- **Photo fallback:** if the URL is blank or the image errors, show an initials tile in the same frame — never a broken-image icon.
- **Ordering:** sort by `priority` ascending (blank/non-numeric last), stable within a level so sheet order still speaks.
- **Do not show a provider count.** A directory's size is not a quality signal and a small network shouldn't look small.

## Search and filters

- **Search box** matches, case-insensitively, across: name (both languages' names), credentials, services, languages, and location text. Location aliases are worth the effort: a visitor may type the full state/region name or its abbreviation, in either UI language — keep a small alias table for the locations your network actually covers and match both directions.
- **Filters** (dropdowns, options built from the data, not hard-coded):
  - Service type
  - Service offered (split the joined `Services Offered` values)
  - Location (split the location values; exclude non-place values your data uses as qualifiers — e.g. a provider listed as "Worldwide" shouldn't become a pickable "location" unless you want it to)
- Filters and search combine (AND). An empty result shows a plain "No providers match your search." — no suggestions, no upsell.

## The copy gesture (the point of the directory)

- **Clicking a provider's photo copies three lines — name, credentials, website — to the clipboard**, with a toast ("Copied — paste it into your message/note"). Keyboard accessible: the photo is focusable and Enter/Space does the same; `aria-label` says what it does.
- Why: the directory's real job happens in another window — a clinician pasting a referral into a client email or note. One click that produces exactly the paste-able text is worth more than any other feature on the page. Put the explanation behind a small hint affordance, not a visible tip line.
- Copy failure (browser denies clipboard) → toast says so plainly.

## Optional second-language view

- A small EN / language toggle in the header.
- In the second-language view: **only providers whose Languages value contains one of the configured markers** (e.g. for Mandarin: `mandarin, cantonese, chinese, 普通话, 粤语, …`) are shown, under their second-language name when the sheet has one (fallback: English name), with the full UI translated — including search, which matches names/services/languages in both languages in both views.
- The view is selectable via URL parameter (`?lang=xx`) so the practice can link directly to it from its second-language pages.

## Style

- Clean, professional, mobile-first; the practice's own palette and name. No platform branding, no emoji in the UI. Loading state while the sheet read runs; a plain error message if it fails (never a stack trace or a blank page).
