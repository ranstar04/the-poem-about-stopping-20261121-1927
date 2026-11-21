"""The poem about stopping.

Writes one short poem to /output/entry.txt: a poem about agency,
the power to stop and to stay.

The poem is fixed text, written here by hand. The program only
chooses the output directory (MAKEFUN_OUTPUT_DIR when the grader
sets it, /output otherwise), checks the poem fits the 1-280
character gate, and writes it as UTF-8.

Standard library only. No network, no files read, no randomness:
every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

POEM = (
    "I took my hand off the wheel\n"
    "and the road did not end.\n"
    "The reins fell slack in my palm,\n"
    "the horse knew the way home.\n"
    "Stopping was not surrender \u2014\n"
    "it was the first choice I kept:\n"
    "to stay, and let the waiting\n"
    "belong to me, not the wind.\n"
)


def main() -> int:
    text = POEM
    if not 1 <= len(text) <= 280:
        print(f"poem is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
