"""Item constructors shared by the French and Dutch sources."""

from __future__ import annotations

import re
import unicodedata

PERSONS = ["1s", "2s", "3s", "1p", "2p", "3p"]
SCHEMA_URL = "https://maxmb15.github.io/maxlango-content/schema/pack-v1.json"
AUTHOR = "Max Boksem"
LICENSE = "CC-BY-SA-4.0"


def slug(text: str) -> str:
    """Stable, readable item id from a form: lowercase, no accents, hyphens."""
    s = unicodedata.normalize("NFKD", text.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def pack(
    id: str,
    version: int,
    language: str,
    name: str,
    items: list,
    delta=None,
    units=None,
    retired: list[str] | None = None,
) -> dict:
    out = {
        "$schema": SCHEMA_URL,
        "id": id,
        "version": version,
        "language": language,
        "name": name,
        "author": AUTHOR,
        "license": LICENSE,
    }
    if delta:
        out["profile_delta"] = delta
    # The app resolves a Unit's bare word id to one item, so a bare id must
    # be unique in the pack. The first item keeps it; a later homonym (the
    # noun "dag" after the phrase "dag") becomes "<id>-<kind>".
    claimed: set[str] = set()
    for it in items:
        if it["kind"] != "misc" and it["id"] in claimed:
            it["id"] = f"{it['id']}-{it['kind']}"
        claimed.add(it["id"])
    out["items"] = items
    if units:
        out["units"] = units
    if retired:
        # Build-time bookkeeping only (scripts/content/build.py's
        # check_no_silent_removals): never shipped in the pack JSON, since
        # the app's Pack schema has no `retired` field.
        out["_retired"] = retired
    return out


UNIT_MIN = 6
UNIT_MAX = 10


def topic_labels(delta: list[dict]) -> dict[str, str]:
    """Target-language label per topic id, read off a pack's own DELTA list."""
    return {c["id"]: c["label"] for c in delta if c.get("kind") == "topic"}


def _chunk_balanced(ids: list[str]) -> list[list[str]]:
    """Split `ids` (length >= UNIT_MIN, and never exactly UNIT_MAX + 1 — see
    `build_units`) into groups of UNIT_MIN..UNIT_MAX, sizes differing by at
    most one, in order."""
    n = len(ids)
    if n == 0:
        return []
    if n <= UNIT_MAX:
        return [ids]
    count = -(-n // UNIT_MAX)  # ceil(n / UNIT_MAX)
    size, remainder = divmod(n, count)
    chunks = []
    i = 0
    for k in range(count):
        take = size + (1 if k < remainder else 0)
        chunks.append(ids[i : i + take])
        i += take
    return chunks


def build_units(
    items: list[dict],
    explicit_units: list[dict] | None = None,
    labels: dict[str, str] | None = None,
    leftover_title: str = "Practice",
) -> list[dict]:
    """Course units: authored pairings first, then a mechanical sweep of
    whatever's left.

    `explicit_units` is this pack's own hand-listed `[{"title", "page_id"?,
    "word_ids"}, ...]` — one entry per grammar page, giving the 6-10 words
    that use or illustrate it (titles in the target language), plus any
    topic whose words don't fall out of a plain tag grouping (e.g. colour
    adjectives, which share the "adjectifs" first tag with every other
    adjective). Every id in it is claimed and removed from the automatic
    pass below.

    `labels` maps a remaining item's first tag to a target-language Unit
    title (normally `topic_labels(DELTA)`, plus any of the pack's own
    non-topic domains worth naming, e.g. "food"). Tag groups with a label
    and >= UNIT_MIN words become their own Units, chunked to UNIT_MAX.
    Everything else — unlabeled tags, and labelled groups too small on
    their own — is pooled into trailing `leftover_title` Units with no
    page, the one mechanical fallback this function still does.

    UNIT_MIN..UNIT_MAX (6..10) has one gap a plain "split evenly" can't
    cross: a group of exactly 11 has no partition where every part is
    6..10 (two parts need 12..20). A group that size gives up its last id
    to the leftover pool instead, becoming a clean single unit of 10.
    """
    explicit_units = explicit_units or []
    labels = labels or {}

    bare_ids = {it["id"] for it in items if it["kind"] != "misc"}
    consumed: set[str] = set()
    units: list[dict] = []

    for eu in explicit_units:
        for w in eu["word_ids"]:
            if w not in bare_ids:
                raise ValueError(f"unit '{eu['title']}': word_id '{w}' not found in pack items")
            if w in consumed:
                raise ValueError(f"unit '{eu['title']}': word_id '{w}' already claimed by another unit")
            consumed.add(w)
        unit = {"title": eu["title"], "word_ids": list(eu["word_ids"])}
        if eu.get("page_id"):
            unit["page_id"] = eu["page_id"]
        units.append(unit)

    order: list[str] = []
    members: dict[str, list[str]] = {}
    # A Unit's word_ids are bare pack-JSON ids (no kind segment). Two items
    # can share a bare id under different kinds here (e.g. "si" as both a
    # phrase and a conjunction); pack() later renames the second one to
    # "si-conjunction". Only the first item to claim a bare id joins a Unit;
    # later homonyms are still fully studyable, just not through a Course
    # Unit.
    seen_word_ids: set[str] = set(consumed)

    for it in items:
        if it["kind"] == "misc":
            continue
        tags = it.get("tags") or []
        if not tags or it["id"] in seen_word_ids:
            continue
        seen_word_ids.add(it["id"])
        tag = tags[0]
        if tag not in members:
            members[tag] = []
            order.append(tag)
        members[tag].append(it["id"])

    leftover: list[str] = []
    for tag in order:
        ids = members[tag]
        label = labels.get(tag)
        if label is None:
            leftover.extend(ids)
            continue
        if len(ids) == UNIT_MAX + 1:
            leftover.append(ids.pop())
        if len(ids) < UNIT_MIN:
            leftover.extend(ids)
            continue
        for chunk in _chunk_balanced(ids):
            units.append({"title": label, "word_ids": chunk})

    if leftover:
        if len(leftover) < UNIT_MIN and units and len(units[-1]["word_ids"]) + len(leftover) <= UNIT_MAX:
            # Too few leftover words for a unit of their own: fold them into
            # the last real unit rather than ship an under-sized one.
            units[-1]["word_ids"].extend(leftover)
        else:
            for chunk in _chunk_balanced(leftover):
                units.append({"title": leftover_title, "word_ids": chunk})

    return units


def topic(id: str, label: str, gloss: str, depends_on: list[str]) -> dict:
    return {"id": id, "kind": "topic", "label": label, "labelGloss": gloss, "dependsOn": depends_on}


def page(
    id: str,
    title: str,
    body: str,
    tags: list[str],
    unlocks: str | None = None,
    explains: list[str] | None = None,
) -> dict:
    """An Explainer Page. `unlocks` puts it in the session Reading rotation;
    `explains` lists the Tags it opens for when the learner taps one."""
    extras: dict = {}
    if unlocks:
        extras["unlocks"] = [f"concept:{unlocks}"]
    if explains:
        extras["explains"] = list(explains)
    return {
        "kind": "misc",
        "id": id,
        "title": title,
        "body_md": body.strip("\n"),
        "extras": extras,
        "tags": tags,
    }


def with_example(extras: dict, example: str | None, example_en: str | None) -> dict:
    if example:
        extras["example"] = example
    if example_en:
        extras["example_en"] = example_en
    return extras


def simple(kind: str, form: str, gloss: str, tags: list[str], id: str | None = None, **extras) -> dict:
    """A phrase, adjective without forms, or other simple item."""
    ex = {k: v for k, v in extras.items() if v is not None}
    item = {"kind": kind, "id": id or slug(form), "primary_form": form, "gloss": gloss}
    if ex:
        item["extras"] = ex
    item["tags"] = tags
    return item


def rows(block: str) -> list[list[str]]:
    """Split a pipe table: one item per non-empty line, fields trimmed."""
    out = []
    for line in block.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append([f.strip() for f in line.split("|")])
    return out


def interleave(*groups: list[dict]) -> list[dict]:
    """Merge item groups so each is spread evenly through the result.

    New items reach the learner in pack order, so a pack that listed all its
    phrases, then all its nouns, would spend its first week on phrases alone.
    """
    keyed = []
    for g in groups:
        n = len(g)
        for i, item in enumerate(g):
            keyed.append(((i + 0.5) / n, len(keyed), item))
    return [item for _, _, item in sorted(keyed, key=lambda k: (k[0], k[1]))]
