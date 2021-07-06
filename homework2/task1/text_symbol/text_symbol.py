"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    :param file_path: path to file
    :return: list with words
    """
    with open(file_path, encoding="unicode escape") as file:
        # Create dict to save some parameters of words and set for uniq words
        word_dict = {}
        word_set = set()
        # Unique number of words
        uniq_number_of_word = 0
        for line in file:
            list_of_word_on_line = line.strip().split()
            for word in list_of_word_on_line:
                word = word.strip(string.punctuation)
                length_word = len(word)
                count_uniq_symbol = len(set(word))
                param_word = (length_word, count_uniq_symbol, uniq_number_of_word)
                if param_word not in word_dict and word not in word_set:
                    word_dict[param_word] = word
                    word_set.add(word)
                    uniq_number_of_word += 1
    # sorting firstly by length after by uniq chars in word
    keys_sort = sorted(word_dict.keys(), key=lambda x: (x[0], x[1]), reverse=True)
    list_with_word = []
    for keys in keys_sort:
        list_with_word.append(word_dict[keys])
        if len(list_with_word) > 9:
            break
    return list_with_word


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    :param file_path: path to file
    :return: char
    """
    count = Counter()
    with open(file_path, encoding="unicode-escape") as f:
        for line in f:
            for char in line:
                count[char] += 1
    return count.most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    """
    Count every punctuation char
    :param file_path: path to file
    :return: count of punctuation chars
    """
    # set with all punctuation chars
    list_of_punctuation = set(string.punctuation)
    count = 0
    with open(file_path, encoding="unicode-escape") as f:
        for line in f:
            for char in line:
                if char in list_of_punctuation:
                    count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char
    :param file_path: path to file
    :return: count of non ascii char
    """
    list_of_ascii = set(string.ascii_letters)
    count = 0
    with open(file_path, encoding="unicode-escape") as f:
        for line in f:
            for char in line:
                if char not in list_of_ascii:
                    count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    :param file_path: path to file
    :return: most common non ascii char
    """
    list_of_ascii = set(string.ascii_letters)
    count = Counter()
    with open(file_path, encoding="unicode-escape") as f:
        for line in f:
            for char in line:
                if char not in list_of_ascii:
                    count[char] += 1
    return count.most_common()[0][0]
