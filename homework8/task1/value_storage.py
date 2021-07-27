# We have a file that works as key-value storage, each line is represented as key and value separated by = symbol, example:
# name=kek last_name=top song_name=shadilay power=9001
# Values can be strings or integer numbers.
# If a value can be treated both as a number and a string, it is treated as number.
# Write a wrapper class for this key value storage that works like this:
# storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection items and as attributes.
# Example: storage['name'] # will be string 'kek' storage.song_name # will be 'shadilay' storage.power # will be integer 9001
# In case of attribute clash existing built-in attributes take precedence.
# In case when value cannot be assigned to an attribute (for example when there's a line 1=something) ValueError should be raised.
# File size is expected to be small, you are permitted to read it entirely into memory.

from string import ascii_letters


class KeyValueStorage:
    """
    Class save date in dict and have getattr and getitem
    """

    def __init__(self, path):
        self.path = path
        self.data = self._save_data_from_file()

    def _read_line_in_file(self):
        with open(self.path) as readable_file:
            for line in readable_file:
                yield line.rstrip("\n")

    def _save_data_from_file(self):
        data_for_save = {}
        for read_line in self._read_line_in_file():
            key, value = read_line.split("=")
            value = int(value) if value.isdigit() else value
            if key[0] not in ascii_letters:
                raise ValueError(
                    f"Value can't be assigned to an attribute for this key - {key}"
                )
            data_for_save[key] = value
        return data_for_save

    def __getitem__(self, item):
        value = self.data.get(item, None)
        if value is None:
            raise ValueError(f"Object has not in data this item: {item}")
        return value

    def __getattr__(self, item):
        attribute = self.data.get(item, None)
        if attribute is None:
            raise ValueError(f"Object has not in data this item: {item}")
        return attribute
