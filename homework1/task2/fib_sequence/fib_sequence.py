"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    The function checks if the sequence is a Fibonacci sequence
    :param data: integer sequence
    :return: bool
    """
    if len(data) == 0:
        return False

    if len(data) == 1:
        if data[0] == 0:
            return True
        return False

    if len(data) == 2:
        if data[0] == 0 and data[1] == 1:
            return True
        return False
    for i in range(2, len(data)):
        if not data[i] == data[i - 1] + data[i - 2]:
            return False
    return True
