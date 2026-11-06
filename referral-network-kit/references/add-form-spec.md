# Add form spec — internal and public editions

Two Apps Script projects with **identical server logic**, differing only in title, intro copy, and the admin email subject. Build one, then copy the project for the other edition. Each: `Code.gs`, `Index.html`, `appsscript.json`; deployed **Execute as: owner**, **Access: Anyone**, `ALLOWALL` for embedding.

## Form fields

All fields required except "Your Name".

| Field | Control | Maps to column |
|---|---|---|
| Service Type | radio group (the configured types) | `Service Type` |
| Provider Name | text | `Provider Name` |
| Credentials | text | `Credentials` |
| States Licensed In | text (label it for your geography) | `States` |
| Services Offered | checkbox group (small fixed vocabulary: Individual / Couples / Family Therapy, Medication Management, …) | `Services Offered` (joined with `, `) |
| Website | URL input, with a hint: "Paste the full link starting with https:// — this is the page clients will land on." | `Website` |
| Profile Picture URL | URL input, hint: a public link to the photo that should appear on the card | `Profile Pic` |
| Languages | text | `Languages` |
| Your Name | text, **optional** — "So we know who sent the recommendation" | not stored in the sheet; appears in the admin email only |

Intro copy states the listing's meaning and the consent rule in one or two plain sentences, e.g.: *"Add a colleague you know and recommend. Please only list someone who knows they're being recommended."*

## Server: `submitProvider(data)`

1. **Normalize:** trim every string field.
2. **Validate:** service type must be one of the configured types; all required fields non-blank. Return `{success:false, error}` with a human message — no partial writes.
3. **Duplicate guard:** scan the name column; if any row's name equals the submitted name case-insensitively (trimmed), return `{success:false, error: "<Name> is already in the recommendations list."}`.
4. **Section-grouped insert:** find the last row whose `Service Type` equals the submitted type; `insertRowsAfter` that row (fallback: right below the header) and write the 8 core columns in one `setValues`. Never append a row at the very bottom unless its section is last — the sheet stays grouped by type.
5. **Admin email:** send to the configured admin address with every submitted value, the submitter's name if given, a timestamp, and a link to the sheet. Subject differs by edition:
   - Internal: `New Referral Network Provider — <Name>`
   - Public: `New Recommended Provider — <Name>`
   Wrap the send in try/catch and log failures — **email failure never fails the submission**.
6. Return `{success:true}`; the form shows a plain confirmation and offers "add another".

## Client behavior

- Validate required fields in the browser too (fast feedback), but the server re-validates everything — the client is never trusted.
- Disable the submit button while the call runs; on error, show the server's message verbatim and keep the entered data; on success, reset the form.
- Small "i" hint affordances on fields whose value has a consequence (Website, Profile Picture URL). Hints explain, they don't decorate.

## Editions at a glance

| | Internal ("Build Your Referral Network") | Public ("Get Recommended by <Practice>") |
|---|---|---|
| Audience | Own clinicians | Community colleagues |
| Framing | "Add a colleague to our shared referral network" | "Add yourself or recommend a colleague" |
| Distribution | Internal portal / providers only | Public community page |
| Trust default | Trusted; admin still gets the email | Unvetted; admin reviews via the email before treating the listing as settled |
