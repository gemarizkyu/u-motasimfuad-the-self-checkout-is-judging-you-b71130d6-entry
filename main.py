#!/usr/bin/env python3
"""The Self-Checkout Is Judging You -- make.fun entry.

Writes one funny line in the voice of a smug self-checkout machine to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set for local runs).

Deterministic by construction: no input, no clock, no randomness, no network,
no model calls. The same line is written on every run.
"""

import os
from pathlib import Path

LINE = "Twelve yogurts, zero spoons, zero plan. Please place your coping mechanism in the bagging area."


def main() -> None:
    # The gate accepts 1-200 characters; fail loudly locally if ever breached.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
