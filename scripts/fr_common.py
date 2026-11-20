"""French item constructors."""

from __future__ import annotations

from common import rows, simple, slug, with_example
from fr_conj import agreement_alternatives, conjugate

H_ASPIRE = "*"  # prefix marking an h aspiré noun: no elision, "le haricot"
VOWEL_START = tuple("aeiouyéèêâîôûœh")


def nouns(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`word | m/f | gloss | theme [| plural]` per line."""
    out = []
    for f in rows(block):
        word, g, gloss, theme = f[0], f[1], f[2], f[3]
        plural = f[4] if len(f) > 4 and f[4] else None
        aspire = word.startswith(H_ASPIRE)
        word = word.lstrip(H_ASPIRE)
        if word.startswith(VOWEL_START) and not aspire:
            article = "l'"
        else:
            article = "le" if g == "m" else "la"
        extras = {"gender": g, "article": article}
        if plural:
            extras["plural"] = plural
        gender_tag = {"m": "masculin", "f": "féminin"}[g]
        out.append(
            {
                "kind": "noun",
                "id": slug(word),
                "primary_form": word,
                "gloss": gloss,
                "extras": extras,
                "tags": [theme, gender_tag] + (extra_tags or []),
            }
        )
    return out


def adjectives(block: str) -> list[dict]:
    """`ms fs mp fp | gloss [| before]` per line; `before` marks BAGS position."""
    out = []
    for f in rows(block):
        ms, fs, mp, fp = f[0].split(",")
        extras = {"forms": {"ms": ms.strip(), "fs": fs.strip(), "mp": mp.strip(), "fp": fp.strip()}}
        if len(f) > 2 and f[2] == "before":
            extras["position"] = "before the noun"
        out.append(
            {
                "kind": "adjective",
                "id": slug(ms.strip()),
                "primary_form": ms.strip(),
                "gloss": f[1],
                "extras": extras,
                "tags": ["adjectifs"],
            }
        )
    return out


def verb(
    inf: str,
    gloss: str,
    tags: list[str],
    *,
    pp: str,
    example: str | None = None,
    example_en: str | None = None,
    **conj,
) -> dict:
    refl = conj.get("refl", False)
    aux = "être" if refl else conj.get("aux", "avoir")
    extras = with_example({"auxiliary": aux, "participle": pp}, example, example_en)
    if aux == "être":
        extras["agreement"] = agreement_alternatives(pp)
    return {
        "kind": "verb",
        "id": slug(inf),
        "primary_form": inf,
        "gloss": gloss,
        "extras": extras,
        "tags": ["présent"] + tags,
        "conjugations": conjugate(inf.removeprefix("se ").removeprefix("s'"), pp=pp, **conj),
    }


def phrases(block: str, tags: list[str]) -> list[dict]:
    """`form | meaning [| literal] [| note]` per line."""
    out = []
    for f in rows(block):
        literal = f[2] if len(f) > 2 and f[2] else None
        note = f[3] if len(f) > 3 and f[3] else None
        out.append(simple("phrase", f[0], f[1], tags, literal=literal, note=note))
    return out


def connectors(kind: str, block: str, tags: list[str]) -> list[dict]:
    """`form | gloss | role | example | example_en [| alternative ...]` per line.

    Any field after example_en is another word order the Build-the-sentence
    game accepts for the example.
    """
    out = []
    for f in rows(block):
        extras = {"role": f[2], "example": f[3], "example_en": f[4]}
        if f[5:]:
            extras["example_alternatives"] = f[5:]
        out.append(
            {
                "kind": kind,
                "id": slug(f[0]),
                "primary_form": f[0],
                "gloss": f[1],
                "extras": extras,
                "tags": tags,
            }
        )
    return out
