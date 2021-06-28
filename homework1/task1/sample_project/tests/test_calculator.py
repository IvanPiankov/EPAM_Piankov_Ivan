from pathlib import Path

import pytest
from homework1.task1.sample_project.calculator.calc import check_power_of_2

print(Path.cwd())


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero():
    """Testing that number is zero"""
    assert not check_power_of_2(0)


def test_one():
    """Testing that number is zero"""
    assert not check_power_of_2(1)
