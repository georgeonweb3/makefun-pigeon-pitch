#!/usr/bin/env python3
"""Pigeon Pitch, One Line — the elevator pitch a city pigeon gives investors.

The line is the whole entry: a pigeon pitching its startup to investors.
It outlived the dinosaurs, the Romans, and the investor's last three
startups, and it is the only unicorn that is actually a bird.
"""

LINE = "We outlived the dinosaurs, the Romans, and your last three startups — invest in the only unicorn that's actually a bird. We never pivot, we just migrate."


# The brief's first criterion: the line must actually pitch to investors —
# it needs the ask, not just a joke about pigeons.
ASK_WORDS = ("invest", "Invest")


def validate(line: str) -> None:
    """The brief's gate: 1-200 characters, one line, in English."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    if not any(word in line for word in ASK_WORDS):
        raise SystemExit("line must pitch to investors (no ask found)")


def main() -> None:
    validate(LINE)
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
