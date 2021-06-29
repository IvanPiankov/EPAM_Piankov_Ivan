import os

import pytest
from homework2.task1.text_symbol.text_symbol import *


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [
        (
            "longest_word_and_punct.txt",
            [
                "Hello",
                "PrivetAnswer",
                "Longest",
                "popopopopopopo",
                "victory",
                "find",
                "shell",
                "minus",
                "Solongsosolong",
                "plus",
            ],
        ),
        ("english_one_word_and_punct.txt", ["Hello"]),
    ],
)
def test_check_longest_word(name_of_file: str, expected_result: tuple):
    result = get_longest_diverse_words(
        os.path.join("./homework2/task1/tests/test_data", name_of_file)
    )
    result = set(result)
    expected_result = set(expected_result)
    assert result == expected_result


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [("rer_symbol", "a"), ("one_word_and_punct.txt", "!"),],
)
def test_check_get_rarest_char(name_of_file: str, expected_result: str):
    result = get_rarest_char(
        os.path.join("./homework2/task1/tests/test_data", name_of_file)
    )
    assert result == expected_result


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [
        ("longest_word_and_punct.txt", 7),
        ("one_word_and_punct.txt", 1),
        ("empty_file.txt", 0),
    ],
)
def test_check_count_punctuation_chars(name_of_file: str, expected_result: int):
    result = count_punctuation_chars(
        os.path.join("./homework2/task1/tests/test_data", name_of_file)
    )
    assert result == expected_result


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [("one_word_and_punct.txt", 17), ("empty_file.txt", 0)],
)
def test_check_count_non_ascii_chars(name_of_file: str, expected_result: int):
    result = count_non_ascii_chars(
        os.path.join("./homework2/task1/tests/test_data", name_of_file)
    )
    assert result == expected_result


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [("one_word_and_punct.txt", "Ð"), ("longest_word_and_punct.txt", "\n")],
)
def test_check_get_most_common_non_ascii_char(name_of_file: str, expected_result: int):
    result = get_most_common_non_ascii_char(
        os.path.join("./homework2/task1/tests/test_data", name_of_file)
    )
    assert result == expected_result
