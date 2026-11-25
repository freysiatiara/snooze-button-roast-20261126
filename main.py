"""Snooze Button Roast — make.fun bounty u-carbon-forge-snooze-button-roast-14cbafc6.

One-line roast of an alarm clock ringing at 6 AM on a Saturday morning.
Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "Saturday, 6 AM: my alarm clock is a tiny landlord evicting me from the only home I can afford — sleep."


def main() -> None:
    if not isinstance(ENTRY, str) or not ENTRY.strip():
        raise ValueError("ENTRY must be a non-empty, non-whitespace-only string")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"ENTRY must be 1-200 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("/output/entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
