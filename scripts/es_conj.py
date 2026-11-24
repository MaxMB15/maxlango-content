"""Spanish conjugation for the pack builder.

Regular -ar, -er and -ir verbs are derived, and so are the three stem changes
(e>ie, o>ue, e>i, plus jugar's u>ue), the -zco present of conocer and its
kind, and the spelling changes of -car, -gar and -zar. Anything else passes
its irregular forms explicitly. Every table is printed by
`python3 es_conj.py VERB` so a reviewer can check it by eye.
"""

from __future__ import annotations

TENSES = [
    "presente",
    "pretérito-perfecto",
    "pretérito-indefinido",
    "imperfecto",
    "futuro",
    "condicional",
    "subjuntivo",
]
PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
HABER = ["he", "has", "ha", "hemos", "habéis", "han"]
REFL = ["me", "te", "se", "nos", "os", "se"]

PRESENT = {
    "ar": ["o", "as", "a", "amos", "áis", "an"],
    "er": ["o", "es", "e", "emos", "éis", "en"],
    "ir": ["o", "es", "e", "imos", "ís", "en"],
}
PRETERITE = {
    "ar": ["é", "aste", "ó", "amos", "asteis", "aron"],
    "er": ["í", "iste", "ió", "imos", "isteis", "ieron"],
    "ir": ["í", "iste", "ió", "imos", "isteis", "ieron"],
}
# tuve, tuviste, tuvo: the unstressed endings of the irregular preterites.
STRONG = ["e", "iste", "o", "imos", "isteis", "ieron"]
IMPERFECT = {
    "ar": ["aba", "abas", "aba", "ábamos", "abais", "aban"],
    "er": ["ía", "ías", "ía", "íamos", "íais", "ían"],
    "ir": ["ía", "ías", "ía", "íamos", "íais", "ían"],
}
SUBJUNCTIVE = {
    "ar": ["e", "es", "e", "emos", "éis", "en"],
    "er": ["a", "as", "a", "amos", "áis", "an"],
    "ir": ["a", "as", "a", "amos", "áis", "an"],
}
FUTURE = ["é", "ás", "á", "emos", "éis", "án"]
CONDITIONAL = ["ía", "ías", "ía", "íamos", "íais", "ían"]

# The forms of the most irregular verbs, shared by a verb and its reflexive
# or compound relatives (ir and irse).
IR = dict(
    pp="ido",
    present="voy vas va vamos vais van",
    pret="fui fuiste fue fuimos fuisteis fueron",
    imp="iba ibas iba íbamos ibais iban",
    subj="vaya vayas vaya vayamos vayáis vayan",
)


def group(inf: str) -> str:
    """ar, er or ir; oír and reír count as -ir."""
    end = inf[-2:].replace("í", "i")
    if end not in PRESENT:
        raise ValueError(f"{inf}: not an infinitive")
    return end


def _shift(stem: str, change: str) -> str:
    """Apply a stem change such as "e>ie" to the last matching vowel."""
    old, new = change.split(">")
    i = stem.rfind(old)
    if i < 0:
        raise ValueError(f"{stem}: no '{old}' for {change}")
    return stem[:i] + new + stem[i + len(old) :]


def _weak(stem: str, change: str | None, grp: str) -> str:
    """The -ir verbs' second change (pidió, durmió, sintamos): e>i, o>u."""
    if grp != "ir" or not change:
        return stem
    old = change.split(">")[0]
    return _shift(stem, f"{old}>{'i' if old == 'e' else 'u'}")


def _before_e(stem: str) -> str:
    """Keep the sound of -car, -gar and -zar before an e: busqu-, llegu-, empec-."""
    if stem.endswith("c"):
        return stem[:-1] + "qu"
    if stem.endswith("g"):
        return stem + "u"
    if stem.endswith("z"):
        return stem[:-1] + "c"
    return stem


def _six(forms: str | None, inf: str, what: str) -> list[str] | None:
    if forms is None:
        return None
    out = forms.split()
    if len(out) != 6:
        raise ValueError(f"{inf}: {what} needs six forms, got {len(out)}")
    return out


def conjugate(
    inf: str,
    *,
    pp: str | None = None,
    present: str | None = None,
    pret: str | None = None,
    pret_stem: str | None = None,
    imp: str | None = None,
    fut: str | None = None,
    subj: str | None = None,
    stem: str | None = None,
    zc: bool = False,
    refl: bool = False,
) -> dict[str, dict[str, str]]:
    """All seven profile tenses, keyed tense -> person -> form.

    `present`, `pret`, `imp` and `subj` are six space-separated forms.
    `pret_stem` gives a strong preterite (tuv- makes tuve, tuviste, tuvo).
    `fut` is the future and conditional stem (default: the infinitive).
    `stem` is a stem change, "e>ie", "o>ue", "e>i" or "u>ue", applied where
    the stress falls on the stem. `zc` makes the yo form -zco (conozco).
    `refl` puts me, te, se, nos, os, se before every form.
    """
    grp = group(inf)
    base = inf[:-2]
    strong = _shift(base, stem) if stem else base

    pres = _six(present, inf, "present")
    if pres is None:
        ends = PRESENT[grp]
        pres = [(strong if i in (0, 1, 2, 5) else base) + e for i, e in enumerate(ends)]
        if zc:
            pres[0] = base[:-1] + "zco"

    preterite = _six(pret, inf, "pret")
    if preterite is None and pret_stem:
        ends = list(STRONG)
        if pret_stem.endswith("j"):
            ends[5] = "eron"  # dijeron, trajeron, condujeron
        preterite = [pret_stem + e for e in ends]
    if preterite is None:
        ends = PRETERITE[grp]
        weak = _weak(base, stem, grp)
        preterite = [
            (_before_e(base) if i == 0 and grp == "ar" else weak if i in (2, 5) else base) + e
            for i, e in enumerate(ends)
        ]

    imperfect = _six(imp, inf, "imp") or [base + e for e in IMPERFECT[grp]]

    fstem = fut or inf.replace("í", "i")
    future = [fstem + e for e in FUTURE]
    conditional = [fstem + e for e in CONDITIONAL]

    subjunctive = _six(subj, inf, "subj")
    if subjunctive is None:
        if not pres[0].endswith("o"):
            raise ValueError(f"{inf}: yo form {pres[0]} gives no subjunctive stem; pass subj")
        yo = pres[0][:-1]
        ends = SUBJUNCTIVE[grp]
        fix = _before_e if grp == "ar" else (lambda s: s)
        if stem:
            # pensemos, volvamos: the stress leaves the stem, and so does the change.
            low = _weak(base, stem, grp)
            subjunctive = [fix(low if i in (3, 4) else yo) + e for i, e in enumerate(ends)]
        else:
            subjunctive = [fix(yo) + e for e in ends]

    participle = pp or base + ("ado" if grp == "ar" else "ido")
    perfect = [f"{h} {participle}" for h in HABER]

    table = [pres, perfect, preterite, imperfect, future, conditional, subjunctive]
    if refl:
        table = [[f"{r} {f}" for r, f in zip(REFL, forms)] for forms in table]
    return {t: dict(zip(PERSONS, forms)) for t, forms in zip(TENSES, table)}


if __name__ == "__main__":
    import sys

    import es

    wanted = set(sys.argv[1:])
    for p in es.PACKS:
        for it in p["items"]:
            if it["kind"] == "verb" and (not wanted or it["id"] in wanted or it["primary_form"] in wanted):
                print(f"== {it['primary_form']}  (pp {it['extras']['participle']})")
                for t, forms in it["conjugations"].items():
                    print(f"  {t:22} " + ", ".join(forms.values()))
