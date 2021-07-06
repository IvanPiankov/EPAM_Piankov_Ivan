import string
from typing import Any, List, Sequence

import pytest

from homework2.task5.custom_range.custom_range import custom_range


@pytest.mark.parametrize(
    ["iterable_values", "args", "expected_result"],
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ("g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ("p", "g", -2), ["p", "n", "l", "j", "h"]),
        (string.ascii_lowercase, (), []),
    ],
)
def test_check_custom_range(
    iterable_values: Sequence[Any], args: List[Any], expected_result: List[Any]
):
    result = custom_range(iterable_values, *args)
    assert result == expected_result
