# Insurance Payer Credentialing

**A repeatable, auditable workflow for credentialing solo and group
practice providers directly with insurance payers and EAPs** — per-provider
document checklists, per-payer submission packets, and an outcome log.
The skill prepares everything for your review; **nothing is ever sent
or submitted without your explicit approval.**

This is an **agent skill**: plain-Markdown playbooks your AI agent
follows with your own accounts and your own practice data. It follows
the open Agent Skills format (`SKILL.md`) and works with any capable
AI agent — it is not tied to one vendor.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The main playbook: practice profile, per-provider checklist, payer workflows (including EAP intakes and roster-email payers), the group-vs-individual status rule, output contract, and operating rules. An agent should read this first. |
| `PROMPT.md` | A copy-paste starter prompt for chat-based agents. |

## The two lessons baked in

1. **Group ≠ individual.** A group contract approval does not credential
   an individual provider. The skill tracks group and individual status
   in separate fields, checks individual status by individual NPI, and
   keeps a provider at *In Progress* until the payer confirms that
   provider by name.
2. **A payer's written answer governs.** Contracts and provider guides
   can be silent or stricter than the payer's actual practice. Before
   concluding a clinician type is ineligible, the skill searches the
   practice mailbox for the payer's own correspondence — a provider
   relations email answer governs over a guide summary, and the sender
   and date relied on are recorded in the packet.

## Use it with any AI agent

Paste this repository's link to your agent and tell it which skill to
use, or hand the agent this folder. The agent runs the setup interview
first (practice legal name, NPIs, Tax ID, credentialing contact,
document folder), builds each provider × payer packet for your review,
and submits only after you approve that exact packet.

## What it is not

- Not a credentialing service and not a guarantee of acceptance,
  timelines, or rates — payers decide those.
- Not a place for client information: provider and practice data only,
  never client PHI.
