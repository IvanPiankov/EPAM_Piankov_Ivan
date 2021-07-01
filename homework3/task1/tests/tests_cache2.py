import random

import pytest
from homework3.task1.cache_2.cache_2 import cache


@cache(times=2)
def random_choice_func(a, b, c):
    return random.randrange(a, b, c)


def test_not_integer_error():
    with pytest.raises(TypeError, match="times should be integer"):
        cache("a")


def test_of_random_choice_function():
    first_result = random_choice_func(5, 6, 1)
    second_result = random_choice_func(5, 6, 1)
    third_result = random_choice_func(5, 6, 1)

    assert (first_result == second_result) != third_result
