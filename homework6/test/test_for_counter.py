import pytest

from homework6.task1.counter import instances_counter


@instances_counter
class User:
    pass


def test_check_zero_result_is_counter():
    result = User.get_created_instances()
    assert result == 0


def test_check_int_result_is_counter():
    user, _, _ = User(), User(), User()
    result = user.get_created_instances()
    assert result == 3


def test_check_after_reset_result_is_counter():
    result = User.reset_instances_counter()
    assert (result == 3) and (User.get_created_instances() == 0)
