#!/usr/bin/env python3
"""Validate catalog.json and every pack it lists against schema/.

    pip install jsonschema && python3 scripts/validate_schema.py [ROOT]

Run it on your own catalog folder before you publish it: the app rejects a
pack that breaks these rules, and it checks a few more (a unit's word ids
must name words in the same pack, for one).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
SCHEMA_DIR = HERE.parent / "schema"


def errors_in(validator: Draft202012Validator, value: object, label: str) -> list[str]:
    return [
        f"{label}: {'/'.join(map(str, e.absolute_path)) or '(root)'}: {e.message}"
        for e in sorted(validator.iter_errors(value), key=lambda e: list(map(str, e.absolute_path)))
    ]


def main(argv: list[str]) -> int:
    root = Path(argv[0]) if argv else HERE.parent
    catalog_schema = json.loads((SCHEMA_DIR / "catalog-v1.json").read_text())
    pack_schema = json.loads((SCHEMA_DIR / "pack-v1.json").read_text())
    catalog_v = Draft202012Validator(catalog_schema)
    pack_v = Draft202012Validator(pack_schema)

    catalog = json.loads((root / "catalog.json").read_text())
    errors = errors_in(catalog_v, catalog, "catalog.json")
    for entry in catalog.get("packs", []):
        path = root / entry["url"]
        pack = json.loads(path.read_text())
        errors += errors_in(pack_v, pack, entry["url"])
        if pack.get("id") != entry["id"] or pack.get("version") != entry["version"]:
            errors.append(f"{entry['url']}: id or version differs from its catalog entry")
    for e in errors:
        print(f"ERROR {e}")
    print(f"schema: {len(catalog.get('packs', []))} packs, {'ok' if not errors else f'{len(errors)} errors'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
