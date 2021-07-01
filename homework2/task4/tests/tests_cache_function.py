import pytest

from homework2.task4.cache_function.cache_function import cache


@pytest.fixture
def test_add_finction():
    def f_add(a, b):
        return a + b

    return f_add


def test_cache_true(test_add_finction):
    cache_true = cache(test_add_finction)
    first_start = cache_true(10, 10)
    second_start = cache_true(10, 10)
    assert first_start == second_start


def test_cache_fasle(test_add_finction):
    cache_true = cache(test_add_finction)
    first_start = cache_true(11, 10)
    second_start = cache_true(13, 10)
    assert not first_start == second_start
