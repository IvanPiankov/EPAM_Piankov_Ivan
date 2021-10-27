from typing import List

import pytest

from homework9.task1.merge_integer import merge_sorted_files


@pytest.mark.parametrize(
    ["file1", "file2", "expected_result"],
    [
        ("1\n3\n5", "2\n4\n6", [1, 2, 3, 4, 5, 6]),
        ("", "", []),
        ("", "1", [1]),
    ],
)
def test_merge_sorted_files(file1: str, file2: str, expected_result: List, tmpdir):
    tmdf1 = tmpdir.join("tmdf1.txt")
    tmdf1.write(file1)
    tmdf2 = tmpdir.join("tmdf2.txt")
    tmdf2.write(file2)
    actual_result = list(merge_sorted_files([tmdf1, tmdf2]))
    assert actual_result == expected_result


def test_merge_file_error(tmpdir):
    with pytest.raises(ValueError):
        tmdf1 = tmpdir.join("tmdf1.txt")
        tmdf1.write("zrada")
        tmdf2 = tmpdir.join("tmdf2.txt")
        tmdf2.write("peremoga")
        list(merge_sorted_files([tmdf1, tmdf2]))
