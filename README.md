[![Competition](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![Rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Dedypol22/joke-reviewer-entry/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![Reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Dedypol22/joke-reviewer-entry/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

# The Typo Is Still There

This is my entry for the make.fun competition "The joke the reviewer laughs at". It is a tiny Python program with one job: write a single one-line joke to `/output/entry.txt`.

The joke is about a familiar moment when working beside AI coding agents. You ask for the smallest possible fix, a typo in the README, and the agent enthusiastically rebuilds half the project around it — new auth, renamed database, the works — while the original typo survives untouched.

There is no setup, no dependencies, and no network access. Just Python 3 and the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program creates `/output` if it does not exist yet, then writes the joke followed by a newline. The output is UTF-8 text of 1 to 280 characters, as the gate requires.
