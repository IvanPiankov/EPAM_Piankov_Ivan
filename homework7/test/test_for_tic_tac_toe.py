from typing import List

import pytest

from homework7.task3.tic_tac_toe import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        (([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]), "x wins!"),
        (([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "o"]]), "o wins!"),
        (([["o", "x", "o"], ["x", "x", "x"], ["-", "o", "-"]]), "x wins!"),
    ],
)
def test_tic_tac_check_winners(board: List[List], expected_result: str):
    assert tic_tac_toe_checker(board) == expected_result


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        (([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]), "unfinished!"),
        (([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]), "unfinished!"),
    ],
)
def test_tic_tac_check_unfinished(board: List[List], expected_result: str):
    assert tic_tac_toe_checker(board) == expected_result


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        (([["o", "x", "o"], ["x", "x", "o"], ["x", "o", "x"]]), "draw!"),
    ],
)
def test_tic_tac_check_unfinished(board: List[List], expected_result: str):
    assert tic_tac_toe_checker(board) == expected_result


def test_tic_tac_check_input_data_value_err():
    with pytest.raises(ValueError):
        tic_tac_toe_checker({("o", "x", "o"), str("hello"), ("x", "o", "x")})
