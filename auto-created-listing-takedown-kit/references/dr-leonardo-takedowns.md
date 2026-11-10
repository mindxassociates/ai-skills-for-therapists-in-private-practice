# Dr. Leonardo takedowns

Dr. Leonardo Interactive Webservices, LLC auto-builds a full mini-website for clinicians from NPPES data — millions of them (its own directory is at `https://sitebuilder.dr-leonardo.com/directory`). Unclaimed pages display office hours the operator admits it **assumed** (typically Monday–Friday 9:00–5:00, weekends closed) plus an appointment-request widget. The operator's own FAQ describes the removal route: you "claim" the listing and set the delist toggle. Claiming is the vehicle; **removal is the only goal**.

## Finding the page

1. Try the obvious subdomain: `https://<legalfirstname><legal lastname>.dr-leonardo.com` (all lowercase, no spaces) — e.g. built from the NPPES legal name, not a preferred name.
2. Open it and confirm **name + NPI** match your clinician. Discard same-name pages (other professions, other NPIs) without touching them.
3. If the obvious subdomain 404s, do **not** conclude there is no page. Subdomains are often suffixed or mangled (extra letter strings appended to the name; a mononymous clinician may appear with an "unknown" first-name prefix). Use the claim site's provider search:
   - Start at `https://sitebuilder.dr-leonardo.com/start/claimmyprovidersite` (or the CLAIM flow on provider-pages.com) and search by the clinician's **NPI** — search by state + name if NPI search is unavailable, trying the license states and the NPI mailing state.
   - A search can return several same-name clinicians; submit only for the record whose NPI matches exactly.
4. If a full search (all plausible states + a web search for the name + `dr-leonardo.com`) finds no record, report "no page found" for that clinician. That is a real result.

## Submitting the takedown

Open the claim form for the page:
`https://sitebuilder.dr-leonardo.com/start/claimmyprovidersite?referral_site=https://<subdomain>.dr-leonardo.com`

Set:

- **Takedown Request — "Remove/Delist Your Provider-Page?" → Yes** (bottom of the form).
- **"Does Your Provider-Page Need to be Corrected or Updated?" → No.**
- **Email** → the claim address for *this* clinician (see the email rule below).
- **Reason for Removal** → the practice's standing choice from the forced list (the options are things like Office Closed/Retired; Not Accepting Patients; Research — Do Not See Patients; Not a Healthcare Organization; Practice/Health System Does Not Allow). None may be literally true; pick the practice's standing option in the setup interview and use it for every clinician, consistently.
- **Paid services → none.** Do not subscribe to scheduling, patient portal, or any premium offer.

Submit. The confirmation banner reads: *"Almost done! To finalize, check your inbox for our verification email and click on the validation link to complete your submission."* The takedown is **pending** until the link is clicked.

## The email rule (learned the hard way)

**One email address can be used for exactly one Dr. Leonardo claim.** Reusing the address that filed a verified claim gets the next submission rejected with: *"This email is already used on a verified Provider-Page claim. Please enter a different email address."*

For a group practice, assign each clinician a unique address up front — per-clinician addresses at the practice domain (e.g. `firstname@yourpractice.com`) or plus-addresses — all delivered to / monitored from the one admin inbox that receives the validation emails. Never reuse the practice admin address for a second clinician.

## Validation

- The verification email comes from `no-reply@dr-leonardo.com`, subject *"Verify Email for https://<subdomain>.dr-leonardo.com TakeDown"* — **check the spam folder**; that is where it lands.
- Open the **"Verify & Remove"** link. A successful validation redirects to the claim page with a banner such as *"Site takedown request sent successfully"* or *"Site takedown already requested"* (the latter also means a validated takedown is on file). The operator may also send a *"CONFIRMATION of Takedown"* email afterward — save it.
- **Token gotcha:** the validation link must be opened byte-for-byte. Links extracted carelessly from the email HTML can pick up a trailing `"` (from the href attribute), which makes the token arrive with a `%22` suffix and the site answers *"Invalid token: Please try claiming your provider site again."* If that happens, extract the clean URL from the raw message (decode the quoted-printable body, take the href value exactly) and open that — do not re-claim.
- The email also contains a temporary password for the claim account. You should not need it for a takedown; do not use or store it unless the flow forces a login.

## After validation

- The operator states removal + Google de-indexing can take **up to 72 hours**. Revisit the URL after the window and record gone / still live.
- A still-live page after 72 hours goes back into the monthly sweep with a fresh takedown.

## Abuse reports for this operator

Worth the full set (`abuse-reports.md`): FTC, Google Search Quality, host (the pages are served via AWS S3 + CloudFront — report to AWS Trust & Safety), and registrar (eNom — abuse@enom.com; confirm via RDAP for the domain). Cite the fabricated hours and the operator's own "assumption" admission.
