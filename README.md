# MaxLango content

The word lists, grammar pages and courses that the MaxLango app downloads, one
set per language. The app has no packs built in: it reads them from here, and
it can also read packs that anyone hosts at their own URL.

The packs are published at **https://maxmb15.github.io/maxlango-content/**,
starting from [`catalog.json`](https://maxmb15.github.io/maxlango-content/catalog.json).

| Path                           | What it is                                                              |
| ------------------------------ | ----------------------------------------------------------------------- |
| `catalog.json`                 | Every pack with its version, location, size and SHA-256                 |
| `packs/<lang>/<id>.json`       | The packs: French `fr`, Dutch `nl`, Spanish `es`, Italian `it`, Swedish `sv` |
| `languages/<lang>/profile.json` | Each language's grammar concepts (tenses, word classes) the packs use  |
| `schema/`                      | JSON Schemas for a pack and a catalog                                   |
| `scripts/`                     | The Python that generates the packs and the catalog, and checks them    |

## How the app installs and updates packs

1. **Onboarding.** When a learner picks a language, the app downloads
   `catalog.json`, then each of that language's packs in catalog order. It
   checks every file's SHA-256 against the catalog before importing it.
2. **Checking for updates.** At launch, and when the learner taps *Check for
   updates*, the app asks for the catalog again. It sends the ETag from last
   time, so an unchanged catalog costs one empty `304` reply.
3. **Updating.** A pack updates when the catalog lists a **higher `version`**
   than the one installed. With auto-update on (the default) the app downloads
   and applies it straight away; otherwise the pack shows an *Update* button.
   A lower or equal version is never installed.
4. **Keeping progress.** Items are matched by `id`, so a learner's review
   history and their own edits to an item carry over to the new version. An
   item a learner added to *My words* stays theirs even if a later version of
   the pack drops it.

Every pack belongs to the source it was installed from and only updates from
there. A source can't replace a pack that another source installed.

## Changing a pack

The JSON in `packs/` is generated. Edit the sources in `scripts/` instead:

```sh
# 1. edit scripts/nl_everyday.py (or any <lang>_* module)
# 2. raise that pack's version in the module's PACKS
python3 scripts/build.py          # writes packs/ and catalog.json
python3 scripts/build.py --check --lang es   # or check one language, writing nothing
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Commit the generated files with the change. CI fails a pull request when:

- `packs/` or `catalog.json` differ from what `scripts/build.py` writes,
- a pack doesn't match `schema/pack-v1.json`,
- a pack changed but its `version` didn't go up (apps would never get it),
- a pack's version went down, or a pack left the catalog.

Don't remove or rename an item id. To drop an item, list its id in the pack's
`_retired` list in the generator; the build refuses to lose an id silently.

Merges to `main` publish to GitHub Pages once those checks pass.

### Adding a language

Add `languages/<code>/profile.json`, a `scripts/<code>.py` module with
`PACKS`, and the code to the loop in `scripts/build.py`. The app ships each
language's profile itself, so a new language also needs an app release before
learners can pick it.

## Hosting your own packs

You can serve packs from any static HTTPS host: GitHub Pages, a Gist, S3,
your own server. In the app, open **Library → Packs → Add from URL** and paste
one of these:

- **A single pack.** The URL of one pack JSON file. The app installs it and
  checks the same URL for a higher `version` later.
- **A catalog.** The URL of a `catalog.json` that lists several packs, shaped
  like the one in this repo. Pack `url`s may be relative to the catalog. The
  app offers each pack for the languages the learner studies.

To publish an update, raise the pack's `version` and upload it again (for a
catalog, also update that pack's `version`, `sha256` and `size`). Learners get
it at their next launch or *Check for updates*.

Rules the app enforces:

- `https://` only, and each file at most 10 MB.
- A pack `id` must be unique and must not contain `:`. Prefix it with the
  language code, e.g. `nl-kitchen-v1`. The app refuses a pack whose id belongs
  to a pack installed from another source.
- `version` is a whole number of 1 or more, the same in the pack and its
  catalog entry.
- Units teach 6 to 10 of the pack's own words. Verbs need conjugations,
  pages need a title and a body.

Check your files before you publish them:

```sh
pip install jsonschema
python3 scripts/validate_schema.py path/to/your/folder   # the folder holding catalog.json
```

### A small pack

```json
{
  "$schema": "https://maxmb15.github.io/maxlango-content/schema/pack-v1.json",
  "id": "nl-kitchen-v1",
  "version": 1,
  "language": "nl",
  "name": "In de keuken",
  "author": "Your name",
  "license": "CC-BY-4.0",
  "items": [
    { "kind": "noun", "id": "pan", "primary_form": "pan", "gloss": "pan",
      "extras": { "article": "de" }, "tags": ["keuken", "de"] },
    { "kind": "noun", "id": "mes", "primary_form": "mes", "gloss": "knife",
      "extras": { "article": "het" }, "tags": ["keuken", "het"] },
    { "kind": "phrase", "id": "eet-smakelijk", "primary_form": "eet smakelijk",
      "gloss": "enjoy your meal", "tags": ["keuken"] }
  ]
}
```

Item kinds are `noun`, `verb`, `adjective`, `phrase`, `connective`,
`conjunction`, `other` and `page`. The packs in `packs/` show every field in
use: verb conjugations per tense, adjective forms, a connective's role and
example sentence, and pages written in Markdown with the app's `:::` blocks.
Tense ids and roles come from `languages/<lang>/profile.json`.

### Catalog fields

| Field      | Required | Meaning                                                            |
| ---------- | -------- | ------------------------------------------------------------------ |
| `id`       | yes      | The pack's id                                                      |
| `language` | yes      | Language code, e.g. `nl`                                           |
| `name`     | yes      | Shown in the app before the pack is installed                      |
| `version`  | yes      | The pack's version; the app updates when this goes up              |
| `url`      | yes      | Where the pack is, absolute or relative to the catalog             |
| `sha256`   | no       | Hex SHA-256 of the file; the app refuses a download that differs   |
| `size`     | no       | Bytes, shown before download                                       |
| `items`    | no       | Item count, shown before download                                  |
| `requires` | no       | The pack format the app must know (default `1`)                    |

The catalog's top-level `format` is `1`. A change that older apps can't read
will be published as a new file (`catalog.v2.json`) next to this one, and a
pack that needs a newer app gets a higher `requires`, which older apps skip.

## Licences

- The content (`packs/`, `languages/`, `catalog.json`) is licensed
  [CC BY-SA 4.0](LICENSE). You may share and adapt it, with credit, under the
  same licence.
- The scripts and schemas (`scripts/`, `schema/`) are [MIT](LICENSE-CODE).
