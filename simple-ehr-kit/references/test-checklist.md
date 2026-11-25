# Test checklist

## Harness (fixtures must be live-shaped)

Fixtures must use **real date cells** (not date-shaped strings), empty amount/score cells, a signed note with an amendment, an archived client, and at least two providers with overlapping client first names — the defects that bite in production hide in exactly those shapes.

- [ ] Provider gate: correct PIN opens; 5 wrong attempts lock for 15 minutes; disabled provider cannot sign in.
- [ ] Scoping: provider A cannot load provider B's client by guessing the ClientID; a client token loads only its own client; a revoked token loads nothing.
- [ ] Clients: add / edit (ID and portal link unchanged) / archive / discharge; blanks on a partial edit preserve on-file values.
- [ ] Appointments: create writes workbook row + calendar event with matching times **in the labelled timezone**; reschedule moves both; cancel keeps the row as Cancelled; reminder stamps once and does not re-send.
- [ ] Notes: template renders its fields; carry-over copies only flagged fields and labels them copied; draft auto-saves; signing freezes the file (a later save attempt is refused); amendment appends and displays with the original; hash on the index matches the signed file.
- [ ] Intake: partial save returns and resumes; required-field completion flips IntakeStatus; a resubmission with blanks does not erase chart data.
- [ ] Billing: invoice totals equal the sum of its session rows in cents; part-payment → PartPaid; payment link flow records Paid with a reference; void keeps the row; superbill generation stops and names any missing required element, and never invents a code.
- [ ] Export: one client's export contains their notes, intakes, invoices and superbills — and no other client's files; the export is audit-logged.
- [ ] Archive: a closed year rolls to its archive workbook with matching row counts; the live workbook no longer carries it; a per-client history lookup still finds it on demand.
- [ ] Transport sweep: every server function returning data is called against fixtures containing real dates and empty cells, and returns a non-null payload every time.

## Live click-test (served page, real browser)

With a throwaway provider and a throwaway client, in order:

1. Sign in as the provider; Today shows today's test appointment.
2. Open the client from Today; start a note from the appointment; carry over from the seeded prior note; sign it.
3. Generate the invoice; open the portal link in a private window; see the appointment, the invoice and (after generating) the superbill — and nothing clinical.
4. Complete one intake form on a phone-sized viewport; confirm it lands in the chart.
5. Regenerate the portal token; confirm the old link is dead and the new one works.
6. Time the main screens on the practice's real connection; if Today or Clients feels slow, run the scaling reference before adding data — not after.

Clean out all test providers, clients, notes, invoices and files when finished, and note the cleanup in the audit log.
