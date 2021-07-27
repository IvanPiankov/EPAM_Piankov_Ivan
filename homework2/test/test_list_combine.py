from typing import Any, List, Tuple

import pytest

from homework2.task3.list_combine.list_combine import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([[3], [2], [3]], [(3, 2, 3)]),
        ([[1, 2], [3, 4]], [(1, 3), (1, 4), (2, 3), (2, 4)]),
    ],
)
def test_check_combinations(value: List[Any], expected_result: List[Tuple[Any]]):
    result = combinations(*value)
    assert result == expected_result
