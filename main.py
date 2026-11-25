#!/usr/bin/env python3
"""Write the entry slogan for the Solana wallet agent competition."""

from pathlib import Path

SLOGAN = "The wallet that runs your Solana errands and knocks before spending."
OUTPUT = Path("/output/entry.txt")


def check(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError("slogan must be 1-140 characters")
    if len(text.split()) > 20:
        raise ValueError("slogan must be at most 20 words")
    if text != text.strip() or not text.strip():
        raise ValueError("slogan must not be blank or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("slogan must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("slogan must not contain control characters")
    text.encode("utf-8").decode("utf-8")


def main() -> None:
    check(SLOGAN)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(SLOGAN, encoding="utf-8")


if __name__ == "__main__":
    main()
