"""make.fun bounty entry: "The Long Roast: Lawmakers and the File They Cannot Convert".

The program copies the repository's entry.txt verbatim to the grader's output
path. entry.txt holds a single satirical line (158 characters, no trailing
newline) about lawmakers mandating human oversight for chatbots while still
converting Word documents to PDF by screenshotting pages into PowerPoint.

The copy is done with shutil.copyfile so the bytes are identical on every
grading run: no re-encoding, no newline translation, no rewriting. Before
copying, the script re-checks entry.txt against the published gate (valid
UTF-8, 1-320 characters, not only whitespace) and exits non-zero with a
message on stderr if the entry would be rejected.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The output directory defaults to /output when MAKEFUN_OUTPUT_DIR is unset, so
the same script works both on the grader and on a local machine.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CHARS = 320


def check_text(data: bytes) -> str | None:
    """Return an error message if data would fail the gate, else None."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return f"entry is not valid UTF-8: {exc}"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
    if not text.strip():
        return "entry must contain at least one non-whitespace character"
    return None


def main() -> int:
    """Copy entry.txt byte-for-byte into the output directory."""
    source = Path(__file__).resolve().parent / ENTRY_NAME
    if not source.is_file():
        print(f"error: missing entry file: {source}", file=sys.stderr)
        return 1

    data = source.read_bytes()
    problem = check_text(data)
    if problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    # An empty MAKEFUN_OUTPUT_DIR would resolve to ".", which is never what we
    # want, so treat blank values as unset and fall back to the grader path.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    destination = output_dir / ENTRY_NAME

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: cannot write {destination}: {exc}", file=sys.stderr)
        return 1

    if destination.read_bytes() != data:
        print(f"error: copy to {destination} was not byte-identical", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({len(data.decode('utf-8'))} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
