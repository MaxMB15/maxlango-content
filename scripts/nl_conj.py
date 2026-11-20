"""Dutch conjugation for the pack builder.

Every verb passes its ik-form stem (spelling rules for open and closed
syllables are easier to state than to derive). Weak verbs derive their past and
participle through 't kofschip; strong and irregular verbs pass them.
`python3 nl_conj.py VERB` prints the tables for review.
"""

from __future__ import annotations

TENSES = [
    "tegenwoordige-tijd",
    "voltooid-tegenwoordige-tijd",
    "onvoltooid-verleden-tijd",
    "toekomende-tijd",
]
HEBBEN = ["heb", "hebt", "heeft", "hebben", "hebben", "hebben"]
ZIJN = ["ben", "bent", "is", "zijn", "zijn", "zijn"]
ZULLEN = ["zal", "zult", "zal", "zullen", "zullen", "zullen"]
REFL = ["me", "je", "zich", "ons", "je", "zich"]
UNSTRESSED = ("be", "ge", "ver", "her", "ont", "er")


def _kofschip(raw: str) -> bool:
    """True when the stem ends in a voiceless sound: past in -te, participle in -t."""
    return raw.endswith("ch") or raw[-1] in "tkfsxp"


def conjugate(
    inf: str,
    stem: str,
    *,
    aux: str = "hebben",
    present: str | None = None,
    past: str | None = None,
    pp: str | None = None,
    prefix: str | None = None,
    refl: bool = False,
) -> dict[str, dict[str, str]]:
    """All four profile tenses, keyed tense -> person -> form.

    `inf` is the full infinitive (`opbellen`), `stem` the ik-form without any
    separable prefix (`bel`). `present` is six forms without the prefix,
    `past` is "singular plural" (`at aten`), `pp` the full participle.
    """
    core = inf[len(prefix) :] if prefix else inf
    if present:
        pres = present.split()
    else:
        t = "" if stem.endswith("t") else "t"
        pres = [stem, stem + t, stem + t, core, core, core]
    assert len(pres) == 6, inf

    raw = core[:-2] if core.endswith("en") else core[:-1]
    voiceless = _kofschip(raw)
    if past:
        sg, pl = past.split()
    else:
        sg = stem + ("te" if voiceless else "de")
        pl = sg + "n"
    if not pp:
        # An unstressed prefix needs a real verb after it: be-talen, but bellen.
        unstressed = any(core.startswith(u) and len(core) - len(u) >= 5 for u in UNSTRESSED)
        ge = "" if unstressed else "ge"
        end = "" if stem.endswith(("t", "d")) else ("t" if voiceless else "d")
        pp = ge + stem + end
    if prefix and not pp.startswith(prefix):
        pp = prefix + pp

    r = REFL if refl else [""] * 6
    tail = f" {prefix}" if prefix else ""

    def finite(form: str, i: int) -> str:
        return " ".join(x for x in (form, r[i]) if x) + tail

    auxes = ZIJN if aux == "zijn" else HEBBEN
    table = [
        [finite(f, i) for i, f in enumerate(pres)],
        [" ".join(x for x in (a, r[i], pp) if x) for i, a in enumerate(auxes)],
        [finite(f, i) for i, f in enumerate([sg, sg, sg, pl, pl, pl])],
        [" ".join(x for x in (z, r[i], inf) if x) for i, z in enumerate(ZULLEN)],
    ]
    persons = ["1s", "2s", "3s", "1p", "2p", "3p"]
    return {t: dict(zip(persons, forms)) for t, forms in zip(TENSES, table)}


def participle(inf: str, stem: str, **kw) -> str:
    return conjugate(inf, stem, **kw)["voltooid-tegenwoordige-tijd"]["1p"].split()[-1]


if __name__ == "__main__":
    import sys

    import nl

    wanted = set(sys.argv[1:])
    for p in nl.PACKS:
        for it in p["items"]:
            if it["kind"] == "verb" and (not wanted or it["id"] in wanted):
                print(f"== {it['primary_form']}")
                for t, forms in it["conjugations"].items():
                    print(f"  {t[:12]:12} " + ", ".join(forms.values()))
