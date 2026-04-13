"""Text processing utilities for the XYZ CLI."""

from __future__ import annotations

import re
import string
from collections import Counter


def slugify(value: str) -> str:
    """Convert text into a lowercase URL slug."""
    cleaned = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9\s-]", "", cleaned)
    cleaned = re.sub(r"[\s_-]+", "-", cleaned)
    return cleaned.strip("-")


def word_frequency(text: str) -> list[tuple[str, int]]:
    """Return sorted word frequencies for a text block."""
    words = re.findall(r"[a-zA-Z0-9']+", text.lower())
    counts = Counter(words)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def punctuation_ratio(text: str) -> float:
    """Compute punctuation characters ratio in text."""
    if not text:
        return 0.0
    punctuation_count = sum(1 for ch in text if ch in string.punctuation)
    return punctuation_count / len(text)
