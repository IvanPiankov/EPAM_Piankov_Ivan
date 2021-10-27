import pytest

from homework9.task3.count_tokenizer import universal_file_counter


def create_file(tmpdir):
    tmdf1 = tmpdir.join("tmdf1.txt")
    tmdf1.write("1\n3\n5")
    tmdf2 = tmpdir.join("tmdf2.txt")
    tmdf2.write("2\n4\n6")


def test_positive_path_dir(tmpdir):
    create_file(tmpdir)
    actual_result = universal_file_counter(tmpdir, "txt")
    assert actual_result == 6


def test_positive_path_dir_tokenizer(tmpdir):
    create_file(tmpdir)
    actual_result = universal_file_counter(tmpdir, "txt", str.split)
    assert actual_result == 6


def test_not_file(tmpdir):
    create_file(tmpdir)
    actual_result = universal_file_counter(tmpdir, "exe", str.split)
    assert actual_result == 0
