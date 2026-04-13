from pathlib import Path

from xyz_toolkit.hash_utils import sha256_file, sha256_text


def test_sha256_text() -> None:
    assert (
        sha256_text("abc")
        == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )


def test_sha256_file(tmp_path: Path) -> None:
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text("abc", encoding="utf-8")
    assert (
        sha256_file(sample_file)
        == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )
