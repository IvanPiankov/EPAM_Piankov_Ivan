import pytest
from homework4.task5.fib_bazz_opt.fib_bazz_opt import fizzbuzz


def test_right_output():
    expected_result = ["1"]
    actual_result = list(fizzbuzz(1))
    assert actual_result == expected_result


def test_right_output_more_number():
    expected_result = ["1", "2", "fizz", "4", "buzz"]
    actual_result = list(fizzbuzz(5))
    assert actual_result == expected_result


def test_right_output_number_15():
    expected_result = [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
    ]
    actual_result = list(fizzbuzz(15))
    assert actual_result == expected_result


def test_false_output():
    with pytest.raises(ValueError, match="n should be >= 1"):
        list(fizzbuzz(0))
