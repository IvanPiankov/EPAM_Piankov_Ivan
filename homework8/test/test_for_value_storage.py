import pytest

from homework8.task1.value_storage import KeyValueStorage


def function_to_create_dir_and_file(text_for_writing, tmpdir):
    tmpdir_file = tmpdir.join("new_file")
    tmpdir_file.write(text_for_writing)
    return KeyValueStorage(str(tmpdir_file))


def test_value_storage(tmpdir):
    storage = function_to_create_dir_and_file(
        "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n", tmpdir
    )
    assert storage["name"] == "kek"
    assert storage.song == "shadilay"
    assert storage.power == 9001


def test_value_error_key(tmpdir):
    with pytest.raises(ValueError):
        function_to_create_dir_and_file("1=kek\n", tmpdir)


def test_value_error_getattr(tmpdir):
    storage = function_to_create_dir_and_file(
        "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n", tmpdir
    )
    with pytest.raises(ValueError):
        storage.kek1


def test_value_error_getitem(tmpdir):
    storage = function_to_create_dir_and_file(
        "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n", tmpdir
    )
    with pytest.raises(ValueError):
        storage["kek1"]
