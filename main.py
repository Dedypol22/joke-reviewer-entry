"""Make.fun entry for the joke competition.

This program writes a single one-line joke to /output/entry.txt.
The submission gate expects UTF-8 text of 1 to 280 characters,
so the joke is kept short and plain, with a trailing newline.
"""

import os

JOKE = "My agent writes 900 lines before my coffee; my whole job now is one review comment: 'why?'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
