# Catalog format

The catalog is a source JSON file in the project, converted at build time into a server-side data object. The workbook never stores catalog content. One item looks like this (a thought log):

```json
{
  "name": "Thought log",
  "nameZh": "思维记录",
  "category": "Cognitive",
  "slug": "exercises/thought-log",
  "type": "chatbot",
  "description": "Choose a recent thought and the feelings and actions that followed; decide if it was helpful or unhelpful",
  "descriptionZh": "…",
  "zhStatus": "ZH_AUTHORED",
  "audience": ["Adult", "Youth"],
  "inPracticeLibrary": true,
  "inRemindLibrary": true,
  "customSteps": [
    { "kind": "text",     "promptEN": "A thought log slows down a difficult moment…", "promptZH": "…" },
    { "kind": "freetext", "promptEN": "Pick a recent moment that stuck with you…", "promptZH": "…", "required": true },
    { "kind": "choice",   "promptEN": "Looking back, was that thought helpful or unhelpful for you?",
      "promptZH": "…", "options": ["Helpful", "Unhelpful"], "optionsZH": ["有益", "无益"], "required": true }
  ]
}
```

## Item fields

- **slug** — hierarchical and stable: `exercises/<name>` or `reminders/<name>`. The slug is the join key between catalog, assignments, results, and the public page URL. Never rename a live slug; retire instead.
- **type** — the renderer: `chatbot` (step-by-step conversation), `chatbot-game` (choice rounds), `journal`, `self-monitoring` (multi-entry logs), `audio-timer` (breathing / mindfulness / relaxation), `custom-reminder` (a simple "do this" reminder with a Done tap), `affirmation` (a short positive text; no completion state). Keep the type list small — every type is a renderer you must build and test in both languages.
- **category** — display grouping in the assign library and the public index. Categories are data too: a bilingual build keeps a category → translation map, and the harness asserts **every** category used by any item resolves a translation (a category added without one silently falls back to English in the second-language UI).
- **description / descriptionZh** — one or two client-facing sentences, second person, plain and warm. The description is also what some renderers show as their body (affirmations: the description *is* the affirmation text — write a real affirmation, not a feature description).
- **gentleNote / gentleNoteZh** (optional) — a short "go gently" note shown before emotionally heavy items (grief writing, trauma work). If the field exists, its translation field must exist too, and the payload must actually carry it — a translated field with no consumer in the code is a silent English leak.
- **crisisNote: true** (optional) — the item shows the crisis-resources block and every submission flags `REVIEW` for the provider. Safety-plan-type items carry this.
- **zhStatus** — `ZH_AUTHORED` only when a human has authored the item's second-language fields. Anything else renders the English clinical content inside the second-language UI **with a visible note saying so**. This flag is the honesty mechanism; never flip it for machine output.
- **inPracticeLibrary / inRemindLibrary** — an item can be practicable in-session, assignable as homework, or both.

## Steps

`customSteps` is the item's client experience. Step kinds:

| kind | renders as | carries |
|---|---|---|
| `text` | a display bubble/paragraph (intros, instructions) | no answer |
| `freetext` | a textarea | the client's words |
| `choice` | tappable option pills | `options` (+ `optionsZH`, exactly parallel in length and order) |
| `rating` | a scale (e.g. 0–10) | a number |

Every step has `promptEN` and (in a bilingual build) `promptZH`; `required: true` blocks submit until answered. Choice steps record the tapped option string verbatim — there is no hidden scoring for chat items, so right/wrong must be self-evident to the client.

**The authored-steps rule (learned the hard way).** Client steps come from `customSteps` — full stop. An earlier architecture synthesised steps from internal `interactionFlow` build notes when authored steps were missing, and real clients were shown developer text ("Client taps ready/continue pill button", "Submit stays disabled until…"). The renderer must therefore have **no synthesis path**: an item without authored steps gets a minimal generic flow (its description as an intro + one generic reflection step), and the test harness sweeps **every** item's rendered payload for spec-language hallmarks. Descriptions get the same sweep — developer meta ("in the original platform…", character counts, sourcing notes) is not client copy.

Keep a private authoring-notes field if you need one (sourcing, licensing, TODOs) — quarantined in the data, never reachable by any renderer.

## Bilingual string tables (UI chrome)

Separately from catalog content, all interface strings (buttons, labels, email templates, wizard fragments) live in **one keyed string table per language**, generated from a single source into the server file and both HTML files, with a parity check in the harness (same key set both languages; the reference build runs ~250 keys). The natural-language assignment summary ("…will get X by email every Mon at 7:00 PM…") is composed from fragment keys in both languages — budget the fragments when you design the wizard.

Language resolution for a landing: explicit pill tap (this visit) → assignment language snapshot → client's stored language → page language (a `/zh` page variant) → English. The client's own tap is remembered across pages on the same browser (local storage on the app origin); a stored browser choice never overrides an assignment's own language default — only a tap during that visit does. `LangUsed` on the Result records what actually happened.

## Sizing guidance

Start small and deep rather than broad and thin: a dozen well-authored items with complete translations beat a hundred with gaps. The reference build's shape — ~130 exercises across cognitive, relaxation, affect/emotion, social skills, parenting, journals, self-monitoring, sleep, and a large structured homework set, plus a handful of reminders (appointments, medication, affirmations, custom) — took sustained authoring time per item. Every item you add costs: steps in two languages, a public page, parity checks, and a click-test.
