import functools

import pytest

from homework5.task2.save_orig_info import *


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_custom_sum_with_list(capsys):
    expected_result = custom_sum([1, 2, 3], [4, 5])
    captur = capsys.readouterr()
    assert captur.out == "[1, 2, 3, 4, 5]\n"


def test_custom_sum_with_numbers(capsys):
    expected_result = custom_sum(1, 2, 3, 4)
    captur = capsys.readouterr()
    assert captur.out == "10\n"


def test_custom_sum_doc(capsys):
    print(custom_sum.__doc__)
    captur = capsys.readouterr()
    assert captur.out == "This function can sum any objects which have __add___\n"


def test_custom_sum_name(capsys):
    print(custom_sum.__name__)
    captur = capsys.readouterr()
    assert captur.out == "custom_sum\n"


def test_custom_sum_name_without_print(capsys):
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    captur = capsys.readouterr()
    assert captur.out == ""
