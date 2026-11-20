#!/usr/bin/env python3
"""Fail when a pack changed but its version didn't go up.

    python3 scripts/check_versions.py --base origin/main

Apps update a pack only when the catalog's version for it is higher than the
one they have installed, so a pack whose bytes changed under the same version
would never reach anyone who already has it. This compares catalog.json in
the working tree with the one at --base and reports every pack that

  - changed (a different sha256) without a higher version,
  - went down a version, or
  - left the catalog (apps that have it installed would stop getting updates).
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def version_errors(base: dict, head: dict) -> list[str]:
    """Every way `head`'s packs break the update promise `base` made."""
    errors: list[str] = []
    head_by_id = {p["id"]: p for p in head.get("packs", [])}
    for old in base.get("packs", []):
        new = head_by_id.get(old["id"])
        if new is None:
            errors.append(f"{old['id']}: left the catalog")
        elif new["version"] < old["version"]:
            errors.append(f"{old['id']}: version went down from {old['version']} to {new['version']}")
        elif new["sha256"] != old["sha256"] and new["version"] == old["version"]:
            errors.append(f"{old['id']}: changed but is still version {old['version']}; bump its version")
    return errors


def catalog_at(ref: str) -> dict | None:
    """catalog.json as it was at `ref`, or None when it didn't exist yet."""
    result = subprocess.run(
        ["git", "show", f"{ref}:catalog.json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout) if result.returncode == 0 else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check that changed packs got a higher version.")
    parser.add_argument("--base", required=True, help="the git ref to compare catalog.json against")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    base = catalog_at(args.base)
    if base is None:
        print(f"no catalog.json at {args.base}; nothing to compare")
        return 0
    head = json.loads((ROOT / "catalog.json").read_text())
    errors = version_errors(base, head)
    for e in errors:
        print(f"ERROR {e}")
    if not errors:
        print("versions: ok")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
