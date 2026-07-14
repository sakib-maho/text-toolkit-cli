from pathlib import Path
from subprocess import run


def run_cli(*args: str) -> str:
    result = run(["python3", "cli.py", *args], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def test_cli_slugify() -> None:
    assert run_cli("slugify", "My New Project") == "my-new-project"


def test_cli_hash_file(tmp_path: Path) -> None:
    payload = tmp_path / "payload.txt"
    payload.write_text("abc", encoding="utf-8")
    output = run_cli("hash", "--file", str(payload))
    assert output == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def test_cli_emails() -> None:
    output = run_cli("emails", "a@example.com and b@example.com")
    assert "a@example.com" in output
    assert "b@example.com" in output


def test_cli_urls() -> None:
    output = run_cli("urls", "https://example.com/docs")
    assert "https://example.com/docs" in output


def test_cli_readability() -> None:
    output = run_cli("readability", "One short sentence. Another one follows.")
    assert "\"sentence_count\"" in output
    assert "\"avg_sentence_length\"" in output


def test_cli_hmac() -> None:
    output = run_cli("hmac", "--key", "secret", "--text", "abc")
    assert len(output) == 64
