"""catalog.json: the index an app reads to find, install and update packs.

The catalog lists every pack in curriculum order. Each entry carries the
pack's version, so an app compares it with the version it has installed and
downloads the pack only when the number went up. sha256 and size let the app
verify the download before it touches its database.

    {
      "format": 1,
      "name": "MaxLango",
      "packs": [
        {"id": "nl-core-v1", "language": "nl", "name": "...", "version": 7,
         "url": "packs/nl/nl-core-v1.json", "sha256": "...", "size": 26034,
         "items": 120, "requires": 1, "author": "...", "license": "CC-BY-SA-4.0"}
      ]
    }

`url` is relative to the catalog's own URL, so a mirror of this folder works
anywhere. `format` versions the catalog's own shape and `requires` the pack
format an app has to understand: an app skips a pack whose `requires` is
newer than it knows.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

CATALOG_FORMAT = 1
# The pack format these packs are written in. Bump it, for every pack that
# uses the new shape, when a change would break an app that doesn't know it.
PACK_FORMAT = 1
CATALOG_NAME = "MaxLango"


def pack_path(code: str, pack_id: str) -> str:
    """Where a pack lives, relative to the repository root."""
    return f"packs/{code}/{pack_id}.json"


def entry_for(root: Path, pack: dict) -> dict:
    """The catalog entry for `pack`, read from its file under `root`."""
    rel = pack_path(pack["language"], pack["id"])
    raw = (root / rel).read_bytes()
    entry = {
        "id": pack["id"],
        "language": pack["language"],
        "name": pack["name"],
        "version": pack["version"],
        "url": rel,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size": len(raw),
        "items": len(pack["items"]),
        "requires": PACK_FORMAT,
    }
    for key in ("author", "license"):
        if pack.get(key):
            entry[key] = pack[key]
    return entry


def build_catalog(root: Path, packs: list[dict]) -> dict:
    """The catalog for `packs`, in the order given, from their files under `root`."""
    return {
        "format": CATALOG_FORMAT,
        "name": CATALOG_NAME,
        "packs": [entry_for(root, p) for p in packs],
    }
