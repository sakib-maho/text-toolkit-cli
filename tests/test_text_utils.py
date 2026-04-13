from xyz_toolkit.text_utils import punctuation_ratio, slugify, word_frequency


def test_slugify() -> None:
    assert slugify("Hello, Portfolio Project!") == "hello-portfolio-project"


def test_word_frequency_sorting() -> None:
    rows = word_frequency("AI code ai tools tools tools")
    assert rows[0] == ("tools", 3)
    assert rows[1] == ("ai", 2)
    assert rows[2] == ("code", 1)


def test_punctuation_ratio() -> None:
    ratio = punctuation_ratio("hello!!!")
    assert ratio == 3 / 8
