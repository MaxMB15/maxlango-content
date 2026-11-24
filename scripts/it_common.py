"""Italian item constructors. Every row carries its own example sentence and
its English translation, so the Italian packs need no scripts/examples file."""

from __future__ import annotations

from common import rows, simple, slug, with_example
from fr_common import connectors  # language-agnostic
from it_conj import agreement_alternatives, conjugate

__all__ = ["nouns", "adjectives", "verb", "phrases", "connectors", "article_for"]

VOWEL_START = tuple("aeiouàèéìòùh")
# A masculine noun takes lo (and gli in the plural) before these sounds.
LO_START = ("gn", "ps", "pn", "x", "y", "z")


def article_for(word: str, gender: str) -> str:
    """The singular definite article: l' before a vowel (or a silent h), lo
    before s + consonant, z, gn, ps, pn, x and y, otherwise il or la."""
    w = word.lower()
    if w.startswith(VOWEL_START):
        return "l'"
    if gender == "f":
        return "la"
    if w.startswith(LO_START) or (w.startswith("s") and len(w) > 1 and w[1] not in "aeiouàèéìòù"):
        return "lo"
    return "il"


def nouns(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`word | m/f | gloss | theme | plural | example | example_en` per line.
    An empty plural marks a noun with no everyday plural (il latte)."""
    out = []
    for f in rows(block):
        word, g, gloss, theme, plural, example, example_en = f
        extras = {"gender": g, "article": article_for(word, g)}
        if plural:
            extras["plural"] = plural
        gender_tag = {"m": "maschile", "f": "femminile"}[g]
        out.append(
            {
                "kind": "noun",
                "id": slug(word),
                "primary_form": word,
                "gloss": gloss,
                "extras": with_example(extras, example, example_en),
                "tags": [theme, gender_tag] + (extra_tags or []),
            }
        )
    return out


def adjectives(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`ms, fs, mp, fp | gloss | example | example_en [| before]` per line;
    `before` marks an adjective that usually goes before its noun."""
    out = []
    for f in rows(block):
        ms, fs, mp, fp = (x.strip() for x in f[0].split(","))
        extras: dict = {"forms": {"ms": ms, "fs": fs, "mp": mp, "fp": fp}}
        if len(f) > 4 and f[4] == "before":
            extras["position"] = "usually before the noun"
        out.append(
            {
                "kind": "adjective",
                "id": slug(ms),
                "primary_form": ms,
                "gloss": f[1],
                "extras": with_example(extras, f[2], f[3]),
                "tags": ["aggettivi"] + (extra_tags or []),
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
    """A verb item. A reflexive infinitive (alzarsi) conjugates as alzare with
    the reflexive pronoun in every form, and takes essere."""
    refl = inf.endswith("si")
    base = inf[: -len("si")] + "e" if refl else inf
    aux = "essere" if refl else conj.get("aux", "avere")
    extras = with_example({"auxiliary": aux, "participle": pp}, example, example_en)
    if aux == "essere":
        extras["agreement"] = agreement_alternatives(pp)
    return {
        "kind": "verb",
        "id": slug(inf),
        "primary_form": inf,
        "gloss": gloss,
        "extras": extras,
        "tags": ["presente"] + tags,
        "conjugations": conjugate(base, pp=pp, refl=refl, **conj),
    }


def phrases(block: str, tags: list[str]) -> list[dict]:
    """`form | meaning | example | example_en [| literal] [| note]` per line."""
    out = []
    for f in rows(block):
        literal = f[4] if len(f) > 4 and f[4] else None
        note = f[5] if len(f) > 5 and f[5] else None
        item = simple("phrase", f[0], f[1], tags, literal=literal, note=note)
        item.setdefault("extras", {})
        with_example(item["extras"], f[2], f[3])
        # Keep the key order of the other kinds: extras before tags.
        item["tags"] = item.pop("tags")
        out.append(item)
    return out
