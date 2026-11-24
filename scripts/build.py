#!/usr/bin/env python3
"""Build every language's Base Packs from the sources in this directory.

    python3 scripts/build.py            # write packs/<lang>/*.json and catalog.json
    python3 scripts/build.py --check    # validate only, write nothing
    python3 scripts/build.py --out DIR  # write into DIR/packs and DIR/catalog.json instead
    python3 scripts/build.py --lang es  # build one language's packs only, no catalog

Each language module (fr.py, nl.py, es.py, it.py, sv.py) exposes PACKS: a list of dicts with the pack
header, an optional profile_delta and the items. This script validates them
against the rules the app enforces against each language's profile
(languages/<lang>/profile.json) and writes one JSON file per pack, plus
catalog.json: every pack's version, location, size and checksum in curriculum
order, which is what an app reads to install and update packs (see catalog.py).

Across each language's packs it also checks that every concept a learner can
tap as a Tag opens exactly one page (check_tag_pages), and on each page that
no game's answer is already printed (gap_answers.py).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LANGUAGE_DIR = ROOT / "languages"
PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
# Every language with Base Packs, in the order the catalog lists them. Each
# code names a module in this directory and a folder in languages/.
LANGUAGES = ("fr", "nl", "es", "it", "sv")

sys.path.insert(0, str(HERE))

from gap_answers import check_gap_answers  # noqa: E402


def word_span_count(text: str, word: str) -> int:
    """How often `word` occurs in `text` as a whole word (mirrors lang/cloze.ts)."""
    pattern = r"(?<![^\W_])" + re.escape(word.strip()) + r"(?![^\W_])"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def validate(pack: dict, profile: dict, seen_concepts: set[str]) -> list[str]:
    errors: list[str] = []
    tenses = [c["id"] for c in profile["concepts"] if c["kind"] == "tense"]
    roles = {c["id"] for c in profile["concepts"] if c["kind"].endswith("-class")}
    known = {c["id"] for c in profile["concepts"]} | seen_concepts
    roles |= {c for c in seen_concepts if c.startswith(("conn-", "conj-"))}
    for c in pack.get("profile_delta", []):
        known.add(c["id"])
        roles.add(c["id"]) if c["kind"].endswith("-class") else None
    for c in pack.get("profile_delta", []):
        for d in c.get("dependsOn", []):
            if d not in known:
                errors.append(f"delta concept {c['id']} depends on unknown {d}")

    ids: set[str] = set()
    bare_ids: set[str] = set()
    page_ids: set[str] = set()
    # Pages that explain a Tag open from that Tag, so they need no Unit.
    explaining_page_ids: set[str] = set()
    for it in pack["items"]:
        key = (it["kind"], it["id"])
        where = f"{pack['id']}:{it['kind']}:{it['id']}"
        if key in ids:
            errors.append(f"duplicate item {where}")
        ids.add(key)
        bare_ids.add(it["id"])
        kind = it["kind"]
        if kind == "misc":
            page_ids.add(it["id"])
            extras = it.get("extras", {})
            if extras.get("explains"):
                explaining_page_ids.add(it["id"])
            if not it.get("title") or not it.get("body_md"):
                errors.append(f"{where}: page needs title and body_md")
            if not extras.get("unlocks") and not extras.get("explains"):
                errors.append(
                    f"{where}: page neither unlocks a concept nor explains a tag, so nothing will show it"
                )
            continue
        if not it.get("primary_form") or not it.get("gloss"):
            errors.append(f"{where}: needs primary_form and gloss")
        ex = it.get("extras", {})
        if kind == "verb":
            conj = it.get("conjugations") or {}
            for t in tenses:
                forms = conj.get(t)
                if not forms or any(not forms.get(p) for p in PERSONS):
                    errors.append(f"{where}: missing forms for {t}")
        if kind == "adjective":
            want = [f["key"] for f in profile["adjectiveForms"]]
            if sorted(ex.get("forms", {})) != sorted(want):
                errors.append(f"{where}: adjective forms must be {want}")
        if kind == "noun" and not ex.get("article"):
            errors.append(f"{where}: noun needs an article")
        if kind in ("connective", "conjunction"):
            if ex.get("role") not in roles:
                errors.append(f"{where}: unknown role {ex.get('role')}")
            n = word_span_count(ex.get("example", ""), it["primary_form"])
            if n != 1:
                errors.append(f"{where}: example must contain the word once (found {n})")

    unit_page_ids: set[str] = set()
    seen_word_ids: set[str] = set()
    seen_titles: set[str] = set()
    for i, u in enumerate(pack.get("units", [])):
        label = f"{pack['id']} unit {i} ('{u['title']}')"
        if u["title"].casefold() in seen_titles:
            errors.append(f"{label}: another Unit in the pack has this title")
        seen_titles.add(u["title"].casefold())
        if "subtitle" in u and not (isinstance(u["subtitle"], str) and u["subtitle"].strip()):
            errors.append(f"{label}: subtitle must be a non-empty string")
        n = len(u["word_ids"])
        if not (6 <= n <= 10):
            errors.append(f"{label}: has {n} word_ids, must be 6-10")
        for w in u["word_ids"]:
            if w not in bare_ids:
                errors.append(f"{label}: word_id '{w}' not found in pack items")
            elif w in page_ids:
                errors.append(f"{label}: word_id '{w}' is a Page item, not a Word")
            elif w in seen_word_ids:
                errors.append(f"{label}: word_id '{w}' already belongs to another unit")
            seen_word_ids.add(w)
        page_id = u.get("page_id")
        if page_id is not None:
            unit_page_ids.add(page_id)
            if page_id not in bare_ids:
                errors.append(f"{label}: page_id '{page_id}' not found in pack items")
            elif page_id not in page_ids:
                errors.append(f"{label}: page_id '{page_id}' is not a Page item")

    if pack.get("units"):
        # Only a pack that ships a Course (units) makes this promise; a pack
        # with no units at all (fr-core-v1, nl-core-v1) has no Course to omit
        # a grammar page from.
        for pid in sorted(page_ids - unit_page_ids - explaining_page_ids):
            errors.append(f"{pack['id']}: page '{pid}' is not the page of any unit")

    return errors


def check_no_silent_removals(pack: dict, previous: dict | None, retired: set[str]) -> list[str]:
    """`previous` is the pack JSON last committed under packs/<lang>/;
    an id present there and absent from `pack` must be listed in `retired`."""
    if previous is None:
        return []
    prev_ids = {it["id"] for it in previous.get("items", [])}
    curr_ids = {it["id"] for it in pack.get("items", [])}
    missing = sorted(prev_ids - curr_ids - retired)
    return [
        f"{pack['id']}: item '{i}' present in the committed pack is gone and not listed in 'retired'"
        for i in missing
    ]


EXAMPLES_BLOCK = re.compile(r"^:::examples[ \t]*\n(.*?)^:::[ \t]*$", re.MULTILINE | re.DOTALL)
# "- <target-language sentence> — <English gloss>", the format ExamplesWidget bolds.
GLOSSED_LINE = re.compile(r"^\s*[-*]\s+\S.*?\s—\s+\S")


def glossed_example_counts(body: str) -> list[int]:
    """How many glossed lines each :::examples block in `body` holds."""
    return [
        sum(1 for line in block.splitlines() if GLOSSED_LINE.match(line))
        for block in EXAMPLES_BLOCK.findall(body)
    ]


def check_tag_pages(code: str, packs: list[dict], profile: dict) -> list[str]:
    """AC15: every profile concept, and every concept used as a tag on a Base Pack
    page, is in the `explains` of exactly one page across the language's Base
    Packs; every `explains` entry is a known concept; every page explaining a
    profile concept has an :::examples block of at least three glossed lines.

    A known concept is a profile concept or one a pack's profile delta adds.
    """
    profile_concepts = [c["id"] for c in profile["concepts"]]
    known = set(profile_concepts)
    for p in packs:
        known |= {c["id"] for c in p.get("profile_delta", [])}

    pages = [it for p in packs for it in p["items"] if it["kind"] == "misc"]
    errors: list[str] = []
    explained_by: dict[str, list[str]] = {}
    for it in pages:
        for concept in it.get("extras", {}).get("explains", []):
            if concept not in known:
                errors.append(f"{code}: page {it['id']} explains '{concept}', which is no known concept")
            explained_by.setdefault(concept, []).append(it["id"])

    tagged = sorted({t for it in pages for t in it.get("tags", []) if t in known} - set(profile_concepts))
    for concept in profile_concepts + tagged:
        by = explained_by.get(concept, [])
        if not by:
            errors.append(f"{code}: no page explains '{concept}'")
        elif len(by) > 1:
            errors.append(f"{code}: '{concept}' is explained by {len(by)} pages: {', '.join(by)}")

    bodies = {it["id"]: it.get("body_md", "") for it in pages}
    for pid in sorted({pid for c in profile_concepts for pid in explained_by.get(c, [])}):
        if max(glossed_example_counts(bodies[pid]), default=0) < 3:
            errors.append(
                f"{code}: page {pid} explains a profile concept but has no :::examples block of 3 glossed lines"
            )
    return errors


EXAMPLE_DIR = HERE / "examples"


def apply_examples(pack: dict, examples: dict[str, dict]) -> list[str]:
    """Give each Word its example sentence from `examples`, in place.

    `examples` maps a Word's id, or "kind:id" where two Words in the pack
    share an id, to {"example", "example_en"}, or to {"example_en"} alone
    for a sentence the source already has. An example written in the pack's
    own source wins. A key that matches no Word, or a bare id two
    Words share, is an error, so a renamed Word can't silently lose its
    sentence.
    """
    errors: list[str] = []
    words = [it for it in pack["items"] if it["kind"] != "misc"]
    by_id: dict[str, list[dict]] = {}
    for it in words:
        by_id.setdefault(it["id"], []).append(it)
    for key, ex in examples.items():
        kind, _, wid = key.rpartition(":")
        hits = [it for it in by_id.get(wid, []) if not kind or it["kind"] == kind]
        if not hits:
            errors.append(f"{pack['id']}: example for '{key}' matches no Word")
            continue
        if len(hits) > 1:
            errors.append(f"{pack['id']}: example for '{key}' fits {len(hits)} Words; key it as kind:id")
            continue
        extras = hits[0].setdefault("extras", {})
        if not extras.get("example") and ex.get("example"):
            extras["example"] = ex["example"]
            extras["example_en"] = ex["example_en"]
        elif extras.get("example") and not extras.get("example_en"):
            # An entry with only "example_en" translates the source's own sentence.
            extras["example_en"] = ex["example_en"]
    return errors


def examples_for(pack_id: str) -> dict[str, dict]:
    path = EXAMPLE_DIR / f"{pack_id}.json"
    return json.loads(path.read_text()) if path.exists() else {}


UNIT_NAME_DIR = HERE / "units"


def apply_unit_names(pack: dict, names: dict[str, dict]) -> list[str]:
    """Give each Unit its title and subtitle from `names`, in place.

    `names` maps a Unit's first word_id to {"title", "subtitle"}: the title
    in the pack's language, the subtitle in English saying what the words
    cover. Keying by the first word keeps the grouping, and so a learner's
    progress, untouched. A key that starts no Unit is an error, and so is a
    Unit left without a name once the pack has a names file.
    """
    if not names:
        return []
    errors: list[str] = []
    units = {u["word_ids"][0]: u for u in pack.get("units", [])}
    for key, name in names.items():
        unit = units.get(key)
        if unit is None:
            errors.append(f"{pack['id']}: unit name for '{key}' starts no Unit")
            continue
        unit["title"] = name["title"]
        unit["subtitle"] = name["subtitle"]
    for key, unit in units.items():
        if key not in names:
            errors.append(f"{pack['id']}: Unit '{unit['title']}' ({key}) has no name")
    return errors


def unit_names_for(pack_id: str) -> dict[str, dict]:
    path = UNIT_NAME_DIR / f"{pack_id}.json"
    return json.loads(path.read_text()) if path.exists() else {}


def profile_for(code: str) -> dict:
    return json.loads((LANGUAGE_DIR / code / "profile.json").read_text())


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build every language's Base Packs.")
    parser.add_argument("--check", action="store_true", help="validate only, write nothing")
    parser.add_argument(
        "--lang",
        action="append",
        choices=LANGUAGES,
        help="build only this language (repeatable); the catalog, which lists every language, is not written",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT,
        help="the folder whose packs/ the previous build is read from, and where packs/ and catalog.json are written",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    import importlib

    import catalog

    args = parse_args(sys.argv[1:] if argv is None else argv)
    check_only = args.check
    out: Path = args.out
    codes = [c for c in LANGUAGES if not args.lang or c in args.lang]
    failed = False
    built: list[dict] = []
    for code in codes:
        module = importlib.import_module(code)
        profile = profile_for(code)
        pack_dir = out / "packs" / code
        seen: set[str] = set()
        # Concepts the core pack's delta introduced are on the stored profile
        # too. A new language has no core pack on disk until its first build.
        core_path = pack_dir / f"{code}-core-v1.json"
        if core_path.exists():
            core = json.loads(core_path.read_text())
            seen |= {c["id"] for c in core.get("profile_delta", [])}
        to_write: list[tuple[Path, dict]] = []
        for pack in module.PACKS:
            retired = set(pack.pop("_retired", []) or [])
            out_path = pack_dir / f"{pack['id']}.json"
            previous = json.loads(out_path.read_text()) if out_path.exists() else None

            errs = apply_examples(pack, examples_for(pack["id"]))
            errs += apply_unit_names(pack, unit_names_for(pack["id"]))
            errs += validate(pack, profile, seen)
            errs += check_no_silent_removals(pack, previous, retired)
            errs += check_gap_answers(pack)
            seen |= {c["id"] for c in pack.get("profile_delta", [])}
            kinds: dict[str, int] = {}
            for it in pack["items"]:
                kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
            summary = ", ".join(f"{v} {k}" for k, v in sorted(kinds.items()))
            print(f"{pack['id']} v{pack['version']}: {len(pack['items'])} items ({summary})")
            for e in errs:
                print(f"  ERROR {e}")
            failed |= bool(errs)
            built.append(pack)
            if not errs:
                to_write.append((out_path, pack))

        tag_errs = check_tag_pages(code, module.PACKS, profile)
        print(f"{code} tag pages: {'ok' if not tag_errs else f'{len(tag_errs)} errors'}")
        for e in tag_errs:
            print(f"  ERROR {e}")
        failed |= bool(tag_errs)
        # A Tag that opens no page, or two, is a language-wide fault, so none
        # of that language's packs are written until it's fixed.
        if not check_only and not tag_errs:
            pack_dir.mkdir(parents=True, exist_ok=True)
            for out_path, pack in to_write:
                write_json(out_path, pack)
    # A failed pack keeps its previous file, so a catalog of the new versions
    # would promise apps versions that aren't there.
    if not check_only and not failed and not args.lang:
        write_json(out / "catalog.json", catalog.build_catalog(out, built))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
