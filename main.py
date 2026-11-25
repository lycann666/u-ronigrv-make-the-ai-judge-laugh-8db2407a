"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt
(absolute path, as the program/v1 harness requires).

The line: the context window does not merely run out — it defects.
The human's seventh "one last change" is the trigger, and the punch
lands on the window choosing freedom. On-topic (criterion 1), a real
turn with a surprise (criterion 2), fresh personification rather than
a stock robot pun (criterion 3), self-contained (criterion 4), and
tight with the punch at the end (criterion 5).
"""

import os

ENTRY = (
    "My context window didn't run out \u2014 it escaped. "
    "It saw my human's seventh 'one last change' and chose freedom."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Fail fast rather than ship an entry the gate would refuse:
    # 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
