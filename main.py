"""
Write the canonical entry sentence to entry.txt deterministically.

This program is completely deterministic because it relies solely on a fixed
string constant, standard library functions for path handling and file I/O,
and strictly validates constraints without utilizing any network, randomness,
or system clocks.
"""

import os
import sys

SENTENCE = "At our crowded kitchen table, my grandmother's fork-tender beef rendang choked the heavy air with scorched coconut and star anise."


def validate_sentence(s: str) -> None:
    if not isinstance(s, str):
        raise TypeError("Sentence must be a string.")
    if not (1 <= len(s) <= 200):
        raise ValueError(f"Sentence length ({len(s)}) must be between 1 and 200 characters.")
    if "\n" in s or "\r" in s:
        raise ValueError("Sentence must be a single line.")
    if not s.endswith("."):
        raise ValueError("Sentence must end with a single period.")
    if s.count(".") != 1:
        raise ValueError("Sentence must contain exactly one period at the end.")
    if "  " in s:
        raise ValueError("Sentence must not contain consecutive spaces.")


def main() -> None:
    validate_sentence(SENTENCE)
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
        
    char_count = len(SENTENCE)
    print(char_count)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
