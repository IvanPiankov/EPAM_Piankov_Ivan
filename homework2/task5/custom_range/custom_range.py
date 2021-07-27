"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:

import string

assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List, Sequence


def custom_range(iterable_values: Sequence[Any], *args) -> List[Any]:
    """
    Function take 3 or less argument and accept any iterable of unique values and then
    it behaves as range function
    :param iterable_values: iterable collections
    :param args: any arguments
    :return: list  of values in a given range
    """
    if len(args) == 0:
        return []
    step = 1
    if len(args) == 1:
        start_position = 0
        stop_position = iterable_values.index(args[0])
    elif len(args) == 2:
        start_position = iterable_values.index(args[0])
        stop_position = iterable_values.index(args[1])
    else:
        start_position = iterable_values.index(args[0])
        stop_position = iterable_values.index(args[1])
        step = args[2]
    list_result = [i for i in iterable_values[start_position:stop_position:step]]
    return list_result
