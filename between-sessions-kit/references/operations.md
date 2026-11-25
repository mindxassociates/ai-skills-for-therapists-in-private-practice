# Operations

## Day-2 operations

**Add a provider.** Assign the stable ProviderID first and add the roster row (ID + name) *before* any access step — the ID is the join key everywhere. Seed/sync the Providers tab with their PIN hash (from the roster's PIN scheme, or an admin-set initial PIN they change later). They appear in the gate picker by display name automatically. Retired IDs are never reused.

**Add a catalog item.** Author the steps (both languages, if bilingual — see `catalog-format.md`), add the item to the catalog source, regenerate, run the harness sweeps, deploy, create its public page (hidden → verified → public), and run the parity check. An item is not "added" until a client can open it from its public URL.

**Custom exercises (providers, in-app).** Draft in the step builder → Publish (now assignable; optionally practice-shared) → Retire when done — or Delete outright while it is a draft, retired, or never assigned; once it has assignments it can only be retired, and assignment history is never deleted. Drafts edit in place; published items fork on edit. If a published custom "doesn't appear" in the assign library, suspect the provider page's session catalog cache first — the server merges customs at read time; invalidate the cached catalog when a custom is published/retired (the reference build shipped exactly this stale-cache bug).

**Clients.** Edit in place for typos, email changes, timezone moves — issued links keep working because ID and tokens don't change. Archive when a client pauses (reversible — provide Unarchive; a one-way archive door *will* generate support mail). Hard-delete only test/duplicate rows: the cascade removes instances, results, assignments, then the client, and audits the counts.

**Review routine.** The flagged queue is the daily list: crisis-adjacent submissions — and any result a provider flags manually — wait there (and on the dashboard count / portal bell) until a provider opens the detail — prompt → answer pairs, never raw JSON — and marks reviewed. One stamp clears all three surfaces. Export is a provider-scoped CSV of the same filtered rows; the server re-checks ownership per row.

**Backups and restore.** Weekly copies land in the backups folder (keep 4). Restore = make a copy of the backup workbook, verify its tabs/headers, and point the app's configured workbook ID at it (or copy its data back) — then run the click-test stages before telling providers it's back. Code restore points (per deploy) live with the project source; a code rollback is a re-push of the restore-point tree + a new version on the same deployment.

**Retire an item.** Remove it from the catalog source (deploy) *and* delete/unpublish its public page; verify the URL 404s and the parity check is clean. Existing assignments of a retired catalog item stop resolving — end them first, or keep the item and mark it unassignable instead.

## Troubleshooting — from real incidents, generalised

| Symptom | Likely cause | Fix |
|---|---|---|
| A whole view (Summary / Review) never renders; no error anywhere | A `Date` or `NaN` in that function's payload nulled the transport (Sheets auto-converted a date-shaped cell; an empty score became `NaN`) | Coerce date-shaped fields to text and optional numbers via clean-number before returning; add null guards that render a visible in-view error. Reproduce with the **live-shaped row**, not string fixtures |
| "Nothing happens" when confirming an assignment — but a duplicate assignment exists | The click *did* succeed: the result card rendered below the fold / looked identical to the previous one, and the provider clicked again | Check the Audit tab before assuming failure. Fix the feedback: busy label on the button, clear the old result at click time, scroll the new card into view, validate edge inputs (no days/dates/times) client-side with a banner next to the wizard |
| Assignment creation takes minutes | Whole series materialised row-by-row | 60-day window + one bulk write + nightly top-up (`reminder-engine.md`) |
| Client did the work early; a reminder still went out; adherence dropped | Submission didn't credit a pending instance; engine sent anyway | Crediting at save time (earliest pending) + the engine's covered-work guard, incl. legacy uncredited results |
| Reminders show the wrong hour after a move / DST change | Times read in the provider's (or server's) zone instead of the client's | Client-zone wall times + epoch storage + zone-labelled displays (`reminder-engine.md`) |
| Client link opens a page asking for a token / shows the wrong item | The public page didn't forward its query string into the embed iframe | Head-tags passthrough script; verify with a real `?t=` link end-to-end (`architecture.md`) |
| A published custom exercise is missing from the assign library | Provider page's session catalog cache is stale (server side is correct) | Invalidate the catalog cache on publish/retire and after any catalog deploy |
| New capability (e.g. backups) silently does nothing after a scope was added | The owner's old grant covers only the old scopes; new-scope calls fail inside try/catch | Re-authorize (remove the stale grant if the prompt won't appear), then verify the capability itself — an actual backup file — not just the consent |
| App serves 403 right after creation | API-created project not yet authorized by the owner | Owner opens the editor once, runs the setup function, accepts consent (also creates the triggers) |
| Chinese UI shows English for one item / one label | That item's fields (or its category, or its gentle note) lack authored translations | Author them; check all three leak points — item fields, category map, note fields — and that the payload actually carries the translated field |
| Provider list / gate picker empty | Providers tab not seeded, or seed copied the wrong columns | Seed from the roster's PIN-hash + token columns exactly as stored; never invent PINs |
| A page on the public site shows literal HTML tags | The CMS editor stored the body as escaped text (a known visual-editor failure mode) | Re-paste via the editor's code view, reload the editor to confirm the body is intact, then verify the **public** page — editor reload alone is not evidence |
