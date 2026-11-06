

# Insurance Payer Credentialing

## Purpose
Help a solo or group practice credential providers directly with insurance payers using a repeatable, auditable workflow. This skill prepares submissions; it never sends or submits without explicit approval.

## Workflow
1. **Confirm the practice profile.** Record, with placeholders where needed:
   - Practice legal name, DBA/trade name, entity type
   - Group (Type 2) NPI if a group practice; otherwise individual NPI
   - Tax ID / EIN
   - Credentialing contact name, admin email, office phone, website
   - Provider documents folder (licenses, liability COI, CVs)
2. **Build the per-provider checklist.** Before any submission, collect:
   - [ ] Current professional license proof for every licensed state (PDF)
   - [ ] Malpractice / professional liability certificate of insurance (PDF)
   - [ ] Resume or CV (PDF)
   - [ ] Individual NPI
   - [ ] CAQH ID and confirmed current attestation when required by the payer
   - [ ] Business phone and email for credentialing/referral contact
   - [ ] Telehealth location: city / state / ZIP
3. **Choose the payer workflow.** Use the appropriate section below. Do not invent payer URLs or recipient addresses; confirm the payer's current published submission route first.
4. **Prepare the submission packet.** Draft every field, recipient, attachment, and send channel for review. Show the exact values before anything is sent.
5. **Submit only after explicit approval.** After approval, submit/send and capture the observed result (confirmation page, sent-mail record, reference number, or blocker).
6. **Log the outcome.** Record date, provider, payer, confirmation/evidence, or the exact blocker. Keep provider names; never retain client PHI.

## Payer workflows

### CuraLinc Healthcare (EAP) — online intake
- Intake route: use CuraLinc's current online provider intake form; confirm the published URL before starting.
- Questions contact: use the payer's published credentialing contact.
- Rules: one submission per provider; complete all fields; many intake forms have no save-as-draft, so finish in one sitting.
- Typical prerequisites: behavioral-health/health-services degree; post-degree supervised experience as specified by the payer; required malpractice limits; current unrestricted license; licensed to practice without supervision.
- Typical field map:
  - Personal: legal first/last name, NPI if applicable, practice legal name, Tax ID
  - Contact: credentialing/referral email and phone
  - Office: practice name; telehealth-only flag if applicable; city/state/ZIP even for telehealth; work phone
  - Licenses: enter the primary state license block; add extra states through the payer's additional-license mechanism
  - Liability: carrier name, policy number, expiration, aggregate/per-occurrence limits as plain numbers
  - Practice details: care delivery methods, specializations, populations, languages, services, modalities, insurance panels
  - Uploads: license proof(s), liability COI, resume/CV; confirm accepted file formats (many CuraLinc uploads are PDF-only)
- After submitting: watch for any required follow-up forms (for example, a provider disclosure form); activation often takes 1+ months and is only real after the payer's welcome/activation email. If the form stalls on submit, do not click submit twice without explicit approval; wait, verify receipt with the payer, or retry only with approval.

### Curative Health Plan — roster email
- Prerequisite: confirm the provider's CAQH attestation is current before submitting.
- Maintain a group provider roster for the payer; additions typically include: add/change action, effective date, group tax ID, taxonomy, specialty, practice/group/pay-to/tax block, credentialing contact, ages served, licenses, and CAQH ID.
- Send an email from the practice's credentialing email to the payer's published credentialing contact:
  - Subject names the practice and the roster addition
  - Body states the attached updated roster adds the provider(s), with NPI and CAQH for each
  - Attach the current roster spreadsheet

### AllOne Health (EAP) — email application
- Recipients: use the payer's published provider-relations/credentialing contacts; confirm CCs from the payer's current instructions.
- Subject: provider application naming the clinician.
- Attachments: completed payer application/info page, resume/CV, professional liability COI, license proof for every applicable state.
- Body: brief cover note identifying the clinician and practice, listing attachments, and inviting requests for additional information.

## Output Contract
For each provider × payer submission, produce:
- A complete submission packet: payer, submission route, recipients, every entered value, attachments, and send channel.
- A review-ready draft (form values, email text, or message) shown to the user before approval.
- An outcome log entry: date, provider, payer, confirmation evidence or blocker.

## Operating Rules
1. Show exact recipients, all entered values, and every attachment before sending or submitting.
2. Never send or submit without explicit user approval; drafting or filling a form is not approval.
3. Never claim completion until the result is observed (confirmation page, sent-mail record, reference number, or payer reply).
4. Keep provider and practice data; never retain client PHI.
5. If a payer's published route, recipient, or requirement has changed, confirm it before proceeding; do not reuse stale instructions.
6. Prefer primary payer sources (payer portal, published instructions, payer emails) over summaries.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.
