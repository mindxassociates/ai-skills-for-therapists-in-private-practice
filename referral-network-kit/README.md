# Referral Network Kit

Build a **living referral directory** for your therapy practice: one Google Sheet holds the providers you recommend, a public web directory renders it live, and simple add-forms let your own clinicians — and optionally your wider professional community — contribute recommendations. No database to maintain, no monthly directory fee, and editing the sheet updates the directory on the next page load.

## What you get

- **A public, read-only directory** of recommended colleagues: photo cards with name, credentials, location, services, and languages — searchable and filterable, with a one-click "copy this provider's details" gesture for handing a referral to a client.
- **An internal add form** ("Build Your Referral Network") so your own providers can add colleagues they recommend.
- **An optional public add form** ("Get Recommended") so community colleagues can add themselves or recommend someone — same sheet, same duplicate protection.
- **One spreadsheet as the single source of truth.** Duplicate names are rejected, new entries land grouped by service type, and the practice admin gets an email for every submission.

## Who this is for

Solo and group practices that refer out regularly — overflow, off-specialty, off-state, waitlist — and want those referrals to go to known, vetted colleagues instead of a search engine. Works for a single practice's internal network, a community directory, or both.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build me a referral network using this kit. Start with the setup interview in SKILL.md — don't build anything until I've answered."

Three ways to hand it over:

- **Native skill support** (e.g., Muse): install/copy this folder as a skill, then ask for a referral network.
- **Coding-workspace agent**: drop the folder into your workspace and point the agent at `SKILL.md`.
- **Chat-only agent**: upload all the `.md` files and paste the starter prompt from `PROMPT.md`.

Your agent will produce paste-ready Apps Script projects plus the sheet, and walk you through the Google sign-in / authorize / deploy clicks that only you can do (unless your agent has approved direct access to your account).

## Important boundaries

- The directory holds **professional, public-facing information only** — names, credentials, locations, services, websites, photos. Never put client information in it.
- Only list a colleague **with their knowledge**. The add forms state this; your admin reviews every submission email before treating a listing as settled.
- This is a directory of *recommendations*, not a credentialing or endorsement verification system. Say what a listing means on your site ("colleagues our clinicians know and refer to") and nothing stronger.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/referral-network-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
