"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function returns N FizzBuzz numbers

    Tests for this function:

    >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    >>> fizzbuzz(0)
    Traceback (most recent call last):
    ...
    ValueError: n should be >= 1


    :param n: number
    :return: list with FizzBuzz numbers
    """
    if n <= 0:
        raise ValueError("n should be >= 1")

    fizz_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizz_list.append("fizzbuzz")
        elif i % 3 == 0:
            fizz_list.append("fizz")
        elif i % 5 == 0:
            fizz_list.append("buzz")
        else:
            fizz_list.append(str(i))

    return fizz_list
