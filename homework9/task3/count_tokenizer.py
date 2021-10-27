"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional


def count_line(file, tokenizer):
    """
    Count line in file
    :param file: path to file
    :param tokenizer: -
    :return: number of lines
    """
    line_counter = 0
    with open(file) as reading_file:
        for _ in reading_file:
            line_counter += 1
        return line_counter


def count_tokenizer(file, tokenizer):
    """
    Count tokenizer
    :param file: path to file
    :param tokenizer: specific tokenizer
    :return: number of tokenizer
    """
    token_counter = 0
    with open(file) as reading_file:
        for _ in map(tokenizer, reading_file):
            token_counter += 1
        return token_counter


def get_file_from_dir(dir_path, file_extension):
    """
    Function wolk in dir and found files with have file_extension
    :param dir_path: path to dir
    :param file_extension: file_extension
    :return: path to file
    """
    for file in os.listdir(dir_path):
        if file.endswith(file_extension) and os.path.isfile(
            os.path.join(dir_path, file)
        ):
            yield os.path.join(dir_path, file)


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Universal_file_counter
    :param dir_path: path to dir
    :param file_extension: file_extension
    :param tokenizer: specific tokenizer
    :return: number
    """
    counter = 0
    function_for_count = count_line if tokenizer is None else count_tokenizer
    for file in get_file_from_dir(dir_path, file_extension):
        counter += function_for_count(file, tokenizer)
    return counter
