"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Take four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero

    :param a: list A  with tuples
    :param b: list B  with tuples
    :param c: list C  with tuples
    :param d: list D  with tuples
    :return: numbers of tuples which sum equal zero
    """

    first_part = []
    for element_a in a:
        for element_b in b:
            first_part.append(element_b + element_a)

    second_part = []
    for element_c in c:
        for element_d in d:
            second_part.append(element_c + element_d)

    count = 0
    for numbers_first_part in first_part:
        for numbers_second_part in second_part:
            if (numbers_first_part + numbers_second_part) == 0:
                count += 1

    return count
