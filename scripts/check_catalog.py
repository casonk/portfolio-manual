#!/usr/bin/env python3
"""Validate the public catalog without reaching outside this repository."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    catalog = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))
    repositories = catalog.get("repositories")
    if catalog.get("schema_version") != 1 or not isinstance(repositories, list):
        print("invalid catalog schema")
        return 1
    names: set[str] = set()
    for repository in repositories:
        if set(repository) != {"category", "name", "slug", "url"}:
            print(f"invalid catalog fields: {repository!r}")
            return 1
        name = repository["name"]
        if not all(isinstance(repository[field], str) and repository[field] for field in repository):
            print(f"invalid catalog value: {repository!r}")
            return 1
        if name in names or repository["url"] != f"https://github.com/{repository['slug']}":
            print(f"duplicate or invalid repository: {repository!r}")
            return 1
        names.add(name)
    if not repositories:
        print("catalog is empty")
        return 1
    print(f"catalog OK: {len(repositories)} repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
