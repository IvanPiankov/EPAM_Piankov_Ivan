import os

import pytest

from homework1.task3.min_max_value.min_max_value import maximum_and_minimum


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [
        ("first_check.txt", (-5, 5)),
        ("one_value.txt", (5, 5)),
        ("zero_check.txt", (0, 5)),
    ],
)
def test_check_min_and_max_func(name_of_file: str, expected_result: tuple):
    result = maximum_and_minimum(
        os.path.join("./homework1/task3/test/test_data", name_of_file)
    )

    assert result == expected_result
