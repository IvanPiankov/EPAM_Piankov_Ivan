"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function find maximal sum of sub-array with length less equal to "k"
    :param nums: integer list
    :param k: length of element in sub-array
    :return: sum
    """
    assert k <= len(nums)
    assert k > 0

    if k == 1:
        return max(nums)
    else:
        sum_array = min(nums)
        for i in range(1, k + 1):
            for j in range(i, len(nums) + 1):
                first_elem_in_window = j - i
                sum_of_sub_array = sum(nums[first_elem_in_window:j])
                sum_array = max(sum_array, sum_of_sub_array)
        return sum_array
