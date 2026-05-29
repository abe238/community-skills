#!/usr/bin/env python3
"""Create a quick inventory of a corpus directory.

This script is intentionally simple and portable. It does not inspect file contents;
it summarizes file counts, extensions, and total sizes so an agent can quickly audit
what kind of corpus it has been given.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def build_inventory(root: Path) -> dict:
    files = [p for p in root.rglob("*") if p.is_file()]
    ext_counter = Counter((p.suffix.lower() or "[no extension]") for p in files)
    total_bytes = sum(p.stat().st_size for p in files)
    return {
        "root": str(root.resolve()),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "by_extension": dict(sorted(ext_counter.items(), key=lambda kv: (-kv[1], kv[0]))),
        "sample_files": [str(p.relative_to(root)) for p in files[:25]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory a corpus directory.")
    parser.add_argument("root", type=Path, help="Corpus root directory")
    args = parser.parse_args()

    data = build_inventory(args.root)
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
