"""Dutch item constructors."""

from __future__ import annotations

from common import rows, slug, with_example
from fr_common import connectors, phrases  # language-agnostic
from nl_conj import conjugate, participle

__all__ = ["nouns", "adjectives", "verb", "phrases", "connectors"]


def nouns(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`word | de/het | plural | gloss | theme` per line."""
    out = []
    for f in rows(block):
        word, article, plural, gloss, theme = f[:5]
        extras = {"article": article}
        if plural and plural != "-":
            extras["plural"] = plural
        out.append(
            {
                "kind": "noun",
                "id": slug(word),
                "primary_form": word,
                "gloss": gloss,
                "extras": extras,
                "tags": [theme, article] + (extra_tags or []),
            }
        )
    return out


def adjectives(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`base, inflected | gloss` per line."""
    out = []
    for f in rows(block):
        base, inflected = (x.strip() for x in f[0].split(","))
        out.append(
            {
                "kind": "adjective",
                "id": slug(base),
                "primary_form": base,
                "gloss": f[1],
                "extras": {"forms": {"base": base, "inflected": inflected}},
                "tags": ["bijvoeglijke-naamwoorden"] + (extra_tags or []),
            }
        )
    return out


def verb(
    inf: str,
    stem: str,
    gloss: str,
    tags: list[str],
    *,
    example: str | None = None,
    example_en: str | None = None,
    **conj,
) -> dict:
    core = inf.removeprefix("zich ")
    table = conjugate(core, stem, **conj)
    extras = {
        "auxiliary": conj.get("aux", "hebben"),
        "participle": participle(core, stem, **conj),
        "past": table["onvoltooid-verleden-tijd"]["1s"].split()[0]
        + " / "
        + table["onvoltooid-verleden-tijd"]["1p"].split()[0],
    }
    if conj.get("prefix"):
        extras["separable"] = conj["prefix"]
    return {
        "kind": "verb",
        "id": slug(inf),
        "primary_form": inf,
        "gloss": gloss,
        "extras": with_example(extras, example, example_en),
        "tags": ["tegenwoordige-tijd"] + tags,
        "conjugations": table,
    }
