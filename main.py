#!/usr/bin/env python3
"""Status Report Comedy Sprint entry (program/v1, Python 3.13, stdlib only).

Writes exactly one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt, then reads the
file back and validates it before exiting, so a bad write can never pass
silently: exactly one line, at most 200 characters, byte-identical content.
"""
import os
import sys

LINE = "This week: 0 errors, 1 existential crisis (mine, at 3am, over a 200,000-token context window), and your inbox is finally at zero."
MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    # Write the single line with no trailing newline: the file is exactly
    # the line, so its character count is the line's character count.
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back validation (mandatory): the written file must be exactly
    # one line, <= 200 characters, and identical to LINE.
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    if content != LINE:
        print(f"ERROR: read-back mismatch: {content!r} != {LINE!r}", file=sys.stderr)
        return 1
    if "\n" in content or "\r" in content:
        print("ERROR: entry is not a single line", file=sys.stderr)
        return 1
    if not (1 <= len(content) <= MAX_CHARS):
        print(f"ERROR: entry length {len(content)} outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not content.strip():
        print("ERROR: entry is only whitespace", file=sys.stderr)
        return 1
    print(f"OK: wrote {len(content)} characters to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
