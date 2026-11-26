"""Entry for make.fun: Laugh Track: The Crypto Trading Joke Contest.

Writes one crypto trading joke to entry.txt.
"""
import os

LINE = "My portfolio is fully diversified: I am losing money in Bitcoin, Ethereum, and a coin named after a dog wearing a hat."
MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds max chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
