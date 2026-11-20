"""French conjugation for the pack builder.

Regular -er, -ir (finir) and -re (vendre) verbs are derived. Anything irregular
passes its present tense, and where needed its future stem and subjunctive,
explicitly. Every derived table is printed by `python3 fr_conj.py VERB` so a
reviewer can check it by eye.
"""

from __future__ import annotations

TENSES = ["présent", "passé-composé", "imparfait", "futur-simple", "conditionnel", "subjonctif"]
PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
AVOIR = ["ai", "as", "a", "avons", "avez", "ont"]
ETRE = ["suis", "es", "est", "sommes", "êtes", "sont"]
REFL = ["me", "te", "se", "nous", "vous", "se"]
VOWELS = tuple("aeiouéèêâîôûhœ")


def _participle_forms(pp: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    """An être-auxiliary or reflexive verb's past participle, per person: the
    inclusive display form (`allé(e)`, `allé(e)s`) passé composé is stored
    under, and the accepted written alternatives (`["allé", "allée"]`) a
    learner's answer is checked against. Gender never changes the auxiliary,
    only this one trailing word.
    """
    fem = pp if pp.endswith("e") else pp + "e"
    display: dict[str, str] = {}
    agreement: dict[str, list[str]] = {}
    for i, person in enumerate(PERSONS):
        if i >= 3:  # plural
            masc = pp if pp.endswith("s") else pp + "s"
            femp = fem if fem.endswith("s") else fem + "s"
            display[person] = f"{pp}(es)" if pp.endswith("s") else f"{pp}(e)s"
            agreement[person] = [masc, femp]
        else:
            display[person] = f"{pp}(e)"
            agreement[person] = [pp, fem]
    return display, agreement


def agreement_alternatives(pp: str) -> dict[str, list[str]]:
    """Passé composé agreement alternatives for an être-auxiliary or reflexive
    verb's past participle, keyed `"passé-composé.{person}"` — design.md's
    `extras.agreement` format, ready to splat straight into an item's extras.
    """
    _, agreement = _participle_forms(pp)
    return {f"passé-composé.{person}": forms for person, forms in agreement.items()}


def _regular_present(inf: str) -> list[str]:
    stem = inf[:-2]
    if inf.endswith("er"):
        nous = stem + ("eons" if stem.endswith("g") else "ons")
        if stem.endswith("c"):
            nous = stem[:-1] + "çons"
        return [stem + "e", stem + "es", stem + "e", nous, stem + "ez", stem + "ent"]
    if inf.endswith("ir"):
        return [stem + "is", stem + "is", stem + "it", stem + "issons", stem + "issez", stem + "issent"]
    if inf.endswith("re"):
        return [stem + "s", stem + "s", stem, stem + "ons", stem + "ez", stem + "ent"]
    raise ValueError(f"no regular pattern for {inf}")


def _join(base: str, ending: str) -> str:
    # mange- + ions -> mangions; commenç- + ions -> commencions
    if ending.startswith("i"):
        if base.endswith("ge"):
            return base[:-1] + ending
        if base.endswith("ç"):
            return base[:-1] + "c" + ending
    return base + ending


def _refl(forms: list[str]) -> list[str]:
    out = []
    for pron, form in zip(REFL, forms):
        if pron in ("me", "te", "se") and form.startswith(VOWELS):
            out.append(pron[0] + "'" + form)
        else:
            out.append(pron + " " + form)
    return out


def conjugate(
    inf: str,
    *,
    pp: str,
    aux: str = "avoir",
    present: str | None = None,
    fut: str | None = None,
    subj: str | None = None,
    imp: str | None = None,
    refl: bool = False,
) -> dict[str, dict[str, str]]:
    """All six profile tenses, keyed tense -> person -> form.

    `present` and `subj` are six space-separated forms. `fut` is the future and
    conditional stem (default: the infinitive, minus the final e of -re).
    `imp` is the imperfect stem (default: the nous form minus -ons).
    """
    pres = present.split() if present else _regular_present(inf)
    assert len(pres) == 6, inf
    imp_base = imp or pres[3][: -len("ons")]
    imparfait = [_join(imp_base, e) for e in ["ais", "ais", "ait", "ions", "iez", "aient"]]
    fstem = fut or (inf[:-1] if inf.endswith("re") else inf)
    futur = [fstem + e for e in ["ai", "as", "a", "ons", "ez", "ont"]]
    cond = [fstem + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]]
    if subj:
        subjonctif = subj.split()
    else:
        base = pres[5][: -len("ent")]
        subjonctif = [base + "e", base + "es", base + "e", imparfait[3], imparfait[4], base + "ent"]
    assert len(subjonctif) == 6, inf

    use_etre = aux == "être" or refl
    auxes = ETRE if use_etre else AVOIR
    if use_etre:
        display, _ = _participle_forms(pp)
        pc = [f"{a} {display[person]}" for a, person in zip(auxes, PERSONS)]
    else:
        pc = [f"{a} {pp}" for a in auxes]

    table = [pres, pc, imparfait, futur, cond, subjonctif]
    if refl:
        table = [_refl(forms) for forms in table]
    return {t: dict(zip(PERSONS, forms)) for t, forms in zip(TENSES, table)}


if __name__ == "__main__":
    import sys

    import fr

    wanted = set(sys.argv[1:])
    for p in fr.PACKS:
        for it in p["items"]:
            if it["kind"] == "verb" and (not wanted or it["id"] in wanted):
                print(f"== {it['primary_form']}")
                for t, forms in it["conjugations"].items():
                    print(f"  {t:14} " + ", ".join(forms.values()))
