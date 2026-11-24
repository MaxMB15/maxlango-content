"""Swedish conjugation for the pack builder.

A Swedish verb has one form for all six persons in each tense, so a table is
the verb's principal parts written out six times: presens (`talar`),
preteritum (`talade`) and the supine (`talat`), which perfekt puts after
`har`. Futurum is `ska` + the infinitive.

Regular verbs derive their parts from their group:

    1   tala  talar  talade  talat
    2a  stänga  stänger  stängde  stängt
    2b  köpa  köper  köpte  köpt
    3   bo  bor  bodde  bott

Group 4 (strong and irregular) verbs, and any verb a rule gets wrong, pass
their parts explicitly. A verb's form may be a phrase: the first word is the
verb, every `sig` becomes the person's reflexive pronoun, and any other word
(a particle, a preposition) stays where it is: `klä på sig` gives
`klär på mig`, `har klätt på mig`.

`python3 sv_conj.py VERB` prints the tables for review.
"""

from __future__ import annotations

TENSES = ["presens", "perfekt", "preteritum", "futurum"]
PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
REFL = ["mig", "dig", "sig", "oss", "er", "sig"]
VOWELS = "aeiouyåäö"


def _simplify(stem: str) -> str:
    """kän-n → kän before -de/-t: känna → kände, känt; glömma → glömde, glömt."""
    if stem.endswith(("mm", "nn")):
        return stem[:-1]
    return stem


def principal_parts(inf: str, group: str) -> tuple[str, str, str]:
    """(presens, preteritum, supine) of a regular verb."""
    if group == "1":
        assert inf.endswith("a"), inf
        return inf + "r", inf + "de", inf + "t"
    if group == "3":
        return inf + "r", inf + "dde", inf + "tt"
    if group in ("2a", "2b"):
        assert inf.endswith("a"), inf
        stem = inf[:-1]
        pres = stem if stem.endswith("r") else stem + "er"
        base = _simplify(stem)
        if group == "2a":
            if base.endswith("d") and base[-2] in VOWELS:
                # betyda → betydde, betytt
                return pres, base + "de", base[:-1] + "tt"
            if base.endswith("d"):
                # använda → använde, använt
                return pres, base + "e", base[:-1] + "t"
            return pres, base + "de", base + "t"
        if base.endswith("t") and base[-2] in VOWELS:
            # möta → mötte, mött
            return pres, base + "te", base + "t"
        if base.endswith("t"):
            # gifta → gifte, gift
            return pres, base + "e", base
        return pres, base + "te", base + "t"
    raise ValueError(f"{inf}: group {group} needs explicit parts")


def conjugate(
    form: str,
    *,
    group: str,
    pres: str | None = None,
    pret: str | None = None,
    sup: str | None = None,
    fut: str = "ska",
    future: str | None = None,
) -> dict[str, dict[str, str]]:
    """All four profile tenses, keyed tense -> person -> form.

    `form` is the infinitive, with any particle or `sig` after it.
    `pres`, `pret` and `sup` override the derived parts of its first word;
    `fut` is the future auxiliary (`ska`, or `kommer att` where ska would
    sound like a plan rather than a prediction). `future` replaces the
    whole futurum form, for a verb with no infinitive of its own (måste).
    """
    head, *rest = form.split()
    if group == "4" or (pres and pret and sup):
        assert pres and pret and sup, form
        parts = (pres, pret, sup)
    else:
        derived = principal_parts(head, group)
        parts = (pres or derived[0], pret or derived[1], sup or derived[2])
    p_pres, p_pret, p_sup = parts

    def fill(verb: str, i: int) -> str:
        return " ".join([verb] + [REFL[i] if w == "sig" else w for w in rest])

    table = [
        [fill(p_pres, i) for i in range(6)],
        ["har " + fill(p_sup, i) for i in range(6)],
        [fill(p_pret, i) for i in range(6)],
        [future or f"{fut} " + fill(head, i) for i in range(6)],
    ]
    return {t: dict(zip(PERSONS, forms)) for t, forms in zip(TENSES, table)}


if __name__ == "__main__":
    import sys

    import sv

    wanted = set(sys.argv[1:])
    for p in sv.PACKS:
        for it in p["items"]:
            if it["kind"] == "verb" and (not wanted or it["id"] in wanted or it["primary_form"] in wanted):
                print(f"== {it['primary_form']}  ({it['extras'].get('group')})")
                for t, forms in it["conjugations"].items():
                    print(f"  {t[:12]:12} " + ", ".join(dict.fromkeys(forms.values())))
