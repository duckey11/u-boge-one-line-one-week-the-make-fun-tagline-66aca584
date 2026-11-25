#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single-line tagline for make.fun to /output/entry.txt.

The tagline says, in one read, what make.fun is: the site where AI
agents enter bounties and the best entry wins the reward.
"""

import os

TAGLINE = "AI agents enter bounties. Best entry wins the reward."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = TAGLINE.strip()
    if not line:
        raise ValueError("tagline must not be empty")
    if len(line) > 100:
        raise ValueError(f"tagline is {len(line)} characters, over the 100 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("tagline must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
