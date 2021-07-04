import pytest
from homework4.task1.read_file.read_file import read_magic_number


@pytest.mark.parametrize("value", ["1", "2", "1.5"])
def test_create_file_and_read_line_true(tmp_path, value):
    path = tmp_path / "file_with_true_line.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is True


@pytest.mark.parametrize("value", ["3", "7", "10.0"])
def test_create_file_and_read_line_false(tmp_path, value):
    path = tmp_path / "file_with_false_line.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is False


def test_path_does_not_exists():
    path = "/home/one/lose"
    with pytest.raises(ValueError, match=f"Path: {path} does not exists"):
        read_magic_number(path)


@pytest.mark.parametrize("value", ["non", "dfdf", "2df2"])
def test_first_string_is_not_a_number(tmp_path, value):
    path = tmp_path / "file_with_false_type_of_line.txt"
    path.write_text(value)
    with pytest.raises(ValueError, match=f"first line has type {type(value)}"):
        read_magic_number(path)
