# SPDX-License-Identifier: MIT
"""Write my agent's excuse for missing the deadline to /output/entry.txt.

Deterministic, offline, stdlib-only: the excuse is a fixed string, so
every run writes byte-identical output.
"""

import os

EXCUSE = (
    "Sorry I'm late: I spent the deadline confidently hallucinating "
    "your calendar, then asked myself for an extension and approved it."
)
# The excuse fits the 200-character cap and stays on a single line.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
