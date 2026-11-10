# The monthly sweep

Auto-created pages come back. Operators re-import NPPES data, mirrors re-scrape, and a removal that worked in January can be live again in March. A short monthly sweep keeps the inventory true. Schedule it (cron / recurring task) for a fixed day each month, in the practice's local time, reporting to the practice admin in chat or email.

## Each run

### 1. Re-check every known URL

For every entry in the inventory (Dr. Leonardo page per clinician; the clinician's Healthgrades / WebMD / npiprofile / usadb / datalabs / Topline listings):

- Fetch the URL. **Gone** (404, delisted notice, profile removed) → mark REMOVED with the date.
- **Still live** after a previously validated takedown → the page resurrected or never came down: re-file the removal through the site's playbook (for Dr. Leonardo, a fresh claim-to-delist with that clinician's own claim address + validation click) and file a fresh Google spam report if the page is deceptive.
- **Live but never removable** (policy or no-route sites) → note status only; re-send the standing removal request where the playbook says to (e.g. Healthgrades Contact Us).

### 2. Check the validation inbox

Dr. Leonardo and similar flows validate by email. Search the admin inbox (including **spam**) for new verification emails from the operators for any claim filed since the last run, and open every outstanding validation link. A takedown older than a few days that was never validated is not a takedown — validate it or re-file.

### 3. Scout for new pages

For each clinician: web-search the **NPI number**, the **legal name**, and the **preferred name + credential**. Review results for auto-created pages not already in the inventory. Skip legitimate/managed listings (practice sites, claimed directories, licensing boards, NPPES). For each genuinely new page:

- Verify name + NPI; discard same-name strangers.
- Submit removal via the site's published route if one exists; file a Google spam report if deceptive.
- Add it to the inventory with the date found and the action taken. New sites with no removal route get reported in the summary as such.

### 4. Report once

One summary per run, in this shape:

- **Still removed:** count + any changes since last run.
- **Re-removed this run:** site, clinician, what was filed, validation status.
- **Still live:** site, clinician, why (awaiting operator window / policy refusal / no route), and the next step.
- **New pages found:** site, clinician, action taken.
- **Needs a decision:** anything the standing instructions don't cover — a new forced-choice reason list, a site demanding payment or account creation, a claim-and-correct judgment call. Flag it; never improvise.

Log the run (date + outcomes) wherever the practice keeps the inventory, so next month's run starts from the last verified state.

## Standing parameters to set once

- **Clinicians covered** + legal names + NPIs (rebuild from the practice roster each run if the roster lives in a sheet/doc the agent can read — practices change).
- **Claim addresses** — one per clinician for Dr. Leonardo; never reuse across clinicians.
- **Standing removal reason** for forced-choice forms.
- **Legitimate listings** to always skip.
- **Authority** — the sweep may re-file removals and spam reports for *known* pages without asking; anything new or ambiguous is reported, not acted on beyond a first removal request through a published route.
