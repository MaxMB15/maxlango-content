"""Swedish item constructors.

Every Word carries its example sentence inline, so the Swedish packs need no
scripts/examples/ file.
"""

from __future__ import annotations

from common import rows, simple, slug, with_example
from fr_common import connectors  # language-agnostic
from sv_conj import conjugate

__all__ = ["nouns", "adjectives", "verb", "phrases", "connectors"]


def nouns(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`word | en/ett | definite | plural | gloss | theme | example | example_en` per line.

    `plural` is the indefinite plural, or `-` for a noun with none.
    """
    out = []
    for f in rows(block):
        word, article, definite, plural, gloss, theme, example, example_en = f[:8]
        assert article in ("en", "ett"), word
        extras = {"article": article, "definite": definite}
        if plural and plural != "-":
            extras["plural"] = plural
        out.append(
            {
                "kind": "noun",
                "id": slug(word),
                "primary_form": word,
                "gloss": gloss,
                "extras": with_example(extras, example, example_en),
                "tags": [theme, article] + (extra_tags or []),
            }
        )
    return out


def adjectives(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`en, ett, pl | gloss | example | example_en` per line."""
    out = []
    for f in rows(block):
        en, ett, pl = (x.strip() for x in f[0].split(","))
        out.append(
            {
                "kind": "adjective",
                "id": slug(en),
                "primary_form": en,
                "gloss": f[1],
                "extras": with_example({"forms": {"en": en, "ett": ett, "pl": pl}}, f[2], f[3]),
                "tags": ["adjektiv"] + (extra_tags or []),
            }
        )
    return out


def phrases(block: str, tags: list[str]) -> list[dict]:
    """`form | meaning | example | example_en [| literal] [| note]` per line."""
    out = []
    for f in rows(block):
        literal = f[4] if len(f) > 4 and f[4] else None
        note = f[5] if len(f) > 5 and f[5] else None
        out.append(
            simple(
                "phrase",
                f[0],
                f[1],
                tags,
                literal=literal,
                note=note,
                example=f[2],
                example_en=f[3],
            )
        )
    return out


def verb(
    form: str,
    gloss: str,
    tags: list[str],
    *,
    group: str,
    example: str,
    example_en: str,
    **conj,
) -> dict:
    """A verb from its infinitive (with any particle or `sig`) and group.

    `conj` passes `pres`, `pret`, `sup`, `fut` or `future` on to
    `sv_conj.conjugate` for a verb whose parts no rule derives.
    """
    table = conjugate(form, group=group, **conj)
    particles = [w for w in form.split()[1:] if w != "sig"]
    extras = {
        "auxiliary": "ha",
        "supine": table["perfekt"]["1s"].split()[1],
        "past": table["preteritum"]["1s"].split()[0],
        "group": group,
    }
    if particles:
        extras["particle"] = " ".join(particles)
    if "sig" in form.split():
        extras["reflexive"] = True
    return {
        "kind": "verb",
        "id": slug(form),
        "primary_form": form,
        "gloss": gloss,
        "extras": with_example(extras, example, example_en),
        "tags": ["presens"] + tags,
        "conjugations": table,
    }
