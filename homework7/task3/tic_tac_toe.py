"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function determine winners in tic-tac-toe game
    :param board: board with tic-tac-toe game
    :return: winners
    """
    if not all(isinstance(row, list) for row in board):
        raise ValueError("board should be List[List]")

    unfinished = "unfinished!"
    draw = "draw!"

    positions_groups = (
        [[(x, y) for y in range(3)] for x in range(3)]
        + [[(x, y) for x in range(3)] for y in range(3)]
        + [[(d, d) for d in range(3)]]
        + [[(2 - d, d) for d in range(3)]]
    )

    for positions in positions_groups:
        values = [board[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0] != "-":
            return f"{str(values[0]).lower()} wins!"
    if "-" in chain(*board):
        return unfinished
    return draw
