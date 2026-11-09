# Retell Virtual Receptionist Kit

Set up a **Retell AI virtual receptionist** for a solo or group therapy practice: one phone line that can answer practice questions, match a caller with the right clinician, check real consultation availability, book only a slot the booking system confirms, take structured messages, and log each call's duration and cost — without giving the voice agent access to clinical records.

This kit is a playbook, not a copy of a working practice's account. Your agent builds the version for your practice from your own provider roster, booking system, phone route, languages, and policies.

## What you get

- **One front-door number** for a solo clinician or a whole group. Directory listings can keep their own public tracking numbers while routing behind the scenes to the receptionist.
- **Roster-based matching.** The receptionist works from a provider directory you control: states served, ages, client types, specialties, languages, published self-pay rates, insurance panels, accepting status, and provider-specific exceptions.
- **Real booking, not guessed availability.** A small bridge connects Retell to your booking backend. The agent may offer only returned slots and may say “booked” only after the backend confirms.
- **Therapy-practice guardrails.** Crisis wording comes before booking, insurance answers never become benefit estimates, established-client calls stay logistical, and requests for another person's information or internal practice data are refused.
- **Privacy controls you configure deliberately.** Retell BAA verification, data-redaction and retention choices, a call log containing structured operational fields rather than transcripts, and optional admin notifications with a link back to the call in Retell.
- **Call-cost visibility.** A call log records duration, Retell's structured cost, outcome, and the clinician the call concerned. Solo practices can treat all cost as overhead; groups can choose pass-through or absorbed cost rules.
- **A free-first testing method.** Most debugging happens in Retell's text simulation and bridge tests, before any paid live-call testing or directory cutover.

## Who this fits

- A solo practice that wants after-hours or overflow answering without hiring a receptionist.
- A group practice replacing several per-provider answering arrangements with one central line.
- A practice that already has — or is building — a booking system with calendars and server-side booking rules.
- A bilingual or multilingual practice that needs the receptionist's languages and name-confirmation rules designed deliberately rather than left to speech recognition.

## Choose your booking mode during setup

1. **Live booking bridge (full kit):** Retell checks availability and books through your booking backend.
2. **Message-and-callback mode:** the receptionist answers questions and captures a structured callback request, but does not book. Use this until the bridge passes every test.
3. **Information-only mode:** the receptionist answers public practice questions and routes callers to your booking page or human line. This is the safe starting point for a pilot.

Do not let the agent improvise a fourth mode. If the booking integration is unavailable, it must say so and use the fallback you chose.

## How to use this kit

Hand the **whole folder** to your AI agent and say:

> “Set up a Retell virtual receptionist for my practice using this kit. Start with the setup interview in SKILL.md — don't configure Retell, buy a number, or change any phone routing until I've answered.”

Routes: native skill support (install the folder) / coding-workspace agent (point it at `SKILL.md`) / chat-only agent (upload all `.md` files, paste the prompt from `PROMPT.md`).

## Boundaries

- **Verify the BAA and every vendor in the call path.** A BAA with Retell does not automatically cover a separate telephony carrier, transcription add-on, booking vendor, or analytics tool.
- **The receptionist is not an emergency service and not a clinician.** It gives your configured crisis resources and does not counsel.
- **No clinical records in the bridge or call log.** The integration needs booking configuration, calendars, availability, and structured call outcomes — not notes, diagnoses, or treatment information.
- **Never promise a channel the number cannot use.** If the selected number or plan does not support SMS, the receptionist must not offer to text.
- **Cut over one route at a time.** Test the agent and bridge first; change directory or main-line forwarding only after the test battery passes, and verify each route after changing it.

## Downloading this skill as a zip

GitHub has no per-folder download button. To get just this folder as a zip: copy this folder's address — `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice/tree/main/retell-virtual-receptionist-kit` — paste it into [download-directory.github.io](https://download-directory.github.io/), and download the zip it creates. (Or download the whole repository from its front page: green **Code** button → **Download ZIP**, and keep just this folder.) Unzip it and hand the whole folder to your AI agent.
