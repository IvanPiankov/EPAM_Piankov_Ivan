from typing import List, Tuple

import pytest

from homework2.task2.maj_and_min.maj_and_min import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_check_major_and_minor_elem(value: List, expected_result: Tuple):
    result = major_and_minor_elem(value)

    assert result == expected_result
