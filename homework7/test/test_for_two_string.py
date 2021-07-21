import pytest

from homework7.task2.two_strings import backspace_compare, to_list


@pytest.mark.parametrize(
    ["first_string", "second_string", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("", "", True),
        ("a#c", "b", False),
        ("####", "####", True),
    ],
)
def test_for_two_stringe_equel(
    first_string: str, second_string: str, expected_result: bool
):
    assert backspace_compare(first_string, second_string) == expected_result
