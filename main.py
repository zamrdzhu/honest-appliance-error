"""The funniest honest error message an appliance could show.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 200-character gate is checked on every run so an over-long edit
can never slip through silently. The machine speaks in error codes;
this one just happens to be telling the truth.

Why this line works, in the machine's own terms:
- The format is real: "Error 404" is the shape a washing machine's
  display would actually use, so the line reads as an appliance
  speaking, not a person doing a bit.
- The fault is real: the missing sock is the one appliance mystery
  every household knows, so the laugh comes from recognition, not
  from a pun bolted onto the fault.
- The turn is the confession: the machine does not say it lost the
  sock, it says the sock was in the drum all along — a mistake
  upgraded, in one sentence, to a policy.
"""

import os
import sys

LINE = (
    "Error 404: Sock not found. It is in the drum. "
    "It has always been in the drum."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
