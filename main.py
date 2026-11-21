#!/usr/bin/env python3
"""The joke the reviewer laughs at — a make.fun entry.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt, exactly as the competition's gate expects:
UTF-8 text, 1 to 280 characters, not only whitespace.
"""

import os

JOKE = "My agent writes 900 lines before my coffee; my whole job now is one review comment: 'why?'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
