# AI Skills for Therapists in Private Practice

English | [中文版](README.zh.md)

A collection of 18 reusable AI-agent skills built for therapists in solo and group private practice. Each skill is a self-contained folder you can hand to your own AI agent (Muse, ChatGPT, or any agent that can read Markdown files) — the agent follows the playbook inside to do the work with your own accounts, your own data, and your own configuration.

No practice data from any real practice is included. Every skill was scrubbed before publishing: no names, emails, account IDs, fees, or client information.

## The fastest way to use a skill: paste this repo's link to your AI agent

You don't need to download anything yourself. **Copy this repository's link — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice` — paste it to your AI agent, and tell it which skill you want**, for example:

> "Use the Solo Consult Booking Kit from this repository to build my booking system: https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice"

A capable agent will fetch the skill, read its `SKILL.md`, run its setup interview with you, and do the work. The download routes below are there if your agent can't fetch links, or you prefer to handle the files yourself.

## Free to DIY — or have it installed for you

Every skill in this repository is **free** to use yourself, for as long as you like. They are written so a capable AI agent can walk you through the whole build.

If you'd rather not do it yourself, **hands-on installation is available for a fee** from the practice that built these skills: we set the system up in your own accounts, with your own configuration, and hand it over working and tested. Pricing depends on which skills you want and the size of your practice — join [Community by Mind X Associates](https://community.mindx.us/) or reach out through [mindx.us](https://mindx.us/) and ask about installation.

## Downloading a skill (zip)

**The whole collection:** on this page, click the green **Code** button → **Download ZIP**. Unzip it — every folder inside is one complete skill.

**Just one skill:** GitHub doesn't offer a per-folder download button, so use one of these:

1. **Easiest — a folder-download helper:** open the skill's folder (links in the table below), copy its address from your browser's address bar, paste it into [download-directory.github.io](https://download-directory.github.io/), and it hands you a zip of just that folder.
2. **With Git:** `git clone https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice.git` — then copy out the one folder you need and delete the rest.
3. **Ask your AI agent:** paste the skill folder's GitHub link to your agent and say "download this folder as a zip" — most coding agents can fetch it for you.

Then hand the **unzipped folder** (all of its files, including the `references` subfolder) to your AI agent — see "How to use a skill" below.

## The skills

| Skill | What it does |
|---|---|
| [Solo Consult Booking Kit](solo-consult-booking-kit/) | Builds a HIPAA-supporting initial-consultation booking system for a **solo** practice on Google Workspace + Apps Script — public booking page, availability management, and a consult console, with no monthly booking-platform fee. Start with its `README.md`, or paste its `PROMPT.md` into your agent. |
| [Group Consult Booking Kit](group-consult-booking-kit/) | The **group practice** edition of the booking system: one public booking page that routes prospective clients to the right clinician by license state, insurance panel, language, and age group, plus provider self-service apps and an admin console. Start with its `README.md` or `PROMPT.md`. |
| [Practice Books Kit](practice-books-kit/) | Bookkeeping + payroll for a therapy practice: feed your agent your bank/card statements, and it categorizes every transaction into a therapist-specific chart of categories, builds a monthly P&L spreadsheet, and specifies a visual finances + payroll app your agent can build for you. |
| [Practice CRM Kit](practice-crm-kit/) | A lead-tracking CRM for a therapy practice: pipeline board (New → Started, with honest exits), automatic lead capture from booking, outcome forms, website forms, and hourly inbox ingest, follow-ups on each lead, and group-practice roles — admin sees all, providers see only their own leads with Notes stripped server-side. No clinical notes, no unattended sends. Start with its `README.md` or `PROMPT.md`. |
| [Therapist ISO Tracker](therapist-iso-tracker/) | Scans the Facebook therapist groups you belong to for "ISO" (in search of) client referral posts, matches them against your profile (state, populations, panels, specialties), and drafts copy-paste replies you post yourself. Strictly read-only — it never posts, comments, or messages on your behalf. Fill in `config.md` and `references/provider-profile.md` first. |
| [Referral Network Kit](referral-network-kit/) | Builds a living referral directory on Google Workspace + Apps Script: one spreadsheet of recommended colleagues rendered live as a public, searchable directory (photo cards, filters, one-click copy of a provider's details for pasting into a referral), an internal add form for your own clinicians, and an optional public "get recommended" form — with duplicate protection and an admin email on every submission. Start with its `README.md` or `PROMPT.md`. |
| [Secure Messages Kit](secure-messages-kit/) | A secure client + external-provider messaging portal you own, instead of a paid subscription: email + 6-digit-code sign-in for clients, name + PIN for providers, participant-scoped externals, content-free notification emails, validated unshared attachments, and a hash-chained audit log — with the limits stated honestly (not end-to-end encrypted; practice admin can access messages). Start with its `README.md` or `PROMPT.md`. |
| [CE Records Kit](ce-records-kit/) | Keep continuing-education records renewal-ready across one or more licenses: verified per-license requirements worksheets, a certificate-based course tracker, reconciliation against the official reporting system (CE Broker or your state's equivalent) entering only what's missing, and status reports that show each category's deficit separately. The agent never attests or submits a renewal. Start with its `README.md` or `PROMPT.md`. |
| [Practice Website Kit](practice-website-kit/) | Build a practice website with **Astro + PagesCMS + Cloudflare Pages**: a fast static site (home, provider profiles, services, fees, FAQs, blog/resources) edited through web forms instead of code, hosted free on your own domain — with booking/directories embedded from your existing systems, structured data and llms.txt, and the crisis line on every contact path. Start with its `README.md` or `PROMPT.md`. |
| [Retell Virtual Receptionist Kit](retell-virtual-receptionist-kit/) | Set up a **Retell AI phone receptionist** for a solo or group practice: one front-door line, roster-based clinician matching, optional multilingual behavior, live consult availability and booking through a secure bridge to your own booking system, structured call-cost logging, privacy and crisis guardrails, free-first testing, and one-route-at-a-time cutover for directory and main-line numbers. Start with its `README.md` or `PROMPT.md`. |
| [Auto-Created Listing Takedown Kit](auto-created-listing-takedown-kit/) | Find and remove **directory pages you never created**: sites scrape the NPPES registry and auto-publish profiles — sometimes whole mini-websites — with assumed office hours, wrong specialties, and fake appointment widgets. Covers inventory by NPI and legal name, per-site removal playbooks (including Dr. Leonardo's claim-to-delist flow), validation-link discipline, FTC / Google / host / registrar abuse reports, and a monthly sweep so removed pages stay removed. Start with its `README.md` or `PROMPT.md`. |
| [Insurance Payer Credentialing](insurance-payer-credentialing/) | A repeatable, auditable workflow for credentialing providers directly with insurance payers and EAPs: per-provider document checklists, per-payer submission packets, and an outcome log — with group-vs-individual status tracked separately, so a group contract is never mistaken for a credentialed provider. It prepares submissions only — nothing is ever sent without your explicit approval. Start with its `README.md` or `PROMPT.md`. |
| [Practice Chatbot Kit](practice-chatbot-kit/) | Build a bilingual practice-coordinator chatbot for your website: matches visitors to providers by license state first, then specialty, panel, language and age; guides matched visitors to your own booking link; answers FAQs from your own help-center content; routes billing questions to a human without quoting unpublished fees; and stops booking to give 988 crisis resources when a visitor discloses crisis. Start with its `README.md` or `PROMPT.md`. |
| [Snoooz Inbox Automation Kit](snoooz-inbox-automation-kit/) | Set up Snoooz.ai email automation for a solo or small practice: directory and Psychology Today inquiry replies gated on age, client type, insurance, location, crisis, format and fees; EAP inquiry handling; existing-client and billing routing; labels and exclusions — with blank config templates and a simulation battery before anything sends. Start with its `README.md` or `PROMPT.md`. |
| [Brilliant Directories Publishing Kit](brilliant-directories-publishing-kit/) | Create, restyle and repair Brilliant Directories directory/SEO pages without the usual disasters: hidden-first creation, wholesale body replacement from your styled source file (never a paraphrase), exact live verification of provider cards, schema and hreflang, and the noindex trap — flip public, uncheck NoIndex, refresh, and verify the live robots meta before requesting indexing. Start with its `README.md` or `PROMPT.md`. |
| [Client Tool Publishing Kit](client-tool-publishing-kit/) | Deploy a bilingual interactive client tool (worksheets, trackers, psychoeducation tools) from a zip to GitHub Pages on your own domain, pick a copyright-free cover photo, and list it in your tools index spreadsheet in both languages — with both live URLs verified before you share them. Start with its `README.md` or `PROMPT.md`. |
| [Apps Script Deploy Kit](apps-script-deploy-kit/) | Deploy Google Apps Script web apps through the Apps Script API with your own OAuth client instead of pasting code into the editor: push exact files, read back, create a version, bump the *existing* deployment (never mint a new URL), and verify from the served page. The engine room behind the other kits' apps. Start with its `README.md` or `PROMPT.md`. |
| [Apps Script Build Checklist Kit](apps-script-build-checklist-kit/) | A pre-deploy checklist of the Apps Script defects that actually bite in production: manifest mail scopes, browser-global variable collisions, PIN-gate contract mismatches, forms that lose work on partial save, records joined by display name instead of stable ID, and spreadsheet-timezone timestamp shifts — each with its fix and a final sweep. Start with its `README.md` or `PROMPT.md`. |

## How to use a skill

1. **Pick one skill** — you don't need the whole repository.
2. **Fastest: paste this repository's link to your AI agent** and name the skill (see the top of this page). Or give the whole folder to your agent:
   - Agent with native skill support: install/copy the folder as a skill.
   - Coding-workspace agent: drop the folder into your workspace and point the agent at its `SKILL.md`.
   - Chat-only agent: upload all of the folder's `.md` files and use the starter prompt (the booking kits include a ready-made `PROMPT.md`).
3. **Do the setup interview / configuration first.** Each skill asks for your practice's own details (domain, rates, panels, groups) before it builds or runs anything. Never skip that step, and never let an agent guess your pay rates, panels, or fees.
4. **Review before anything goes live.** These skills prepare drafts, specs, and paste-ready files. Deployments, submissions, and sends stay in your hands unless you explicitly approve them.

## A note on HIPAA

The booking kits are designed to run inside a **Google Workspace account with a signed BAA** — that prerequisite is stated at the top of each kit and is not optional if real client data will flow through the system. Software implements safeguards that support HIPAA compliance; no skill here certifies compliance. Read each skill's `references/security-and-hipaa.md` before building.

## Contributing / feedback

These skills come from a working group practice and are shared so colleagues don't have to reinvent them. If you adapt one for your practice and improve it, a pull request or an issue describing what you changed is welcome.
