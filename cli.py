"""Command line interface for Text Toolkit CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from xyz_toolkit.hash_utils import hmac_sha256, sha256_file, sha256_text
from xyz_toolkit.text_utils import (
    extract_emails,
    extract_urls,
    punct_ratio,
    readability_proxy,
    slugify,
    word_freq,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="text-toolkit",
        description="Common text analysis and hashing helpers from the command line.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    slug_parser = subparsers.add_parser("slugify", help="Generate a URL-friendly slug.")
    slug_parser.add_argument("text", help="Input text.")

    freq_parser = subparsers.add_parser("freq", help="Show top word frequencies.")
    freq_parser.add_argument("text", help="Input text.")
    freq_parser.add_argument("--top", type=int, default=10, help="Top N words.")

    ratio_parser = subparsers.add_parser("punct", help="Return punctuation ratio.")
    ratio_parser.add_argument("text", help="Input text.")

    emails_parser = subparsers.add_parser("emails", help="Extract email addresses.")
    emails_parser.add_argument("text", help="Input text.")

    urls_parser = subparsers.add_parser("urls", help="Extract URLs.")
    urls_parser.add_argument("text", help="Input text.")

    readability_parser = subparsers.add_parser("readability", help="Show lightweight readability metrics.")
    readability_parser.add_argument("text", help="Input text.")

    hash_parser = subparsers.add_parser("hash", help="Compute SHA-256 hash.")
    hash_target = hash_parser.add_mutually_exclusive_group(required=True)
    hash_target.add_argument("--text", help="Hash text input.")
    hash_target.add_argument("--file", type=Path, help="Hash file path.")

    hmac_parser = subparsers.add_parser("hmac", help="Compute HMAC-SHA256 for text.")
    hmac_parser.add_argument("--key", required=True, help="Shared secret key.")
    hmac_parser.add_argument("--text", required=True, help="Input text.")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "slugify":
        print(slugify(args.text))
        return 0
    if args.command == "freq":
        print(json.dumps(word_freq(args.text)[: max(1, args.top)], indent=2))
        return 0
    if args.command == "punct":
        print(f"{punct_ratio(args.text):.4f}")
        return 0
    if args.command == "emails":
        print(json.dumps(extract_emails(args.text), indent=2))
        return 0
    if args.command == "urls":
        print(json.dumps(extract_urls(args.text), indent=2))
        return 0
    if args.command == "readability":
        print(json.dumps(readability_proxy(args.text), indent=2))
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
    if args.command == "hmac":
        print(hmac_sha256(args.key, args.text))
        return 0

    parser.error("invalid command")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
