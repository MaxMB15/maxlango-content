"""Spanish item constructors."""

from __future__ import annotations

import re

from common import rows, simple, slug, with_example
from es_conj import conjugate
from fr_common import connectors  # noqa: F401  (language-agnostic, re-exported)

# Feminine nouns that start with a stressed a- or ha- take el in the
# singular (el agua fría) and stay feminine everywhere else (las aguas).
EL_FEMININE = {"agua", "hambre", "aula", "alma", "área", "águila", "hacha", "arma"}
GENDER_TAG = {"m": "masculino", "f": "femenino"}
ACCENTED = "áéíóú"
PLAIN = str.maketrans(ACCENTED, "aeiou")


def plural_of(word: str) -> str:
    """The regular plural, or a ValueError where the rules need a human."""
    if " " in word:
        raise ValueError(f"{word}: give the plural of a compound explicitly")
    last = word[-1]
    if last in "aeiouáéó":
        return word + "s"
    if last == "z":
        return word[:-1] + "ces"
    if last in "íúsx":
        raise ValueError(f"{word}: give the plural explicitly")
    if word[-2] in ACCENTED:
        # canción, canciones; autobús is handled above; the accent goes.
        return word[:-2] + word[-2].translate(PLAIN) + last + "es"
    syllables = len(re.findall(r"[aeiouáéíóú]+", word))
    if last == "n" and syllables > 1 and not any(c in ACCENTED for c in word):
        # joven, jóvenes: an extra syllable needs a written accent.
        raise ValueError(f"{word}: give the plural explicitly")
    return word + "es"


def nouns(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`word | m/f | gloss | theme | plural | example | example_en [| note]` per line.

    An empty plural is derived; `-` means the noun has none in normal use.
    """
    out = []
    for f in rows(block):
        word, g, gloss, theme, plural, example, example_en = f[:7]
        note = f[7] if len(f) > 7 and f[7] else None
        article = "el" if g == "m" or word in EL_FEMININE else "la"
        extras: dict = {"gender": g, "article": article}
        if plural != "-":
            extras["plural"] = plural or plural_of(word)
        with_example(extras, example, example_en)
        if note:
            extras["note"] = note
        out.append(
            {
                "kind": "noun",
                "id": slug(word),
                "primary_form": word,
                "gloss": gloss,
                "extras": extras,
                "tags": [theme, GENDER_TAG[g]] + (extra_tags or []),
            }
        )
    return out


def adjectives(block: str, extra_tags: list[str] | None = None) -> list[dict]:
    """`ms, fs, mp, fp | gloss | example | example_en [| note]` per line."""
    out = []
    for f in rows(block):
        ms, fs, mp, fp = (x.strip() for x in f[0].split(","))
        extras: dict = {"forms": {"ms": ms, "fs": fs, "mp": mp, "fp": fp}}
        with_example(extras, f[2], f[3])
        if len(f) > 4 and f[4]:
            extras["note"] = f[4]
        out.append(
            {
                "kind": "adjective",
                "id": slug(ms),
                "primary_form": ms,
                "gloss": f[1],
                "extras": extras,
                "tags": ["adjetivos"] + (extra_tags or []),
            }
        )
    return out


def verb(
    inf: str,
    gloss: str,
    tags: list[str],
    *,
    example: str,
    example_en: str,
    note: str | None = None,
    **conj,
) -> dict:
    """A verb; an infinitive ending in -rse is reflexive in every form."""
    refl = inf.endswith("rse")
    base = inf[:-2] if refl else inf
    table = conjugate(base, refl=refl, **conj)
    pp = table["pretérito-perfecto"]["1s"].split()[-1]
    extras = with_example({"auxiliary": "haber", "participle": pp}, example, example_en)
    if note:
        extras["note"] = note
    return {
        "kind": "verb",
        "id": slug(inf),
        "primary_form": inf,
        "gloss": gloss,
        "extras": extras,
        "tags": ["presente"] + (["reflexivos"] if refl else []) + tags,
        "conjugations": table,
    }


def phrases(block: str, tags: list[str]) -> list[dict]:
    """`form | meaning | example | example_en [| literal] [| note]` per line."""
    out = []
    for f in rows(block):
        literal = f[4] if len(f) > 4 and f[4] else None
        note = f[5] if len(f) > 5 and f[5] else None
        out.append(
            simple("phrase", f[0], f[1], tags, literal=literal, note=note, example=f[2], example_en=f[3])
        )
    return out
