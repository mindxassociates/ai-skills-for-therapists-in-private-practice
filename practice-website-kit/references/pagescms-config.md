# PagesCMS config — `.pages.yml`

PagesCMS (app.pagescms.org) signs the editor in with GitHub and reads **`.pages.yml` from the repo root**. It turns each declared collection into a form over the Markdown files in a folder, and saves by committing. Editors need GitHub accounts with write access to the repo — invite them to the repo, not to a CMS admin panel; there isn't one.

## The one rule that breaks everything

**Filename templates use field placeholders like `{fields.slug}` — there is no bare `{slug}`.**

A config with `filename: "{slug}.md"` looks right, loads in the CMS fine, and then **every save fails** with an opaque error (`Invalid extension "" for content "…"`) — because the template can't resolve, produces an empty name, and the CMS chokes on the extension. The correct form, for a collection whose entries carry a `slug` field:

```yaml
filename: "{fields.slug}.md"
```

Placeholders are `{primary}` and `{fields.<field-name>}`. If a collection has no slug field, name files by a field it does have (e.g. `{fields.title}` is fragile — prefer adding a slug field to the schema and the CMS form, hidden or auto-derived, so filenames stay stable and URL-safe).

After changing `.pages.yml`, **reload the CMS** — it caches the config for the session, and a fixed config under a stale session still fails. This caching is the second half of the same trap.

## Example config (adapt collections to the blueprint)

```yaml
media:
  - name: images
    label: Images
    input: public/images
    output: /images

content:
  - name: providers
    label: Providers
    type: collection
    path: src/content/providers
    filename: "{fields.slug}.md"
    format: yaml-frontmatter
    fields:
      - { name: slug, label: Slug (URL name), type: string, required: true }
      - { name: name, label: Name, type: string, required: true }
      - { name: credentials, label: Credentials, type: string, required: true }
      - { name: states, label: License states, type: string, list: true }
      - { name: languages, label: Languages, type: string, list: true }
      - { name: specialties, label: Specialties, type: string, list: true }
      - { name: photo, label: Photo, type: image }
      - { name: bookingUrl, label: Booking URL, type: string }
      - { name: draft, label: Draft (hidden), type: boolean, default: false }
      - { name: body, label: Bio, type: rich-text }

  - name: posts
    label: Blog / Resources
    type: collection
    path: src/content/posts
    filename: "{fields.slug}.md"
    format: yaml-frontmatter
    fields:
      - { name: slug, label: Slug, type: string, required: true }
      - { name: title, label: Title, type: string, required: true }
      - { name: description, label: Summary (search/social), type: text, required: true }
      - { name: date, label: Date, type: date, required: true }
      - { name: image, label: Cover image, type: image }
      - { name: faqs, label: FAQs, type: object, list: true,
          fields: [{ name: q, label: Question, type: string }, { name: a, label: Answer, type: text }] }
      - { name: draft, label: Draft (hidden), type: boolean, default: false }
      - { name: body, label: Body, type: rich-text }
```

## Configuring well

- **Mirror the zod schema.** The CMS form and the content schema describe the same fields; when they disagree, saves produce files the build rejects. Change them together, in the same commit.
- **Required means required** in both places — an optional-in-CMS but required-in-schema field is a build failure waiting for its first victim.
- **Media:** one images folder, referenced the same way by schema and CMS (`input` = repo path, `output` = public URL path). Editors upload through the CMS; nobody hand-drops files into `public/` outside it. Compress before upload — the CMS won't.
- **Scope the CMS to content collections.** Layouts, components, and config stay code-managed. The CMS is for words and pictures an editor owns; the moment a template is in the CMS, you've rebuilt a website builder, badly.
- **One CMS collection per content collection,** named in the editors' language (a bilingual practice may prefer labels like “文章 Posts”).

## The acceptance test

A collection is not "configured" until a **real save** through the CMS UI succeeds, commits, deploys, and the change is visible on the live site. Do this for every collection at setup (a one-word edit is enough), and again after any `.pages.yml` change. Config that merely *loads* proves nothing — the failure mode lives exactly at save time.
