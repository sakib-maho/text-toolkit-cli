"""Hash utilities used by the CLI."""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_text(content: str) -> str:
    """Return SHA-256 hash of a text input."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    """Return SHA-256 hash of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
