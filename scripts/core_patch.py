"""Upgrade the hand-written core packs: every core verb gets forms for every
tense in the profile, so the conjugation ladder runs without a model, and a
core page can be added or rewritten here instead of by hand in the JSON."""

from __future__ import annotations

import json
from pathlib import Path

from common import SCHEMA_URL

PACK_DIR = Path(__file__).resolve().parents[1] / "packs"


def patch_core(
    code: str,
    version: int,
    verbs: dict[str, tuple[dict, dict]],
    fixes=None,
    pages: list[dict] | None = None,
) -> dict:
    """`verbs` maps a core verb id to (conjugations, extra extras).

    `pages` are upserted by (kind, id), so rebuilding never duplicates them.
    The core pack is read from the JSON this build writes, so a page added
    here is already in it on the next run. A page with the same kind and id
    replaces the old one where it stands; any other page goes on the end.
    """
    pack = json.loads((PACK_DIR / code / f"{code}-core-v1.json").read_text())
    pack["$schema"] = SCHEMA_URL
    pack["version"] = max(pack["version"], version)
    for it in pack["items"]:
        if it["kind"] == "verb" and it["id"] in verbs:
            conj, extras = verbs[it["id"]]
            it["conjugations"] = conj
            it["extras"] = {**it.get("extras", {}), **extras}
        if fixes and (it["kind"], it["id"]) in fixes:
            fixes[(it["kind"], it["id"])](it)
    index = {(it["kind"], it["id"]): i for i, it in enumerate(pack["items"])}
    for p in pages or []:
        key = (p["kind"], p["id"])
        if key in index:
            pack["items"][index[key]] = p
        else:
            index[key] = len(pack["items"])
            pack["items"].append(p)
    return pack
