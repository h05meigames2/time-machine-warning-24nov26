#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label (<=120 characters) for a time
machine to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, no network.
"""

import os

ENTRY_LINE = (
    "WARNING: Never wave at yourself — if you wave back, the timeline "
    "now has two of you, and only one is insured."
)


def main() -> None:
    line = ENTRY_LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
