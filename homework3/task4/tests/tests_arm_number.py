import pytest
from homework3.task4.arm_num.arm_num import is_armstrong


@pytest.mark.parametrize(
    ["integer", "expected_result"], [(-1, False), (10, False),],
)
def test_check_false_result_is_arm(integer: int, expected_result: bool):
    result = is_armstrong(integer)
    assert result == expected_result


@pytest.mark.parametrize(
    ["integer", "expected_result"], [(153, True), (0, True), (1, True),],
)
def test_check_true_result_is_arm(integer: int, expected_result: bool):
    result = is_armstrong(integer)
    assert result == expected_result
