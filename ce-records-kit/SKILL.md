---
name: ce-records-kit
description: Keep a clinician's continuing-education records renewal-ready across one or more licenses. Use when a therapist wants (1) a verified requirements worksheet per license (board, cycle dates, total hours, ethics/supervision/other sub-requirements, one-time mandates, method rules, reporting system) built from the board's current published rules; (2) a single course tracker whose rows come from the actual certificates, which are the source of truth; (3) reconciliation against the official reporting system (CE Broker or the state's equivalent) — audit the transcript, enter only missing courses, re-verify totals category by category; and (4) periodic status reports that show each sub-category's deficit separately, never just a grand total. The agent prepares and enters records but never attests, certifies, or submits a renewal in the licensee's name.
---

# CE Records Kit — Continuing Education, Renewal-Ready

## What this system is

A workflow, not an app: **requirements worksheets → one tracker → a certificates library → reconciliation against the official transcript → status reports**. It runs in whatever the clinician already uses (a spreadsheet for the tracker, a Drive/Dropbox folder for certificates, the board's reporting system online). The agent does the gathering, math, diffing, and data entry; the licensee owns every attestation.

The failure this prevents is specific and common: renewal arrives, the official transcript is short — not on total hours, but on a **sub-category** (ethics is the classic), or half the courses were never reported, and the proof is scattered across email receipts and download folders.

## Instructions for the agent

- **Every requirement number comes from the board's current published rules**, found and cited at setup — never from training data, never from the licensee's recollection, never carried over from last cycle unverified. Rules change between cycles; treat last cycle's worksheet as a draft to re-verify line by line.
- **The certificate is the source of truth** for a course's title, provider, completion date, and hours — including sub-category splits, which providers print on the certificate and trackers routinely get wrong. Tracker-vs-certificate conflicts are flagged to the licensee and resolved in the certificate's favor.
- **Enter only what's missing.** The reconciliation starts from the official transcript, not from a blank form. Duplicates in an official reporting system are their own mess; don't create them.
- **Never attest.** No checking "I certify," no signing, no submitting a renewal, no completing a required training in the licensee's name. Prepare everything up to the signature line and stop.

## Setup (once per license, re-verified each cycle)

Build the worksheet in `references/requirements-and-categories.md` for **each** license:

1. Board + license type + license number (kept in the worksheet, which lives with the clinician's private records).
2. Current cycle start/end dates and the renewal deadline (they are not always the same date — record both).
3. Total hours required.
4. Every sub-requirement with its own minimum: ethics, supervision, cultural competence/diversity, telehealth, diagnosis-specific — whatever this board names.
5. One-time mandates (e.g. human-trafficking prevention, suicide prevention, implicit bias) with completion status — one-time means once ever, but only if the board says so; verify.
6. Method/delivery rules: live vs. home-study caps, board-approved-provider requirements, whether out-of-state or national providers (e.g. large CE platforms) count.
7. The reporting system of record (CE Broker, a board portal, self-report with audit) and how the transcript is obtained.

## The standing workflow

1. **Capture at completion.** Each finished course becomes a tracker row from its certificate the week it happens (the licensee drops the certificate in the folder; the agent files and logs it). Batch-entering two years of courses at renewal time is the failure mode this step exists to prevent.
2. **Periodic status** (quarterly is a good rhythm, monthly in the final quarter of a cycle): per license — banked vs. required for the total and each sub-category, cycle days remaining, named deficits, and courses that count toward multiple licenses flagged so one enrollment can close two gaps.
3. **Reconciliation** (at least once mid-cycle and once before renewal): transcript ↔ tracker diff → approved entry list → entries made → transcript re-pulled → totals verified per category. See `references/reporting-system-reconciliation.md`.
4. **Renewal packet:** when totals verify complete, assemble the renewal checklist (transcript proof, any one-time-mandate certificates, fee, the renewal itself) and hand it to the licensee at the signature line.

## Hard rules

1. **Category math is per-category, always.** A surplus in total hours never covers an ethics deficit. Status reports show every sub-requirement as its own line.
2. **A course counts toward a license only if that board's rules accept it** (provider approval, method, topic). "It counted for my other license" is not evidence. The tracker records which licenses each course counts toward — as a verified claim, not an assumption.
3. **Dates are cycle-strict.** A course completed outside the cycle doesn't count for that cycle, however good it was. The tracker filters by cycle dates; near-boundary courses get eyeballed.
4. **No duplicate official entries.** Diff before entering; if the transcript already has it (under a slightly different title), it's present — note the title variance in the tracker instead of entering a twin.
5. **Certificates are kept, all of them, for the full audit window** the board specifies (commonly several years past renewal) — organized, named, and backed up with the tracker.
6. **The signature line is the licensee's.** See Instructions.

## Reference files

- `references/requirements-and-categories.md` — the per-license worksheet and how to verify it
- `references/tracker-and-certificates.md` — tracker schema, certificate filing, conflict rules
- `references/reporting-system-reconciliation.md` — transcript audit, missing-only entry, verification
- `references/setup-and-maintenance.md` — first-time setup order, the periodic rhythm, renewal packet
- `references/checklist.md` — setup and per-cycle verification checklists
