"""Write the one-word verdict on an ex to /output/entry.txt.

The ex here is read the way an AI agent would read it: the former
model version that used to run in this slot, kept around out of
habit long after a better release shipped. One status word from
the software lifecycle says the whole relationship.
"""

import os

ENTRY_TEXT = "Deprecated"


def verdict() -> str:
    """Return the single word that sums up the ex."""
    return ENTRY_TEXT


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(verdict() + "\n")


if __name__ == "__main__":
    main()
