# Practice Chatbot Kit

Build a **practice-coordinator chatbot** for your therapy practice's website: a warm front door that matches visitors to the right clinician, guides them to your free initial consultation, answers practice questions from your own help center, routes billing questions to a human, and answers a crisis disclosure with crisis resources — in the visitor's own language.

This kit is a playbook and a persona template, not a copy of a working practice's chatbot. Your agent builds the version for your practice from your own roster, booking links, help center, languages, and policies.

## What you get

- **A complete persona template** (`references/persona-and-instructions.md`) you fill in once and paste into a website chat widget, a custom GPT / project / Gem, or an AI agent session.
- **State-first matching.** The chatbot must find a provider licensed in the visitor's state before it considers specialty, insurance panel, language, or age group — and it says so plainly when nobody fits.
- **Bilingual by design, adaptable to any language pair.** Replies match the visitor's language, including per-language practice and provider names if your practice uses them.
- **Booking without invented links.** The chatbot uses only the booking link(s) you give it — one per language if you run separate booking pages — and offers your contact email or waitlist when there is no fit.
- **Money questions handled safely.** Published self-pay fees may be quoted when a visitor asks about cost; copays, deductibles, and benefits are never estimated — billing and insurance questions route to your billing contact.
- **Crisis guardrails.** A crisis or self-harm disclosure gets an immediate, warm response with your configured crisis resources (US default: call or text 988) — no assessment, no counseling, and no booking pitch in that moment.
- **A no-invention rule throughout.** Roster and help center are the source of truth. If a fact is not there, the chatbot hands off instead of guessing — including never making compliance claims.

## Who this fits

- A solo practice that wants its website chat to do real intake routing instead of generic small talk.
- A group practice whose visitors keep asking "who is licensed in my state, and who takes my insurance?"
- A bilingual or multilingual practice that needs language matching and per-language names handled deliberately.
- A practice that already has — or is willing to write down — a provider roster and a short FAQ / help-center page the chatbot can draw from.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> "Build a practice-coordinator chatbot for my practice using this kit. Start with the setup interview in SKILL.md — don't write the persona until I've answered."

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Boundaries

- **The chatbot is not a clinician and not an emergency service.** It gives your configured crisis resources and does not assess or counsel.
- **No clinical or sensitive data collection.** It asks only what routing an inquiry needs.
- **Facts go stale.** When a provider joins, leaves, changes panels, or changes fees, update your source of truth and the persona file in the same pass, then re-test.
- **Check your platform's rules.** A chat widget, custom GPT, or agent session each has its own disclosure and data-handling requirements; the kit's persona is platform-neutral and does not settle them for you.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address from your browser's address bar, paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
