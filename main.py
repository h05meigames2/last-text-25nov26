#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes the dying phone's final text message to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

LINE = "I've been at 1% for ten whole minutes out of pure spite. The charger's three feet away and you just watched me die. Goodbye. Tell the Wi-Fi I loved it more than you."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    assert isinstance(line, str) and line, "entry must not be empty"
    assert line == line.strip(), "entry must not have leading or trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(LINE)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
