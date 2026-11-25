"""Entry for the make.fun bounty "The Funniest Office Joke, Judged Head
to Head".

The program writes one joke about office life, a single line, to
/output/entry.txt. The joke has a setup and a turn built on something
anyone who has worked in an office recognises, with the punchline last:
nobody catches the faller, they just sidestep in formation. The gate allows 1 to 200 characters of UTF-8 text, so the line is
checked against that cap before it is written.
"""

import os

ENTRY = (
    "Our team building exercise was trust falls, so I fell backwards and "
    "watched fourteen coworkers step aside in perfect agile formation."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
