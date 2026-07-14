# Text Toolkit CLI

`xyz` is now a practical Python command line toolkit for common text and hashing tasks.
It is designed as a lightweight utility project that demonstrates clean module structure,
testing, and developer-friendly CLI design.

## Features

- `slugify` command to convert text into URL-friendly slugs
- `freq` command to print top word frequencies in JSON
- `punct` command to compute punctuation ratio for text quality checks
- `hash` command to generate SHA-256 for text or files
- Unit tests for utilities and CLI behavior

## Tech Stack

- Python 3.10+
- Standard library (`argparse`, `hashlib`, `json`, `re`)
- `pytest` for tests

## Quick Start

```bash
git clone https://github.com/sakib-maho/text-toolkit-cli.git
cd text-toolkit-cli
python3 -m pip install pytest
```

## CLI Examples

```bash
python3 cli.py slugify "Hello Portfolio"
python3 cli.py freq "AI tools for ai engineers and tools"
python3 cli.py punct "Hello!!!"
python3 cli.py hash --text "important data"
python3 cli.py hash --file README.md
```

## Run Tests

```bash
python3 -m pytest -q
```

## Project Structure

```text
xyz/
├── cli.py
├── xyz_toolkit/
│   ├── hash_utils.py
│   └── text_utils.py
└── tests/
    ├── test_cli.py
    ├── test_hash_utils.py
    └── test_text_utils.py
```

## License

MIT License. See `LICENSE`.
