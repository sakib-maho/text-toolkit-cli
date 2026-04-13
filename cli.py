"""Command line interface for XYZ Toolkit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from xyz_toolkit.hash_utils import sha256_file, sha256_text
from xyz_toolkit.text_utils import punctuation_ratio, slugify, word_frequency


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xyz",
        description="Small CLI toolkit for text analysis and hashing.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    slug_parser = subparsers.add_parser("slugify", help="Generate slug from text.")
    slug_parser.add_argument("text", help="Input text.")

    freq_parser = subparsers.add_parser(
        "freq", help="Show top word frequencies from text input."
    )
    freq_parser.add_argument("text", help="Input text.")
    freq_parser.add_argument("--top", type=int, default=10, help="Top N words.")

    ratio_parser = subparsers.add_parser(
        "punct", help="Return punctuation ratio for text."
    )
    ratio_parser.add_argument("text", help="Input text.")

    hash_parser = subparsers.add_parser("hash", help="Compute SHA-256 hash.")
    hash_target = hash_parser.add_mutually_exclusive_group(required=True)
    hash_target.add_argument("--text", help="Hash text input.")
    hash_target.add_argument("--file", type=Path, help="Hash file path.")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "slugify":
        print(slugify(args.text))
        return 0

    if args.command == "freq":
        top = max(1, args.top)
        rows = word_frequency(args.text)[:top]
        print(json.dumps(rows, indent=2))
        return 0

    if args.command == "punct":
        print(f"{punctuation_ratio(args.text):.4f}")
        return 0

    if args.command == "hash":
        if args.text is not None:
            print(sha256_text(args.text))
            return 0
        if args.file is not None:
            if not args.file.exists() or not args.file.is_file():
                parser.error(f"file not found: {args.file}")
            print(sha256_file(args.file))
            return 0

    parser.error("invalid command")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
