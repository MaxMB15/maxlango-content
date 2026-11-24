"""Italian conjugation for the pack builder.

Regular -are, -ere, -ire (dormire) and -isc- (finire) verbs are derived, with
the spelling changes that keep a stem's sound: cercare -> cerchi, cercherò;
mangiare -> mangi, mangerò. Anything irregular passes its present tense, and
where needed its future stem, imperfect stem and subjunctive, explicitly. Every
table is printed by `python3 it_conj.py VERB` so a reviewer can check it by eye.
"""

from __future__ import annotations

TENSES = ["presente", "passato-prossimo", "imperfetto", "futuro-semplice", "condizionale", "congiuntivo"]
PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
AVERE = ["ho", "hai", "ha", "abbiamo", "avete", "hanno"]
ESSERE = ["sono", "sei", "è", "siamo", "siete", "sono"]
REFL = ["mi", "ti", "si", "ci", "vi", "si"]
FUT_ENDINGS = ["ò", "ai", "à", "emo", "ete", "anno"]
COND_ENDINGS = ["ei", "esti", "ebbe", "emmo", "este", "ebbero"]
IMP_ENDINGS = ["vo", "vi", "va", "vamo", "vate", "vano"]


def _participle_forms(pp: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    """An essere-auxiliary or reflexive verb's past participle, per person: the
    inclusive display form (`andato/a`, `andati/e`) the passato prossimo is
    stored under, and the written alternatives (`["andato", "andata"]`) a
    learner's answer is checked against. Gender never changes the auxiliary,
    only this one trailing word.
    """
    if not pp.endswith("o"):
        raise ValueError(f"participle {pp} should end in -o")
    base = pp[:-1]
    display: dict[str, str] = {}
    agreement: dict[str, list[str]] = {}
    for i, person in enumerate(PERSONS):
        if i >= 3:  # plural
            display[person] = f"{base}i/e"
            agreement[person] = [base + "i", base + "e"]
        else:
            display[person] = f"{pp}/a"
            agreement[person] = [pp, base + "a"]
    return display, agreement


def agreement_alternatives(pp: str) -> dict[str, list[str]]:
    """Passato prossimo agreement alternatives for an essere-auxiliary or
    reflexive verb's past participle, keyed `"passato-prossimo.{person}"`,
    ready to splat straight into an item's extras.
    """
    _, agreement = _participle_forms(pp)
    return {f"passato-prossimo.{person}": forms for person, forms in agreement.items()}


def _are_stem_forms(stem: str) -> dict[str, str]:
    """The pieces of an -are stem that change spelling before -i and -e:
    cerc- -> cerchi, mangi- -> mangi (one i), parl- -> parli."""
    if stem.endswith(("c", "g")):
        return {"i": stem + "hi", "iamo": stem + "hiamo", "iate": stem + "hiate", "ino": stem + "hino",
                "fut": stem + "her"}
    if stem.endswith("i"):
        fut = stem[:-1] + "er" if stem.endswith(("ci", "gi")) else stem + "er"
        return {"i": stem, "iamo": stem + "amo", "iate": stem + "ate", "ino": stem + "no", "fut": fut}
    return {"i": stem + "i", "iamo": stem + "iamo", "iate": stem + "iate", "ino": stem + "ino", "fut": stem + "er"}


def _regular_present(inf: str, isc: bool) -> list[str]:
    stem = inf[:-3]
    if inf.endswith("are"):
        s = _are_stem_forms(stem)
        return [stem + "o", s["i"], stem + "a", s["iamo"], stem + "ate", stem + "ano"]
    if inf.endswith("ere"):
        return [stem + "o", stem + "i", stem + "e", stem + "iamo", stem + "ete", stem + "ono"]
    if inf.endswith("ire"):
        if isc:
            return [stem + "isco", stem + "isci", stem + "isce", stem + "iamo", stem + "ite", stem + "iscono"]
        return [stem + "o", stem + "i", stem + "e", stem + "iamo", stem + "ite", stem + "ono"]
    raise ValueError(f"no regular pattern for {inf}")


def _regular_subjunctive(inf: str, pres: list[str]) -> list[str]:
    """-are: parli, parliamo, parliate, parlino. -ere/-ire: from the io form,
    vendo -> venda, finisco -> finisca. Noi is always the present's noi, and
    voi swaps its -mo for -te: vendiamo -> vendiate."""
    if inf.endswith("are"):
        s = _are_stem_forms(inf[:-3])
        sing = s["i"]
        return [sing, sing, sing, pres[3], s["iate"], s["ino"]]
    sing = pres[0][:-1] + "a"
    return [sing, sing, sing, pres[3], pres[3][: -len("mo")] + "te", sing + "no"]


def _with_refl(forms: list[str]) -> list[str]:
    return [f"{pron} {form}" for pron, form in zip(REFL, forms)]


def conjugate(
    inf: str,
    *,
    pp: str,
    aux: str = "avere",
    present: str | None = None,
    fut: str | None = None,
    subj: str | None = None,
    imp: str | None = None,
    imperfetto: str | None = None,
    refl: bool = False,
    isc: bool = False,
) -> dict[str, dict[str, str]]:
    """All six profile tenses, keyed tense -> person -> form.

    `inf` is the plain infinitive (alzare, not alzarsi). `present` and `subj`
    are six space-separated forms. `fut` is the future and conditional stem
    (default: the infinitive minus its final e, with -are -> -er and the
    -care/-ciare spellings). `imp` is the imperfect stem, the part before
    -vo (default: the infinitive minus -re: parla-, vende-, dormi-), and
    `imperfetto` six whole forms for the one verb that fits no stem (essere).
    """
    pres = present.split() if present else _regular_present(inf, isc)
    assert len(pres) == 6, inf
    imp_base = imp or inf[: -len("re")]
    imp_forms = imperfetto.split() if imperfetto else [imp_base + e for e in IMP_ENDINGS]
    assert len(imp_forms) == 6, inf
    if fut:
        fstem = fut
    elif inf.endswith("are"):
        fstem = _are_stem_forms(inf[:-3])["fut"]
    else:
        fstem = inf[:-1]
    futuro = [fstem + e for e in FUT_ENDINGS]
    cond = [fstem + e for e in COND_ENDINGS]
    congiuntivo = subj.split() if subj else _regular_subjunctive(inf, pres)
    assert len(congiuntivo) == 6, inf

    use_essere = aux == "essere" or refl
    if use_essere:
        display, _ = _participle_forms(pp)
        pp_forms = [f"{a} {display[person]}" for a, person in zip(ESSERE, PERSONS)]
    else:
        pp_forms = [f"{a} {pp}" for a in AVERE]

    table = [pres, pp_forms, imp_forms, futuro, cond, congiuntivo]
    if refl:
        table = [_with_refl(forms) for forms in table]
    return {t: dict(zip(PERSONS, forms)) for t, forms in zip(TENSES, table)}


if __name__ == "__main__":
    import sys

    import it

    wanted = set(sys.argv[1:])
    for p in it.PACKS:
        for item in p["items"]:
            if item["kind"] == "verb" and (not wanted or item["id"] in wanted or item["primary_form"] in wanted):
                print(f"== {item['primary_form']} ({item['extras'].get('auxiliary')}, {item['extras'].get('participle')})")
                for t, forms in item["conjugations"].items():
                    print(f"  {t:17} " + ", ".join(forms.values()))
