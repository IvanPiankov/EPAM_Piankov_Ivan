"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Any, Tuple


def maximum_and_minimum(file_name: str) -> Tuple[Any, Any]:
    """
    Function found maximum and minimum in file
    :param file_name: file_name
    :return:min and max value
    """
    min_value = None
    max_value = None

    with open(file_name, "r") as fi:
        for line in fi:
            number = int(line.strip())

            if min_value is None or min_value > number:
                min_value = number

            if max_value is None or max_value < number:
                max_value = number

    return min_value, max_value
