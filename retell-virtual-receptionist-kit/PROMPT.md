# Starter prompt — copy, paste, send to your AI agent

Upload (or install) every file in this kit first, then paste:

---

Set up a Retell AI virtual receptionist for my therapy practice using the Retell Virtual Receptionist Kit in this workspace.

Follow the kit exactly:

1. Run the **setup interview** in `SKILL.md` first — solo or group shape, countries and states served, languages, provider roster source, booking mode, phone and directory routes, SMS needs, human fallback, crisis resources, privacy settings, admin notifications, and cost handling. Do not create the agent, buy a number, connect a calendar, or change any routing until I have answered. Never invent a license, panel, fee, exception, or availability rule — use placeholders and flag every one.
2. Prepare the **provider directory** from my source of truth using `references/prompt-and-provider-directory.md`. For a solo practice it has one entry; for a group it has one entry per clinician. Confirm every hard gate and provider exception with me before the prompt goes live.
3. Build in kit order: telephony and BAA decisions (`references/architecture-and-telephony.md`), agent and knowledge base, the booking bridge if I chose live booking (`references/bridge-contract.md`), privacy configuration (`references/privacy-and-safety.md`), then testing (`references/testing-and-go-live.md`).
4. Obey the kit's hard rules: one front-door receptionist; the agent offers only slots my booking backend returns and claims a booking only on an explicit success response; booking guards are enforced server-side, not just requested in the prompt; the call log stores structured operational fields, never transcripts or clinical content; the receptionist never promises SMS, voicemail, transfer, or any other capability until that exact route has been tested.
5. Test like the kit says: bridge tests in the **actual payload shape Retell sends**, a fresh text-simulation session for every scenario, one end-to-end test booking that is verified and then cancelled or voided through my booking system's approved test cleanup. Do not use repeated paid voice calls for debugging.
6. Cut over one phone route at a time only after the test battery passes. Verify each directory listing or forwarding change by reading it back, keep my human fallback available until the new route is proven, and walk me through `references/testing-and-go-live.md` before calling the receptionist live.

---
