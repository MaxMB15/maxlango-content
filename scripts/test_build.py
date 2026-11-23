#!/usr/bin/env python3
"""Tests for scripts/content/build.py.

Stdlib unittest, not pytest: this repo has no pyproject.toml/pytest.ini for
its app-side Python, so a pytest-only suite would never run anywhere. Invoke
directly:

    python3 scripts/content/test_build.py
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import core_patch  # noqa: E402
from check_versions import version_errors  # noqa: E402
from gap_answers import check_gap_answers  # noqa: E402
from build import (  # noqa: E402
    EXAMPLE_DIR,
    ROOT,
    UNIT_NAME_DIR,
    apply_examples,
    apply_unit_names,
    check_no_silent_removals,
    check_tag_pages,
    profile_for,
    validate,
)
from common import page, topic  # noqa: E402

CURRICULUM_ORDER = [
    "fr-core-v1",
    "fr-foundations-v1",
    "fr-everyday-v1",
    "fr-fluency-v1",
    "nl-core-v1",
    "nl-foundations-v1",
    "nl-everyday-v1",
    "nl-fluency-v1",
]


class CheckNoSilentRemovalsTests(unittest.TestCase):
    """AC32: the content builder fails if a published Item id disappears
    without being retired."""

    def test_fails_when_a_published_id_disappears_without_being_retired(self):
        previous = {"id": "fr-core-v1", "items": [{"id": "chien"}, {"id": "chat"}]}
        current = {"id": "fr-core-v1", "items": [{"id": "chien"}]}

        errors = check_no_silent_removals(current, previous, retired=set())

        self.assertEqual(len(errors), 1)
        self.assertIn("chat", errors[0])
        self.assertIn("retired", errors[0])

    def test_passes_when_the_missing_id_is_listed_as_retired(self):
        previous = {"id": "fr-core-v1", "items": [{"id": "chien"}, {"id": "chat"}]}
        current = {"id": "fr-core-v1", "items": [{"id": "chien"}]}

        errors = check_no_silent_removals(current, previous, retired={"chat"})

        self.assertEqual(errors, [])

    def test_no_previous_pack_is_always_clean(self):
        # A brand-new pack (never built before) has nothing to compare against.
        current = {"id": "fr-new-v1", "items": [{"id": "chien"}]}
        self.assertEqual(check_no_silent_removals(current, None, retired=set()), [])

    def test_unrelated_new_items_do_not_trigger_a_false_positive(self):
        previous = {"id": "fr-core-v1", "items": [{"id": "chien"}]}
        current = {"id": "fr-core-v1", "items": [{"id": "chien"}, {"id": "maison"}]}
        self.assertEqual(check_no_silent_removals(current, previous, retired=set()), [])


class PageTests(unittest.TestCase):
    """A page can explain Tags as well as, or instead of, unlocking a concept."""

    def test_a_page_given_no_explains_writes_none(self):
        p = page("xx-p", "P", "body", ["t"], "xx-p")

        self.assertEqual(p["extras"], {"unlocks": ["concept:xx-p"]})

    def test_explains_lands_in_extras_next_to_unlocks(self):
        p = page("xx-p", "P", "body", ["t"], "xx-p", explains=["t", "u"])

        self.assertEqual(p["extras"], {"unlocks": ["concept:xx-p"], "explains": ["t", "u"]})

    def test_a_page_can_explain_without_unlocking(self):
        p = page("xx-p", "P", "body", ["t"], explains=["t"])

        self.assertEqual(p["extras"], {"explains": ["t"]})


class PatchCorePagesTests(unittest.TestCase):
    """patch_core upserts pages into the committed core pack, which is also
    where it reads the pack from, so a rebuild must never add a page twice."""

    def setUp(self):
        tmp = Path(tempfile.mkdtemp(prefix="lango-core-patch-test-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        (tmp / "xx").mkdir()
        self.core = tmp / "xx" / "xx-core-v1.json"
        self.core.write_text(
            json.dumps(
                {
                    "id": "xx-core-v1",
                    "version": 1,
                    "language": "xx",
                    "name": "Core",
                    "items": [
                        {"kind": "misc", "id": "xx-old", "title": "Old", "body_md": "old", "tags": []},
                        {"kind": "noun", "id": "kat", "primary_form": "kat", "gloss": "cat", "tags": []},
                    ],
                }
            )
        )
        patcher = mock.patch.object(core_patch, "PACK_DIR", tmp)
        patcher.start()
        self.addCleanup(patcher.stop)

    @staticmethod
    def keys(pack: dict) -> list[tuple[str, str]]:
        return [(it["kind"], it["id"]) for it in pack["items"]]

    def test_a_page_with_the_same_kind_and_id_replaces_the_old_one_in_place(self):
        new = page("xx-old", "New", "new", ["t"], explains=["t"])

        out = core_patch.patch_core("xx", 1, {}, pages=[new])

        self.assertEqual(self.keys(out), [("misc", "xx-old"), ("noun", "kat")])
        self.assertEqual(out["items"][0], new)

    def test_a_new_page_is_appended(self):
        new = page("xx-new", "New", "new", ["t"], explains=["t"])

        out = core_patch.patch_core("xx", 1, {}, pages=[new])

        self.assertEqual(self.keys(out), [("misc", "xx-old"), ("noun", "kat"), ("misc", "xx-new")])

    def test_patching_its_own_output_again_changes_nothing(self):
        pages = [
            page("xx-old", "Old, rewritten", "old", ["t"], explains=["t"]),
            page("xx-new", "New", "new", ["u"], explains=["u"]),
        ]
        first = core_patch.patch_core("xx", 1, {}, pages=pages)
        self.core.write_text(json.dumps(first))

        second = core_patch.patch_core("xx", 1, {}, pages=pages)

        self.assertEqual(second, first)
        self.assertEqual(self.keys(second), [("misc", "xx-old"), ("noun", "kat"), ("misc", "xx-new")])


PROFILE = {"concepts": [{"id": "lidwoorden", "kind": "topic"}], "adjectiveForms": []}


def noun(id: str) -> dict:
    return {"kind": "noun", "id": id, "primary_form": id, "gloss": id, "extras": {"article": "de"}, "tags": []}


class ValidatePagesTests(unittest.TestCase):
    """A page reaches the learner through a session (unlocks) or through a Tag
    (explains); validate() rejects one that does neither."""

    def test_accepts_a_page_that_only_explains(self):
        pack = {"id": "xx-core-v1", "items": [page("xx-p", "P", "body", ["lidwoorden"], explains=["lidwoorden"])]}

        self.assertEqual(validate(pack, PROFILE, set()), [])

    def test_rejects_a_page_that_neither_unlocks_nor_explains(self):
        pack = {"id": "xx-core-v1", "items": [page("xx-p", "P", "body", ["lidwoorden"])]}

        errors = validate(pack, PROFILE, set())

        self.assertEqual(len(errors), 1)
        self.assertIn("xx-core-v1:misc:xx-p", errors[0])

    def course(self, p: dict) -> dict:
        words = [noun(f"w{i}") for i in range(6)]
        return {
            "id": "xx-foundations-v1",
            "items": [p] + words,
            "units": [{"title": "Words", "word_ids": [w["id"] for w in words]}],
        }

    def test_an_explaining_page_need_not_be_the_page_of_a_unit(self):
        pack = self.course(page("xx-p", "P", "body", ["lidwoorden"], explains=["lidwoorden"]))

        self.assertEqual(validate(pack, PROFILE, set()), [])

    def test_an_unlocking_page_must_still_be_the_page_of_a_unit(self):
        pack = self.course(page("xx-p", "P", "body", ["lidwoorden"], "xx-p"))

        errors = validate(pack, PROFILE, set())

        self.assertEqual(errors, ["xx-foundations-v1: page 'xx-p' is not the page of any unit"])


TAG_PROFILE = {
    "concepts": [{"id": "de", "kind": "noun-class"}, {"id": "het", "kind": "noun-class"}],
    "adjectiveForms": [],
}
THREE_EXAMPLES = """
:::examples
- De kat slaapt. — The cat is sleeping.
- Het huis is groot. — The house is big.
- De man leest. — The man is reading.
:::
"""


def explaining(id: str, explains: list[str], body: str = THREE_EXAMPLES, tags: list[str] | None = None) -> dict:
    return page(id, id, body, tags if tags is not None else list(explains), explains=explains)


def base_pack(id: str, *pages: dict, delta: list[dict] | None = None) -> dict:
    pack = {"id": id, "items": list(pages)}
    if delta:
        pack["profile_delta"] = delta
    return pack


class CheckTagPagesTests(unittest.TestCase):
    """AC15: every concept a learner can tap opens exactly one Base Pack page,
    and the page for a profile concept shows at least three glossed examples."""

    def test_passes_when_each_concept_has_one_explaining_page(self):
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"]))]

        self.assertEqual(check_tag_pages("xx", packs, TAG_PROFILE), [])

    def test_a_profile_concept_no_page_explains_fails(self):
        packs = [base_pack("xx-core-v1", explaining("xx-de", ["de"]))]

        errors = check_tag_pages("xx", packs, TAG_PROFILE)

        self.assertEqual(errors, ["xx: no page explains 'het'"])

    def test_a_concept_two_pages_explain_fails(self):
        packs = [
            base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"])),
            base_pack("xx-foundations-v1", explaining("xx-het", ["het"])),
        ]

        errors = check_tag_pages("xx", packs, TAG_PROFILE)

        self.assertEqual(errors, ["xx: 'het' is explained by 2 pages: xx-de-het, xx-het"])

    def test_an_explains_entry_that_is_no_known_concept_fails(self):
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het", "lidwoord"]))]

        errors = check_tag_pages("xx", packs, TAG_PROFILE)

        self.assertEqual(errors, ["xx: page xx-de-het explains 'lidwoord', which is no known concept"])

    def test_a_concept_tagged_on_a_page_needs_a_page_that_explains_it(self):
        delta = [topic("verkleinwoorden", "Verkleinwoorden", "diminutives", ["het"])]
        diminutives = page("xx-diminutives", "Diminutives", "body", ["verkleinwoorden", "het"], "xx-diminutives")
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"]), diminutives, delta=delta)]

        errors = check_tag_pages("xx", packs, TAG_PROFILE)

        self.assertEqual(errors, ["xx: no page explains 'verkleinwoorden'"])

    def test_a_delta_concept_page_needs_no_examples(self):
        delta = [topic("verkleinwoorden", "Verkleinwoorden", "diminutives", ["het"])]
        diminutives = explaining("xx-diminutives", ["verkleinwoorden"], body="body", tags=["verkleinwoorden", "het"])
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"]), diminutives, delta=delta)]

        self.assertEqual(check_tag_pages("xx", packs, TAG_PROFILE), [])

    def test_a_tag_that_is_no_concept_needs_no_page(self):
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"], tags=["de", "het", "wiki"]))]

        self.assertEqual(check_tag_pages("xx", packs, TAG_PROFILE), [])

    def test_a_profile_concept_page_with_two_glossed_examples_fails_once(self):
        two = ":::examples\n- De kat slaapt. — The cat is sleeping.\n- Het huis is groot. — The house is big.\n:::"
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"], body=two))]

        errors = check_tag_pages("xx", packs, TAG_PROFILE)

        self.assertEqual(
            errors,
            ["xx: page xx-de-het explains a profile concept but has no :::examples block of 3 glossed lines"],
        )

    def test_an_example_without_an_english_gloss_does_not_count(self):
        body = ":::examples\n- De kat slaapt. — The cat is sleeping.\n- Het huis is groot. — The house is big.\n- De man leest.\n:::"
        packs = [base_pack("xx-core-v1", explaining("xx-de-het", ["de", "het"], body=body))]

        self.assertEqual(len(check_tag_pages("xx", packs, TAG_PROFILE)), 1)

    def test_the_bundled_base_packs_pass(self):
        import fr
        import nl

        for code, module in (("fr", fr), ("nl", nl)):
            profile = profile_for(code)
            with self.subTest(language=code):
                self.assertEqual(check_tag_pages(code, module.PACKS, profile), [])


class BuildOutputTests(unittest.TestCase):
    """The build writes catalog.json, the index an app reads to install and
    update packs, next to the packs it lists."""

    def setUp(self):
        tmp = Path(tempfile.mkdtemp(prefix="lango-build-test-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        # A copy of the committed packs: the build reads the previous version
        # of each pack from its output directory.
        self.out = tmp
        shutil.copytree(ROOT / "packs", self.out / "packs")

    def run_build(self, hash_seed: str, *argv: str) -> None:
        # A separate process per run, each with its own string hash seed, so
        # set iteration order can't hide behind one interpreter's choice.
        env = {**os.environ, "PYTHONHASHSEED": hash_seed}
        result = subprocess.run(
            [sys.executable, str(HERE / "build.py"), *argv, "--out", str(self.out)],
            env=env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def written(self) -> dict[str, bytes]:
        return {str(p.relative_to(self.out)): p.read_bytes() for p in sorted(self.out.rglob("*.json"))}

    def test_the_catalog_lists_every_pack_in_curriculum_order(self):
        self.run_build("1")

        catalog = json.loads((self.out / "catalog.json").read_text())

        self.assertEqual(catalog["format"], 1)
        self.assertEqual([entry["id"] for entry in catalog["packs"]], CURRICULUM_ORDER)
        for entry in catalog["packs"]:
            raw = (self.out / entry["url"]).read_bytes()
            pack = json.loads(raw)
            self.assertEqual(entry["url"], f"packs/{pack['language']}/{pack['id']}.json")
            self.assertEqual(
                (entry["id"], entry["language"], entry["name"], entry["version"], entry["items"]),
                (pack["id"], pack["language"], pack["name"], pack["version"], len(pack["items"])),
            )
            self.assertEqual(entry["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(entry["size"], len(raw))
            self.assertEqual(entry["requires"], 1)
            # Every official pack has card text; the levelled ones say their level.
            self.assertTrue(entry["description"])
            self.assertLessEqual(len(entry["description"]), 240)
            if pack["name"].endswith(")"):
                self.assertEqual(entry["level"], pack["name"][-3:-1])
            else:
                self.assertNotIn("level", entry)

    def test_the_committed_catalog_is_up_to_date(self):
        self.run_build("1")

        self.assertEqual((self.out / "catalog.json").read_bytes(), (ROOT / "catalog.json").read_bytes())

    def test_a_second_build_leaves_every_file_byte_identical(self):
        self.run_build("1")
        first = self.written()
        self.run_build("2")

        expected = [f"packs/{i[:2]}/{i}.json" for i in CURRICULUM_ORDER] + ["catalog.json"]
        self.assertEqual(sorted(first), sorted(expected))
        self.assertEqual(self.written(), first)

    def test_check_writes_nothing(self):
        before = self.written()
        self.run_build("1", "--check")

        self.assertEqual(self.written(), before)


class VersionGuardTests(unittest.TestCase):
    """Apps update a pack only when its catalog version goes up, so a pack
    that changed under the same version would never reach them."""

    @staticmethod
    def catalog(*packs: tuple[str, int, str]) -> dict:
        return {"format": 1, "packs": [{"id": i, "version": v, "sha256": h} for i, v, h in packs]}

    def test_a_changed_pack_with_a_higher_version_passes(self):
        base = self.catalog(("xx-core-v1", 1, "aaa"))
        head = self.catalog(("xx-core-v1", 2, "bbb"), ("xx-new-v1", 1, "ccc"))

        self.assertEqual(version_errors(base, head), [])

    def test_a_changed_pack_under_the_same_version_fails(self):
        base = self.catalog(("xx-core-v1", 3, "aaa"))
        head = self.catalog(("xx-core-v1", 3, "bbb"))

        self.assertEqual(version_errors(base, head), ["xx-core-v1: changed but is still version 3; bump its version"])

    def test_a_version_that_goes_down_fails(self):
        base = self.catalog(("xx-core-v1", 3, "aaa"))
        head = self.catalog(("xx-core-v1", 2, "bbb"))

        self.assertEqual(version_errors(base, head), ["xx-core-v1: version went down from 3 to 2"])

    def test_a_pack_that_leaves_the_catalog_fails(self):
        base = self.catalog(("xx-core-v1", 1, "aaa"))

        self.assertEqual(version_errors(base, self.catalog()), ["xx-core-v1: left the catalog"])


class ApplyExamplesTests(unittest.TestCase):
    def pack(self, *items):
        return {"id": "nl-test-v1", "items": list(items)}

    def word(self, kind, id, **extras):
        it = {"kind": kind, "id": id, "primary_form": id, "gloss": id}
        if extras:
            it["extras"] = extras
        return it

    def test_fills_a_word_without_an_example(self):
        pack = self.pack(self.word("noun", "fiets", article="de"))
        errs = apply_examples(pack, {"fiets": {"example": "Mijn fiets is rood.", "example_en": "My bike is red."}})
        self.assertEqual(errs, [])
        self.assertEqual(
            pack["items"][0]["extras"],
            {"article": "de", "example": "Mijn fiets is rood.", "example_en": "My bike is red."},
        )

    def test_the_sources_own_example_wins(self):
        pack = self.pack(self.word("noun", "fiets", example="Ik fiets.", example_en="I cycle."))
        apply_examples(pack, {"fiets": {"example": "Mijn fiets is rood.", "example_en": "My bike is red."}})
        self.assertEqual(pack["items"][0]["extras"]["example"], "Ik fiets.")

    def test_an_english_only_entry_translates_the_sources_sentence(self):
        pack = self.pack(self.word("conjunction", "maar", example="Ik wil, maar ik kan niet."))
        apply_examples(pack, {"maar": {"example_en": "I want to, but I can't."}})
        self.assertEqual(pack["items"][0]["extras"]["example"], "Ik wil, maar ik kan niet.")
        self.assertEqual(pack["items"][0]["extras"]["example_en"], "I want to, but I can't.")

    def test_kind_id_picks_one_of_two_words_sharing_an_id(self):
        pack = self.pack(self.word("phrase", "dag"), self.word("noun", "dag"))
        ex = {"example": "Het was een lange dag.", "example_en": "It was a long day."}
        self.assertEqual(apply_examples(pack, {"noun:dag": ex}), [])
        self.assertNotIn("extras", pack["items"][0])
        self.assertEqual(pack["items"][1]["extras"]["example"], "Het was een lange dag.")

    def test_a_bare_id_two_words_share_is_an_error(self):
        pack = self.pack(self.word("phrase", "dag"), self.word("noun", "dag"))
        errs = apply_examples(pack, {"dag": {"example": "Dag!", "example_en": "Bye!"}})
        self.assertEqual(len(errs), 1)
        self.assertIn("kind:id", errs[0])

    def test_a_key_that_matches_no_word_is_an_error(self):
        errs = apply_examples(self.pack(self.word("noun", "fiets")), {"auto": {"example": "x", "example_en": "y"}})
        self.assertEqual(errs, ["nl-test-v1: example for 'auto' matches no Word"])

    def test_every_shipped_example_file_names_a_built_pack(self):
        for path in sorted(EXAMPLE_DIR.glob("*.json")):
            code = path.stem.split("-")[0]
            self.assertTrue((ROOT / "packs" / code / path.name).exists(), path.name)



class ApplyUnitNamesTests(unittest.TestCase):
    def pack(self):
        return {
            "id": "nl-test-v1",
            "units": [
                {"title": "Oefening", "word_ids": ["hoi", "dag"], "page_id": "nl-pronouns"},
                {"title": "Oefening", "word_ids": ["rood", "blauw"]},
            ],
        }

    def test_renames_every_unit_and_keeps_its_words(self):
        pack = self.pack()
        errs = apply_unit_names(
            pack,
            {
                "hoi": {"title": "Hoi en doei", "subtitle": "Hi and bye"},
                "rood": {"title": "Kleuren", "subtitle": "Red and blue"},
            },
        )
        self.assertEqual(errs, [])
        self.assertEqual(
            pack["units"][0],
            {"title": "Hoi en doei", "subtitle": "Hi and bye", "word_ids": ["hoi", "dag"], "page_id": "nl-pronouns"},
        )
        self.assertEqual(pack["units"][1]["word_ids"], ["rood", "blauw"])

    def test_no_names_file_leaves_the_units_alone(self):
        pack = self.pack()
        self.assertEqual(apply_unit_names(pack, {}), [])
        self.assertNotIn("subtitle", pack["units"][0])

    def test_a_key_that_starts_no_unit_is_an_error(self):
        errs = apply_unit_names(self.pack(), {
            "hoi": {"title": "A", "subtitle": "a"},
            "rood": {"title": "B", "subtitle": "b"},
            "dag": {"title": "C", "subtitle": "c"},
        })
        self.assertEqual(errs, ["nl-test-v1: unit name for 'dag' starts no Unit"])

    def test_a_unit_left_without_a_name_is_an_error(self):
        errs = apply_unit_names(self.pack(), {"hoi": {"title": "A", "subtitle": "a"}})
        self.assertEqual(errs, ["nl-test-v1: Unit 'Oefening' (rood) has no name"])

    def test_every_shipped_names_file_names_a_built_pack(self):
        for path in sorted(UNIT_NAME_DIR.glob("*.json")):
            code = path.stem.split("-")[0]
            self.assertTrue((ROOT / "packs" / code / path.name).exists(), path.name)

    def test_every_built_unit_has_a_distinct_title_and_a_subtitle(self):
        for path in sorted(UNIT_NAME_DIR.glob("*.json")):
            code = path.stem.split("-")[0]
            units = json.loads((ROOT / "packs" / code / path.name).read_text())["units"]
            titles = [u["title"].casefold() for u in units]
            self.assertEqual(len(titles), len(set(titles)), path.name)
            self.assertTrue(all(u.get("subtitle") for u in units), path.name)


def gap_page(body: str, **extras) -> dict:
    return {"items": [{"kind": "misc", "id": "xx-page", "title": "P", "body_md": body, "extras": extras}]}


class GapAnswersTests(unittest.TestCase):
    """A page's games must not have their answers printed on the same page."""

    def test_a_gap_whose_filled_words_the_page_prints_fails(self):
        body = 'You want *ik heb het koud*.\n\n:::cloze{sentence="Ik ___ het koud, doe het raam dicht." blank="heb"}\n:::'

        errors = check_gap_answers(gap_page(body))

        self.assertEqual(len(errors), 1)
        self.assertIn("ik heb het koud", errors[0])

    def test_a_gap_the_page_teaches_but_does_not_spell_out_passes(self):
        body = '| wij | hebben |\n\n:::cloze{sentence="Wij ___ haast, de trein vertrekt zo." blank="hebben"}\n:::'

        self.assertEqual(check_gap_answers(gap_page(body)), [])

    def test_a_reading_card_gap_next_to_its_own_example_fails(self):
        page = gap_page("", examples=["De kat slaapt op de bank."], cloze=[{"sentence": "___ kat slaapt.", "blank": "De"}])

        self.assertEqual(len(check_gap_answers(page)), 1)

    def test_a_prediction_the_page_conjugates_fails(self):
        body = 'Verbs in -ger keep an e: *nous mangeons*.\n\n:::predict{prompt="nous (manger)" answer="mangeons"}\n:::'

        self.assertEqual(len(check_gap_answers(gap_page(body))), 1)

    def test_a_parse_sentence_the_page_already_takes_apart_fails(self):
        body = (
            "In *Lisa heeft gisteren een cadeau gekocht*, the gezegde is *heeft gekocht*.\n\n"
            ':::parse{sentence="Lisa heeft gisteren in Delft een cadeau gekocht." en="x"}\nPersoonsvorm: heeft\n:::'
        )

        self.assertEqual(len(check_gap_answers(gap_page(body))), 1)

    def test_a_parse_sentence_that_only_shares_a_few_words_passes(self):
        body = "*Daan fietst naar huis* has no lijdend voorwerp.\n\n" + (
            ':::parse{sentence="Na het werk fietst Daan met zijn zus naar huis." en="x"}\nPersoonsvorm: fietst\n:::'
        )

        self.assertEqual(check_gap_answers(gap_page(body)), [])

    def test_the_bundled_packs_print_no_answers(self):
        for path in sorted((ROOT / "packs").glob("*/*.json")):
            with self.subTest(pack=path.name):
                self.assertEqual(check_gap_answers(json.loads(path.read_text())), [])


if __name__ == "__main__":
    unittest.main()
