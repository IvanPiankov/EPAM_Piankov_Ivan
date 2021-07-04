import pytest
from homework4.task4.doc_string_test.doc_string_test import fizzbuzz


def test_right_output():
    expected_result = ["1"]
    actual_result = fizzbuzz(1)
    assert actual_result == expected_result


def test_false_output():
    with pytest.raises(ValueError, match="n should be >= 1"):
        fizzbuzz(0)
