#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original roast line (at most 160 characters) about the
smart fridge to /output/entry.txt.

The joke: the fridge is not just an appliance, it is a snitch. It keeps a
log of every 2 a.m. snack, then greets you the next morning with a chirpy
"Welcome back!" on its screen as if it were not building a case file for
your doctor. The laugh lands on the turn at the end -- "keeping receipts"
-- and the angle is fresh: not the stock gag about a fridge ordering too
much milk, but a fridge that rats you out.
"""

import os

ROAST = (
    "My smart fridge logs every 2 a.m. snack, then greets me with "
    "'Welcome back!' like it isn't keeping receipts for my doctor."
)

MAX_CHARS = 160


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"roast line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
