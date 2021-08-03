import pytest

from homework9.task2.context_manager import Suppressor, suppressor


def test_positive_class_suppress_index_error():
    with Suppressor(IndexError):
        _ = [][2]


def test_positive_dec_suppress_index_error():
    with suppressor(IndexError):
        _ = [][2]


def test_negative_dec_suppress_index_error():
    with pytest.raises(IndexError):
        with suppressor(ValueError):
            _ = [][2]


def test_negative_class_suppress_index_error():
    with pytest.raises(IndexError):
        with Suppressor(ValueError):
            _ = [][2]
