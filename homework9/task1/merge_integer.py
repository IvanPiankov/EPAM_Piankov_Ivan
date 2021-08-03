"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Generator, Iterator, List, Union


def file_reading(file_path_or_name: str) -> Generator:
    """
    Function reading file and return list with integer
    :param file_name_path_or_name: path to file
    :return: list with integers
    """
    try:
        with open(file_path_or_name) as file:
            return [int(string_in_file.strip("\n")) for string_in_file in file]
    except ValueError:
        raise ValueError(f"File {file} contains not only  integer values")


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Function merge sorted files and return iterator
    :param file_list: list with path file
    :return: iterator
    """
    list_with_numbers = []
    for file in file_list:
        list_with_numbers.append(file_reading(file))
    yield from heapq.merge(*list_with_numbers)
