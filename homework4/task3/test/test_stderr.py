import sys

import pytest

from homework4.task3.stderr.stderr import my_precious_logger


def test_my_logger_err_output(capsys):
    my_precious_logger("error: first_try")
    captured = capsys.readouterr()
    assert captured.err == "error: first_try\n"
    assert captured.out == ""


def test_my_logger_out_output(capsys):
    my_precious_logger("Success")
    captured = capsys.readouterr()
    assert captured.out == "Success\n"
    assert captured.err == ""
