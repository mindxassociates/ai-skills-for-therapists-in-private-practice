# Billing — private pay, done completely, and nothing else

## Scope, restated as build rules

| In scope | Out of scope — do not build |
|---|---|
| Fee schedule in Settings (practice-supplied) | Claim submission (837/837P or any portal) |
| Invoice per session or per month | Eligibility / benefits checks |
| Payment link via the practice's processor | ERA/EOB posting, denial workflows |
| Manual payment recording (method + reference) | Payer credentialing or panel management inside the EHR |
| PDF superbill for the client to submit OON | Estimating a client's copay, deductible or reimbursement |
| HSA/FSA-ready receipts (the invoice/receipt itself) | Collecting or storing card numbers in the app |
| Balance view per client + practice totals | Automated dunning beyond a polite reminder email |

If a request crosses the right-hand column, the answer is "that is a different system" — not a workaround inside this one.

## Invoices

- Generated from a completed appointment (or selected appointments) using the client's FeeSchedule profile. Amounts are integer cents end to end; totals are computed server-side from rows, never typed into a total field by hand.
- An invoice is Draft until sent. Sending emails the client a content-light message with the portal/payment link — the amount lives behind the link, not in the email body, matching the kit's minimal-PHI email posture.
- Payments: (a) payment link — the processor confirms payment on its own page; the app records Paid from the processor's confirmation/reference the provider or a webhook-equivalent check supplies; (b) record-only — provider records method label (card/check/cash/transfer), date, amount and reference.
- Partial payments and part-paid status are first-class. Voiding an invoice keeps the row, marked Void with a reason — financial history is never deleted.

## Superbills

Generated on demand (and optionally automatically on payment) as a PDF in Drive, downloadable from the portal. A superbill contains, **all supplied/confirmed by the practice**:

- Practice legal name, address, phone, tax ID
- Provider legal name, license, NPI
- Client name, date of birth, address
- Date(s) of service, place-of-service / telehealth modifier as the practice directs, CPT code(s), diagnosis code(s) recorded for the session, fee charged and amount paid
- Provider signature block

Diagnosis and procedure codes come from the session/note record as the provider entered them. The system never suggests, defaults or invents a code. If a required element is missing, generation stops and names the missing field — a superbill with a guessed code is worse than no superbill.

The superbill is a document *for the client* to submit. The practice does not submit it, track the claim, or predict its outcome; portal copy says exactly that.

## Money hygiene

- Fees change in Settings with an effective date; invoices already issued keep the amounts they were issued at.
- Practice totals (collected this month, outstanding balances) are computed at read time from invoice rows for the requested window only — never by scanning all history on every screen load (see scaling reference).
- Every invoice state change is audit-logged.
