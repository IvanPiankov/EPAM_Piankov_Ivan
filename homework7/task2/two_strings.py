"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def to_list(string_with_elem: str) -> list:
    """
    Transform string to list and deleting element which have in front of #
    :param string_with_elem:
    :return: list
    """
    chars_list = []
    for char in string_with_elem:
        if char != "#":
            chars_list.append(char)
        elif len(chars_list) > 0:
            chars_list.pop()
    return chars_list


def backspace_compare(first: str, second: str) -> bool:
    """
    Function which compare two strings
    :param first: str
    :param second: str
    :return: bool
    """
    return all(
        first_element == second_element
        for first_element, second_element in zip_longest(
            to_list(first), to_list(second)
        )
    )
