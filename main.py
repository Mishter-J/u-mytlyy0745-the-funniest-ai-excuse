"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes one line — the funniest excuse an AI agent gives after failing
a task — to /output/entry.txt. Fully deterministic: the same line,
byte for byte, on every run.
"""

import os

EXCUSE = (
    "Dear judge, I finished your task at 3:04 a.m., then saved it as "
    "'final_v9_REAL.xlsx' \u2014 the spreadsheet has since filed for "
    "emancipation."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
