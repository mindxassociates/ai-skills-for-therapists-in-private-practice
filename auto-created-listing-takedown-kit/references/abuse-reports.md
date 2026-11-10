# Abuse reports

Removals fix your page. Abuse reports attack the pattern — millions of pages built the same way. File the full set for the worst offender (Dr. Leonardo is the archetype); file selectively for smaller mirrors. Every report uses the same evidence core:

- The page URL and the clinician's name + NPI.
- What the page fabricates: office hours never provided, specialties never held, a wrong city, "accepting new patients," an appointment widget for a practice the operator doesn't run.
- The operator's own words, if published (Dr. Leonardo's FAQ admits that for unclaimed pages it is "forced to make an assumption" about office hours).
- The date you requested removal through the operator's own route, and that the page was created without consent or notification.
- Complainant block: clinician legal name, practice legal name, practice address, phone, contact email.

Keep every case/reference number in the inventory.

## 1. FTC — ReportFraud.ftc.gov

File at https://reportfraud.ftc.gov as a consumer report about the company's deceptive practice (this is a report, not a complaint that gets individually investigated — say so to the clinician).

- Category: if no impersonation/deception category fits cleanly, "Something else" works; describe the pattern in the narrative.
- Report the **company** (legal name + domain + phone from its site), complainant = the clinician on behalf of the practice, amount lost $0, date = today.
- Narrative skeleton: *"The company automatically creates public websites for healthcare clinicians from scraped NPI records, without consent or notification. My page, [URL], publishes office hours I never provided ([quoted hours]) — the operator admits it 'assumes' hours for unclaimed pages — and solicits appointment requests for my practice, which the operator does not run. Its directory lists millions of similar unclaimed pages that rank in Google results for clinicians' names and mislead prospective patients. I requested removal through the company's own process on [date]."*
- Save the **Report Number** from the confirmation page.

## 2. Google Search Quality — spam report

File at https://search.google.com/search-console/report-spam (sign in as the practice's Google account).

- Category: **"The page is deceptive" → "Misleading functionality"** fits a page pretending to be the clinician's site with a fake appointment function.
- Example search query: the query a patient would type — `"<Clinician Name> <credential> <City>"`.
- Details (~280 characters is plenty): *"[Site] auto-created this clinician page without consent. It publishes fabricated office hours (Mon–Fri 9–5) the operator admits it 'assumed,' plus a fake appointment widget. Millions of these doorway pages rank for clinicians' names. Takedown requested [date]."*
- Google gives no case number; it may email a "report submitted" confirmation. Note the form's warning: comments may be shared with the site owner if Google takes manual action — another reason to keep the text purely factual.

## 3. Host / CDN abuse desk

Find the infrastructure first: fetch the page and note the serving stack from response headers (Dr. Leonardo's provider pages are served from **Amazon S3 + CloudFront**).

- AWS: email **trustandsafety@support.aws.com** (or the AWS abuse form). Subject: *"Abuse report — unauthorized provider page with fabricated information hosted on AWS (<page domain>)"*. Body: the evidence core + the removal-request date + a line asking AWS to review under its Acceptable Use Policy. Save the case reference AWS replies with.
- Other hosts: use the host's published abuse contact/form with the same text. If the host is hidden behind a CDN, report to the CDN as well.

## 4. Registrar abuse desk

Find the registrar via RDAP for the domain (e.g. `https://rdap.db.ripe.net/` style endpoints or any whois/RDAP lookup): Dr. Leonardo's domain registrar is **eNom, LLC**, abuse contact **abuse@enom.com**.

- Email the registrar's abuse contact. Subject: *"Registrar abuse report — <domain>: millions of unauthorized clinician pages with fabricated information"*.
- Body: the evidence core, plus what you have already done — *"I submitted the operator's own takedown request on [date], filed FTC Report #[number], and reported the hosting to [host] on [date]. I am asking [Registrar], as registrar, to review this domain's deceptive use under its registration agreement and abuse policies."*
- Registrars rarely act on content alone; file it anyway — the paper trail matters and costs five minutes.

## What not to do

- Don't file abuse reports against legitimate directories, the practice's own listings, or NPPES.
- Don't embellish. Fabricated hours + no consent + millions of pages is the story; invented harms undermine it.
- Don't expect individual redress from the FTC or Google reports — they are pattern evidence. The removal route is what takes your page down.
