# Test checklist

Run in order, in a browser where you are **not** signed in as the admin (that's what visitors experience).

## Directory

- [ ] Loads with no sign-in and shows every seeded provider, in priority order.
- [ ] **Live-edit test:** change a provider's services in the sheet, reload the directory — the change is there. Add a row by hand — it appears. Delete it — it's gone.
- [ ] **Column-shuffle test:** move a non-core column in the sheet, reload — directory still renders correctly (header-name matching works).
- [ ] Search finds a provider by partial name, by credential, by service, and by location — including the location's full name when the sheet holds the abbreviation (and vice versa).
- [ ] Each filter (type, service, location) narrows correctly, combines with search, and clearing them restores the full list. No-match state shows the plain empty message.
- [ ] A card with a bad/blank photo URL shows the initials tile, not a broken image.
- [ ] **Copy test:** click a photo → paste into a text field → exactly three lines: name, credentials, website. Toast appears. Keyboard: tab to a photo, Enter → same result.
- [ ] "Learn more" opens the provider's website in a new tab.
- [ ] No provider count is displayed anywhere.
- [ ] If the language view is enabled: toggle shows **only** marker-language providers, under their second-language names, with translated UI and working search in both languages; `?lang=xx` opens it directly.

## Add forms (each edition)

- [ ] Submitting with a required field empty is rejected with a readable message and writes nothing.
- [ ] A complete submission succeeds, and the new row sits **at the end of its service-type section** in the sheet — not at the bottom of the sheet (test with a type whose section is not last).
- [ ] The new provider appears in the directory on reload.
- [ ] **Duplicate test:** submit the same name with different capitalization → rejected with the "already in the list" message; no second row.
- [ ] **Email test:** the admin receives the notification with all values, the submitter name, and the sheet link. (If it doesn't arrive, check the manifest mail scope before anything else.)
- [ ] Kill the email deliberately (wrong admin address in a test copy) → submission still succeeds; failure is only in the log.

## Access

- [ ] The sheet itself is shared with nobody; opening its link signed-out shows a request-access page, while the apps work fine signed-out.
- [ ] The directory app has no path that writes: submitting to its URL with form-style parameters changes nothing in the sheet.
- [ ] Each deployment is a single web-app deployment on its original `/exec` URL (no orphaned duplicate deployments from setup).
