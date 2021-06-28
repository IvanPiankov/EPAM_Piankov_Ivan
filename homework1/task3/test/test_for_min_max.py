from pathlib import Path

from homework1.task3.min_max_value.min_max_value import find_maximum_and_minimum

path = Path.cwd().joinpath("test_data")


def test_min_max_value_check_1():

    path_to_file = Path(path).joinpath("first_check.txt")
    result = find_maximum_and_minimum(path_to_file)
    assert result == (-5, 5)


def test_min_max_value_check_2():
    path_to_file = Path(path).joinpath("one_value.txt")
    result = find_maximum_and_minimum(path_to_file)
    assert result == (5, 5)


def test_min_max_value_check_3():
    path_to_file = Path(path).joinpath("zero_check.txt")
    result = find_maximum_and_minimum(path_to_file)
    assert result == (0, 5)
