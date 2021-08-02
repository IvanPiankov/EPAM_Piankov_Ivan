import sqlite3

import pytest

from homework8.task2.sql_class_table_data import TableData

example_data = TableData(database_name="example.sqlite", table_name="presidents")


def test_check_len_feature():
    assert len(example_data) == 3


def test_check_getitem():
    assert example_data["Yeltsin"] == {
        "name": "Yeltsin",
        "age": 999,
        "country": "Russia",
    }


def test_contains_in_db():
    assert "Yeltsin" in example_data and "Putin" not in example_data


def test_iter_next_method():
    table_with_ex_data = []
    for i in example_data:
        table_with_ex_data.append(i["name"])
    assert table_with_ex_data == ["Yeltsin", "Trump", "Big Man Tyrone"]


def test_db_not_exist():
    with pytest.raises(FileNotFoundError):
        TableData(database_name="empty.sqlite", table_name="presidents")


def test_table_not_exist():
    with pytest.raises(sqlite3.DatabaseError):
        TableData(database_name="example.sqlite", table_name="empty")


def test_item_not_exist():
    with pytest.raises(KeyError):
        example_data["Putin"]
