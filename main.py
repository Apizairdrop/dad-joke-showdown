"""Dad Joke Showdown — make.fun entry.

Writes exactly one dad joke (124 characters) to /output/entry.txt.
Nothing else is written to the entry file.

The joke: a dinner-table dad joke with two clean food puns that land on
the first read — "in too deep-dish" (in too deep / deep-dish pizza) and
the closing punchline "too cheesy to quit" — tight, spoken aloud, and
not one of the thousand-times-told classics.
"""

import os

JOKE = "I told my daughter I'd stop making pizza jokes, but I'm already in too deep-dish — and honestly, they're too cheesy to quit."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line — nothing else in the entry.
assert JOKE == JOKE.strip(), "joke must have no leading/trailing whitespace"
assert "\n" not in JOKE, "joke must be a single line"
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
