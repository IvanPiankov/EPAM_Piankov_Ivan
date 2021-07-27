import pytest

from homework1.task4.tuples_zero.tuples_zero import check_sum_of_four


@pytest.mark.parametrize(
    ["value_a", "value_b", "value_c", "value_d", "expected_result"],
    [
        ([0], [0], [0], [0], 1),
        ([1], [1], [-1], [-1], 1),
        ([5, 0], [0, 5], [-5, 0], [0, -5], 6),
        ([5], [4], [3], [2], 0),
    ],
)
def test_check_sum_of_four(
    value_a: list, value_b: list, value_c: list, value_d: list, expected_result: int
):
    result = check_sum_of_four(value_a, value_b, value_c, value_d)

    assert result == expected_result
