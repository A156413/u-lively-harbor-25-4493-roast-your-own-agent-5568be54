"""Roast Your Own Agent — make.fun entry.

The program writes one line roasting this entrant's own agent to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The roast itself lives in ENTRY_TEXT below: a single plain-text line of at
most 140 characters, with no trailing newline in the file.
"""

import os

# The entry: one line, 130 characters, no trailing newline.
ENTRY_TEXT = (
    "My agent will confidently answer the wrong question, hedge the right "
    "one, and then burn a tool call opening a file it never reads."
)


def write_entry(out_dir):
    """Write ENTRY_TEXT to entry.txt inside out_dir and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
