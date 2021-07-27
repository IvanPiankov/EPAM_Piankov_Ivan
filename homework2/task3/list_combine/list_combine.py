"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List, Tuple


def combinations(*args: List[Any]) -> List[Tuple[Any]]:
    """
    Create all combinations with elements from any lists
    :param args: lists with elements
    :return: lists with combinations
    """
    return list(itertools.product(*args))
