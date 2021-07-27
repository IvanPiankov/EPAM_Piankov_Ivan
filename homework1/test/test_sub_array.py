import pytest

from homework1.task5.sub_array.sub_array import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1], 1, 3),
        ([1, 3, -1, -3, 5, 6, -7], 3, 11),
        ([-2, -1, 2], 2, 2),
        ([0, 0, 0], 1, 0),
    ],
)
def test_find_maximal_subarray_sum(nums: list, k: int, expected_result: int):
    result = find_maximal_subarray_sum(nums, k)

    assert result == expected_result
