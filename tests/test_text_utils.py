from xyz_toolkit.text_utils import (
    extract_emails,
    extract_urls,
    punct_ratio,
    readability_proxy,
    slugify,
    word_freq,
    word_frequency,
)


def test_slugify() -> None:
    assert slugify("Hello, Portfolio Project!") == "hello-portfolio-project"


def test_word_freq_sorting() -> None:
    rows = word_freq("AI code ai tools tools tools")
    assert rows[0] == ("tools", 3)
    assert rows[1] == ("ai", 2)
    assert rows[2] == ("code", 1)


def test_word_frequency_alias() -> None:
    assert word_frequency("one one two") == [("one", 2), ("two", 1)]


def test_punctuation_ratio() -> None:
    ratio = punct_ratio("hello!!!")
    assert ratio == 3 / 8


def test_extract_emails() -> None:
    emails = extract_emails("Contact a@example.com or b@example.com. Repeat a@example.com.")
    assert emails == ["a@example.com", "b@example.com"]


def test_extract_urls() -> None:
    urls = extract_urls("Docs: https://example.com/docs and http://test.dev/path")
    assert urls == ["https://example.com/docs", "http://test.dev/path"]


def test_readability_proxy() -> None:
    stats = readability_proxy("Short sentence. A second sentence appears here!")
    assert stats["word_count"] == 7.0
    assert stats["sentence_count"] == 2.0
    assert stats["avg_sentence_length"] == 3.5
