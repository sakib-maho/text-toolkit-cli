"""Text processing utilities for the toolkit CLI."""

from __future__ import annotations

import re
import string
from collections import Counter


EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_PATTERN = re.compile(r"https?://[^\s<>\"]+")
WORD_PATTERN = re.compile(r"[A-Za-z0-9']+")
SENTENCE_SPLIT_PATTERN = re.compile(r"[.!?]+")


def slugify(value: str) -> str:
    """Convert text into a lowercase URL slug."""
    cleaned = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9\s-]", "", cleaned)
    cleaned = re.sub(r"[\s_-]+", "-", cleaned)
    return cleaned.strip("-")


def word_freq(text: str) -> list[tuple[str, int]]:
    """Return sorted word frequencies for a text block."""
    words = WORD_PATTERN.findall(text.lower())
    counts = Counter(words)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def punct_ratio(text: str) -> float:
    """Compute punctuation characters ratio in text."""
    if not text:
        return 0.0
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    return punctuation_count / len(text)


def extract_emails(text: str) -> list[str]:
    """Extract unique email addresses preserving first-seen order."""
    return list(dict.fromkeys(EMAIL_PATTERN.findall(text)))


def extract_urls(text: str) -> list[str]:
    """Extract unique HTTP(S) URLs preserving first-seen order."""
    return list(dict.fromkeys(URL_PATTERN.findall(text)))


def readability_proxy(text: str) -> dict[str, float]:
    """Return lightweight readability proxy metrics for plain text."""
    words = WORD_PATTERN.findall(text)
    sentences = [sentence for sentence in SENTENCE_SPLIT_PATTERN.split(text) if sentence.strip()]
    if not words:
        return {
            "word_count": 0.0,
            "sentence_count": 0.0,
            "avg_word_length": 0.0,
            "avg_sentence_length": 0.0,
            "long_word_ratio": 0.0,
        }

    sentence_count = len(sentences) or 1
    avg_word_length = sum(len(word) for word in words) / len(words)
    avg_sentence_length = len(words) / sentence_count
    long_word_ratio = sum(1 for word in words if len(word) >= 7) / len(words)
    return {
        "word_count": float(len(words)),
        "sentence_count": float(sentence_count),
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
        "long_word_ratio": long_word_ratio,
    }


def word_frequency(text: str) -> list[tuple[str, int]]:
    """Backward-compatible alias for older imports."""
    return word_freq(text)


def punctuation_ratio(text: str) -> float:
    """Backward-compatible alias for older imports."""
    return punct_ratio(text)
