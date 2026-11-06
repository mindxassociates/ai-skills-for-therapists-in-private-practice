# Security and privacy

## What the CRM holds — and what it must never hold

Lead data is **contact and routing information about people seeking care**: names, emails, phones, the payor they named, a concern *category*, where they are in your intake pipeline. That is sensitive in aggregate even though no single field is clinical.

Never in the CRM: presenting problems in the client's words, symptoms, diagnoses, session or consult content, clinical risk information, documents. The line is simple — if it would belong in a chart note, it belongs in the EHR, and the EHR is where it goes. The Notes field is for intake logistics ("prefers evenings", "asked for a Mandarin-speaking provider") and even those should be categories and logistics, not quotes.

## Access model

- The **workbook is shared with nobody**. The app runs as the owner; users get data only through the app, only after the gate, only their scope.
- **Gate first, data second:** no board, search, or detail response is produced before the identity token verifies. Tokens expire; a stale token returns nothing but a sign-in prompt.
- **Provider scope is server-side on every call** — board, Agenda, search, detail-by-ID, and every write. A provider who guesses another provider's Lead ID gets the same response as a nonexistent ID.
- **Notes stripping is server-side.** Provider payloads are built from a field whitelist that excludes Notes entirely — verify in testing by inspecting the actual payload, not the rendered page.
- Provider **writes** are limited to their own leads and a safe field set (stage, next action, due, last contact). Identity fields, matched provider, and source are admin-only, enforced on the server even if the client sends them.
- Provider self-add is forced: matched provider = themselves, stage = New, Notes dropped, system sources refused (a human can't create a lead claiming the booking system sent it).

## The feeds' security

- Cross-project hooks authenticate with a shared token kept in each project's script properties — never in code, never in the sheet.
- Ingest reads only the channels it is configured for (sender/subject rules) in the practice inbox; it stores no message bodies anywhere, including logs.
- Sync and Ingest logs are PII-free by contract, so they can be shown in admin panels and debugging output without expanding the exposure surface.

## Retention and deletion

- Exits and stale leads **archive** (30 days in stage; Started at 90 days past consult) — they remain countable and restorable by an admin decision, out of the working board.
- Deletes are **soft** (Trash tab, full snapshot) with a grace purge (default 7 days). Before the purge, deletion is undoable; after it, it's real. Test both halves.
- When a lead becomes a client, keep the CRM row as the intake history pointer (EHR destination + status) — do not bulk-copy anything clinical back into it, ever.
- Decide, and write down, how long archived leads are kept. "Forever" is a decision too; make it on purpose.

## Honest framing

These safeguards *support* HIPAA compliance — access control, minimization, audit via the Activity log. Nothing here certifies compliance, and the kit never claims it. Run the CRM in a Google Workspace with a signed BAA, enforce 2-Step Verification, and put the workbook in the practice's access reviews like every other system that holds client-adjacent data.
