# AI Skills for Therapists in Private Practice

A collection of reusable AI-agent skills built for therapists in solo and group private practice. Each skill is a self-contained folder you can hand to your own AI agent (Muse, ChatGPT, or any agent that can read Markdown files) — the agent follows the playbook inside to do the work with your own accounts, your own data, and your own configuration.

No practice data from any real practice is included. Every skill was scrubbed before publishing: no names, emails, account IDs, fees, or client information.

## The skills

| Skill | What it does |
|---|---|
| [Solo Consult Booking Kit](solo-consult-booking-kit/) | Builds a HIPAA-supporting initial-consultation booking system for a **solo** practice on Google Workspace + Apps Script — public booking page, availability management, and a consult console, with no monthly booking-platform fee. Start with its `README.md`, or paste its `PROMPT.md` into your agent. |
| [Group Consult Booking Kit](group-consult-booking-kit/) | The **group practice** edition of the booking system: one public booking page that routes prospective clients to the right clinician by license state, insurance panel, language, and age group, plus provider self-service apps and an admin console. Start with its `README.md` or `PROMPT.md`. |
| [Practice Books Kit](practice-books-kit/) | Bookkeeping + payroll for a therapy practice: feed your agent your bank/card statements, and it categorizes every transaction into a therapist-specific chart of categories, builds a monthly P&L spreadsheet, and specifies a visual finances + payroll app your agent can build for you. |
| [Therapist ISO Tracker](therapist-iso-tracker/) | Scans the Facebook therapist groups you belong to for "ISO" (in search of) client referral posts, matches them against your profile (state, populations, panels, specialties), and drafts copy-paste replies you post yourself. Strictly read-only — it never posts, comments, or messages on your behalf. Fill in `config.md` and `references/provider-profile.md` first. |
| [Referral Network Kit](referral-network-kit/) | Builds a living referral directory on Google Workspace + Apps Script: one spreadsheet of recommended colleagues rendered live as a public, searchable directory (photo cards, filters, one-click copy of a provider's details for pasting into a referral), an internal add form for your own clinicians, and an optional public "get recommended" form — with duplicate protection and an admin email on every submission. Start with its `README.md` or `PROMPT.md`. |
| [Insurance Payer Credentialing](insurance-payer-credentialing/) | A repeatable, auditable workflow for credentialing providers directly with insurance payers and EAPs: per-provider document checklists, per-payer submission packets, and an outcome log. It prepares submissions only — nothing is ever sent without your explicit approval. |

## How to use a skill

1. **Pick one skill folder** — you don't need the whole repository.
2. **Give the whole folder to your AI agent:**
   - Agent with native skill support: install/copy the folder as a skill.
   - Coding-workspace agent: drop the folder into your workspace and point the agent at its `SKILL.md`.
   - Chat-only agent: upload all of the folder's `.md` files and use the starter prompt (the booking kits include a ready-made `PROMPT.md`).
3. **Do the setup interview / configuration first.** Each skill asks for your practice's own details (domain, rates, panels, groups) before it builds or runs anything. Never skip that step, and never let an agent guess your pay rates, panels, or fees.
4. **Review before anything goes live.** These skills prepare drafts, specs, and paste-ready files. Deployments, submissions, and sends stay in your hands unless you explicitly approve them.

## A note on HIPAA

The booking kits are designed to run inside a **Google Workspace account with a signed BAA** — that prerequisite is stated at the top of each kit and is not optional if real client data will flow through the system. Software implements safeguards that support HIPAA compliance; no skill here certifies compliance. Read each skill's `references/security-and-hipaa.md` before building.

## Contributing / feedback

These skills come from a working group practice and are shared so colleagues don't have to reinvent them. If you adapt one for your practice and improve it, a pull request or an issue describing what you changed is welcome.
