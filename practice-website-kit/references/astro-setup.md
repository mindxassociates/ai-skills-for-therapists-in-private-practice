# Astro setup — project and content model

## Project layout (the shape to build)

```
/
├── astro.config.mjs
├── package.json            # scripts: dev, build, preview
├── .pages.yml              # PagesCMS config (repo root — the CMS reads it there)
├── public/                 # favicon, robots extras, llms.txt sources, images copied as-is
├── src/
│   ├── content.config.ts   # content collections + zod schemas
│   ├── content/
│   │   ├── providers/      # one .md per clinician
│   │   ├── posts/          # blog/resources (CMS-managed)
│   │   ├── guides/         # evergreen guides, optional (CMS-managed)
│   │   └── pages/          # editable standalone pages, optional
│   ├── layouts/            # SiteLayout (head, meta, schema slots)
│   ├── components/         # SiteHeader, SiteFooter, ProviderCard, FaqList…
│   └── pages/
│       ├── index.astro
│       ├── providers/[slug].astro
│       ├── posts/[slug].astro  + posts/index.astro
│       ├── sitemap.xml.ts      # sitemap endpoint covering every collection
│       └── …one route file per blueprint page (or generated from `pages` content)
└── …language tree mirrored under src/pages/<lang>/ when chosen
```

Framework preset facts for the deploy step: build command `npm run build`, output directory `dist`, Node current LTS.

## Content collections + schema (the contract)

Define every collection in `src/content.config.ts` with a **zod schema**; Astro validates frontmatter at build — a bad field fails the build loudly instead of rendering a broken page. Example shape for providers:

```ts
const providers = defineCollection({
  loader: glob({ base: './src/content/providers', pattern: '**/*.md' }),
  schema: z.object({
    name: z.string(),
    credentials: z.string(),
    states: z.array(z.string()),          // license states as published
    languages: z.array(z.string()),
    specialties: z.array(z.string()),
    populations: z.array(z.string()),
    photo: z.string().optional(),          // path under public/ or the media folder
    feeSummary: z.string().optional(),
    bookingUrl: z.string().url().optional(),
    order: z.number().default(99),         // display order on the index
    draft: z.boolean().default(false),
  }),
});
```

Posts/guides share a shape: `title, slug-implicit-by-filename, description, date, image, faqs: [{q, a}], related: [slugs], draft`. The `faqs` list is what feeds both the visible FAQ block and the FAQPage JSON-LD — one source, two renderings.

Rules:

- **Schemas are strict but forgiving forward:** new optional fields are cheap; never make a field required until every existing entry has it.
- **Drafts:** `draft: true` excludes an entry from routes, sitemap, and feeds — wire that filter into every consumer, not just the page template.
- **Indexes are generated** (provider index, post index, sitemap, RSS) from the collections — never hand-maintained lists that drift.

## Templates

- One layout owns `<head>`: title/description props, canonical, Open Graph/Twitter meta, and a schema slot each template fills (ProfessionalService on home, Person on profiles, Article + FAQPage on posts/guides).
- `[slug].astro` templates render a collection entry end-to-end (header, body via `<Content />`, FAQ block, related links, booking/action block) — a new entry must need **zero** template work.
- Shared header/footer as components used by **every** page — including the home page. (A hand-written inline header on the home page that the shared component doesn't control is a real-world trap: a nav change then silently misses the most-visited page. One header, everywhere.)

## Local development loop

`npm run dev` for editing; `npm run build` must pass clean before any push is called done — the build *is* the test for content/schema errors, and Cloudflare runs the same command.
