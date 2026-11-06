# Security and privacy

## What's public — by design

The directory is a public page and every field in it should be treated as published: provider name, credentials, locations, services, languages, website, photo. All of it is information the listed clinicians already publish about themselves. Design rule: **if a field shouldn't be public, it doesn't go in the sheet.**

## What never goes in the sheet

- **Client information of any kind.** No client names, no "referred Jane D. here", no case notes. The referral itself happens elsewhere (email, EHR); the directory only answers "who do we recommend for X?"
- Personal contact details a colleague hasn't published professionally (personal email, cell phone).
- Private assessments ("great but slow to reply", fee gossip). If the admin keeps a private notes tab, it lives in the same workbook — which raises the stakes of the sharing rule below. Prefer keeping even notes out.

## Access model

- The **sheet is shared with nobody**. The apps run as the owner ("Execute as Me"), so neither visitors nor submitters need — or get — access to the underlying data file.
- The **directory app** is Anyone-access and read-only; there is no write path through it, and no code path in it that returns more than the card fields.
- The **forms** are Anyone-access at their URLs; the internal form's URL is distributed internally, but treat it as unlisted, not secret — its protection is the duplicate guard plus admin review of every submission, not obscurity. If your internal form is abused, the fix is process (review + delete) or moving distribution, not passwords on a public web app.
- Deployments: web app, Execute as owner, Anyone. Do not deploy as "User accessing the web app" — visitors have no access to the sheet and every load would fail.

## Consent and review

- The forms state that a colleague should be listed **with their knowledge**. The submitter attests by submitting.
- The **admin email is the review gate**: every submission is seen by a human. For public-form submissions especially, confirm the listing is real and welcome before it is treated as settled; remove anything that isn't.
- Removal is deletion of the row, effective on the directory's next load. Offer it plainly ("listed by mistake? contact us") if your community expects it.

## Honest framing

A listing means "our clinicians know and refer to this colleague" — it is not credential verification, not an endorsement of outcomes, and not a guarantee of availability or insurance participation. Directory copy should say the first and imply nothing stronger. Do not present the directory as HIPAA anything — it contains no health information, and claiming otherwise confuses everyone.
