import pytest

from homework1.task2.fib_sequence.fib_sequence import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([0], True),
        ([0, 1], True),
        ([0, 1, 1], True),
        ([0, 1, 1, 2, 3], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_check_sum_of_four(data: list, expected_result: bool):
    result = check_fibonacci(data)

    assert result == expected_result
