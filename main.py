#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one warm line about a small good thing today to
``<MAKEFUN_OUTPUT_DIR or /output>/entry.txt``: no trailing newline,
1-200 characters, not whitespace-only.
"""

import os
import sys

LINE = (
    "This morning the warteg lady remembered I like extra kerupuk "
    "and slipped two into my bag without charging \u2014 small kindness, "
    "whole day brighter."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print(
            f"invalid line: {len(LINE)} chars",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
