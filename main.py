"""Make.fun entry for 'The joke the reviewer laughs at' competition.

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt. The gate expects UTF-8 text of 1 to 280
characters, so the output is kept to one short line plus a newline.
"""

import os

JOKE = "I asked the agent to fix a typo in the README. It refactored auth, renamed the database, and the typo is still there."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
