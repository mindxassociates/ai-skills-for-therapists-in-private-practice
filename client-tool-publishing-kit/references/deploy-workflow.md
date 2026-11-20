# Client Tool Deploy Workflow (scrubbed runbook)

Deploy a bilingual interactive client tool (English + a second language,
e.g. Simplified Chinese) from a zip file to GitHub Pages, then list it in
your Client Tools spreadsheet. Written so any AI agent with shell access,
an authenticated `gh` CLI, and spreadsheet write access can execute it
end to end.

> Every value in `<angle brackets>` — and every owner, domain, and
> spreadsheet reference below — comes from the kit's setup interview
> with the practice that owns the tool. Nothing here is pre-filled for
> any specific practice.

## Inputs (collect before starting)

| Input | Example (illustrative only) | Notes |
|---|---|---|
| Zip file path | `<path-to>/my-tool.zip` | Must contain `index.html` and `<lang>/index.html` at the zip root |
| Repo slug | `my-tool` | lowercase-hyphen; becomes the GitHub repo name and the URL path |
| EN title | `My Tool` | English-tab row + browser tab title |
| Translated title | (supplied by owner) | Translated-tab row; use the owner's rendering — do not translate the EN title word-for-word unless asked |
| EN description | (one sentence) | Also used as the GitHub repo description |
| Translated description | (one sentence, in that language) | |
| EN keywords | `Topic One, Topic Two, ...` | Comma-separated |
| Translated keywords | (comma-separated, in that language) | Match the separator style of existing rows in that tab |
| Cover photo guidance | e.g. "a relevant copyright-free picture from Pexels" | Agent picks; owner may supply their own |

If any input is missing, ask. Do not invent titles or descriptions.

## Constants (yours, from the setup interview — never hardcode)

- **GitHub owner:** whatever `gh api user -q '.login'` returns for the
  signed-in account or organization. Resolve it at runtime; do not
  hardcode it.
- **Pages custom domain:** `https://<your-projects-domain>/<slug>/` and
  `https://<your-projects-domain>/<slug>/<lang>/`. Confirm via the Pages
  API `html_url` rather than assuming.
- **Spreadsheet:** your Client Tools sheet (identified by the owner —
  refer to it by name, not by a copied ID), with one tab per language
  (e.g. an English tab and a translated-language tab). Columns:
  `Title | Keywords | Brief Description | Link | Cover Photo`.

## Step 1 — Extract and inspect

```sh
unzip -l <zip>                                   # confirm index.html + <lang>/index.html
mkdir -p ~/workspace/<slug> && unzip -o <zip> -d ~/workspace/<slug>
```

Sanity checks (do not skip):

- Both files are self-contained: no local `<img>` dependencies, no
  external CSS/JS the page needs to run. External references should be
  plain links only.
- Read the `<title>` and `<meta name="description">` of each file to
  confirm which language each page is.
- If either page appears to send or store what a visitor types, stop
  and flag it to the owner before deploying — these are public static
  pages and must collect nothing.

## Step 2 — Create the GitHub repo and push

```sh
cd ~/workspace/<slug>
git init -q && git checkout -qb main && git add .
git -c user.name="<your-git-name>" -c user.email="<your-git-email>" commit -qm "Initial commit: <slug> (EN + <lang>)"
gh auth status                                   # must show a logged-in account with `repo` scope
gh repo create <slug> --public --source=. --remote=origin --push \
  --description "<EN description>"
```

Gotcha: in non-interactive shells a later plain `git push` can fail with
`could not read Username for 'https://github.com'`. Fix once with
`gh auth setup-git`, then push works.

Verify: `gh repo view <slug> --json url -q .url` prints the repo URL.

## Step 3 — Enable GitHub Pages on `main`

This is the API equivalent of Settings → Pages → Build and deployment →
Deploy from a branch → `main` → Save:

```sh
OWNER=$(gh api user -q '.login')
gh api repos/$OWNER/<slug>/pages -X POST -f 'source[branch]=main' -f 'source[path]=/'
```

Poll until built (builds usually take 30–90 seconds):

```sh
gh api repos/$OWNER/<slug>/pages --jq '{html_url, status}'
```

Then verify both pages actually serve (a `404` here means still
building — wait 30s and retry; do not report it live until you see
`200`):

```sh
for u in "https://<your-projects-domain>/<slug>/" "https://<your-projects-domain>/<slug>/<lang>/"; do
  echo "$u -> $(curl -s -o /dev/null -w '%{http_code}' --max-time 20 -A 'Mozilla/5.0' "$u")"
done
```

## Step 4 — Pick the cover photo

1. Search a copyright-free source (Pexels or Unsplash) for something
   topically relevant to the tool. The final image must be hosted by
   that source under its free licence.
2. Download the candidate and **look at it** — confirm it is
   appropriate, on-theme, and not a meme, watermark, or stock-photo
   cliché that misrepresents the tool.
3. Use the source's bare, stable URL form (for Pexels, matching the
   conventional sheet format:
   `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg`).
4. Verify: `curl -s -o /dev/null -w '%{http_code} %{content_type}'`
   must print `200 image/jpeg` (or the equivalent image type).
5. The same photo is used for both language rows.

## Step 5 — Add both rows to your Client Tools sheet

Append one row per language using your spreadsheet tool's append
operation (Sheets API `spreadsheets.values.append` with
`valueInputOption=USER_ENTERED`), against **your** spreadsheet and
**your** tab names:

- English tab, range `<EN tab>!A:E`, values:
  `["<EN title>", "<EN keywords>", "<EN description>", "https://<your-projects-domain>/<slug>/", "<cover URL>"]`
- Translated tab, range `<translated tab>!A:E`, values:
  `["<translated title>", "<translated keywords>", "<translated description>", "https://<your-projects-domain>/<slug>/<lang>/", "<cover URL>"]`

Verify by reading back the appended rows (a values `get` on both tabs)
and confirming the titles, links, and photo URLs are correct.

## Step 6 — Report

Report: repo URL, both live page URLs (confirmed 200), cover photo
chosen and why, and the two new sheet rows. If the owner later asks to
rename the tool, follow the Rename procedure below.

## Optional — Rename procedure

Used when the tool's display name changes after deploy (e.g. "Gentle
Guide" → "Recovery Kit") without changing the URL slug.

A tool's page header brand typically appears in two places per file —
a static brand element and a JavaScript language-switcher line that
covers each language variant. Replace **both** with the plain new
name, in `index.html` and in the translated file. Localize the brand
for the translated page and for the in-page language switcher instead
of leaving it in English, and set the translated page's static brand
element to the translated name so it renders correctly before the
JavaScript runs. Also update the `<title>` tag and any in-page title
string that drives the browser tab title. Leave the hero headline,
the footer credits, and other page content alone unless the owner
explicitly asks — they are page content, not the tool name.

Then: commit, `git push` (run `gh auth setup-git` first if push asks
for a username), wait ~60s for the Pages rebuild, fetch both URLs to
confirm the new header renders, and update the Title cell in the
sheet (English tab; keep the translated tab's title unless told
otherwise).

**Full URL change (only when the owner explicitly asks):** rename the
repo with `gh api -X PATCH repos/<owner>/<old-slug> -f name=<new-slug>`,
update the local remote
(`git remote set-url origin https://github.com/<owner>/<new-slug>.git`),
wait for Pages to rebuild, verify the new URLs return 200, and update
the Link cells on both sheet tabs to the new URLs. Note: GitHub does
not redirect the old Pages path, so the old URL stops working.
