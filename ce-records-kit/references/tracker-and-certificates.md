# Tracker and certificates

## Tracker schema (one row per course)

A spreadsheet is enough. Columns:

| Column | Source / rule |
|---|---|
| Course Title | From the certificate, verbatim (title variance vs. the reporting system is noted, not "fixed" — see reconciliation). |
| Provider | The CE provider as printed (organization name; keep address/contact when the reporting system asks for it). |
| Date Completed | From the certificate. The cycle filter runs on this. |
| Hours (total) | As granted. Decimals are real (1.75 is common) — keep them exact. |
| Ethics Hours | From the certificate's breakdown; blank/0 when it grants none. |
| Supervision Hours | Same rule. |
| Other Category Hours | One column per additional named sub-requirement on any of the licensee's worksheets (e.g. Cultural Competence). |
| Subject / Competency Areas | As the certificate/reporting system names them (e.g. Professional Practice, Cultural Competence). |
| Delivery Method | Live in-person / live webinar / recorded home-study — method caps run on this. |
| Counts Toward | License(s) this course is verified to count toward (checked against each worksheet's provider/method rules). |
| Certificate File | Link/path to the filed certificate. |
| Reported | Per reporting system: Yes (date verified on transcript) / No. The reconciliation owns this column. |

Totals live in a summary block **per license**: for that license — sum of Hours for rows counting toward it and inside its cycle, and the same sum per category column — set against the worksheet's required numbers, deficits in plain sight. One summary block per license; never a single blended total across licenses.

## Certificates library

- One folder per cycle is a clean convention (`CE Certificates / <cycle start>–<cycle end>/`), or one folder total with filenames that sort by date: `YYYY-MM-DD — Provider — Short Title.pdf`.
- **Every** certificate goes in, including one-time-mandate completions from before the cycle (marked as such) — audits don't care that a file was inconvenient to find.
- Retain for the longest audit window among the licensee's boards, plus margin. The folder + tracker are backed up together; the tracker without the certificates is a claim, not a record.

## Conflict rules

| Conflict | Resolution |
|---|---|
| Tracker row vs. certificate (hours, date, title, splits) | Certificate wins; correct the tracker; note the correction if the row was already reported. |
| Certificate vs. reporting-system entry | The transcript is what the board sees; if the certificate supports more than the transcript shows, the fix is a corrected/supplemented entry per the system's process — prepared by the agent, approved by the licensee. |
| Licensee's recollection vs. either document | Documents win. Memory is how a course gets counted twice or a mandate gets "definitely done" without proof. |
| A course with **no certificate** | It doesn't count until proof exists. Agent's job: chase the provider for a duplicate certificate and log the chase; the row sits in the tracker flagged Unproven and is excluded from totals. |
