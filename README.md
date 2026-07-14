# Text Toolkit CLI

Text Toolkit CLI is a small but useful command-line toolbox for text cleanup,
lightweight content analysis, and hashing. The original `xyz_toolkit` package name
is still supported for compatibility, and a `text_toolkit` alias is also provided.

## Features

- `slugify` for URL-safe identifiers
- `freq` for top word frequency analysis
- `punct` for punctuation-density checks
- `emails` and `urls` extraction helpers
- `readability` proxy metrics for quick text diagnostics
- `hash` and `hmac` commands for SHA-256 workflows

## CLI Examples

```bash
python3 cli.py slugify "Hello Portfolio"
python3 cli.py freq "AI tools for ai engineers and tools" --top 3
python3 cli.py punct "Hello!!!"
python3 cli.py emails "Contact: a@example.com and b@example.com"
python3 cli.py urls "Read https://example.com/docs first"
python3 cli.py readability "Short sentence. Another short sentence."
python3 cli.py hash --text "important data"
python3 cli.py hash --file README.md
python3 cli.py hmac --key secret --text "important data"
```

## Python API

```python
from xyz_toolkit.text_utils import extract_emails, readability_proxy, slugify, word_freq
from xyz_toolkit.hash_utils import hmac_sha256, sha256_text

print(slugify("My New Project"))
print(word_freq("tools tools ai"))
print(extract_emails("Reach me at me@example.com"))
print(readability_proxy("Simple text. Another sentence."))
print(sha256_text("payload"))
print(hmac_sha256("secret", "payload"))
```

## Compatibility Notes

- Existing imports from `xyz_toolkit` continue to work.
- New imports can also use `text_toolkit`.
- Older helper names `word_frequency()` and `punctuation_ratio()` remain as aliases.

## Run Tests

```bash
python3 -m pytest -q
```

## License

MIT. See `LICENSE`.
