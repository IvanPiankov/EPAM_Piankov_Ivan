"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

with supressor(IndexError):
...    [][2]
"""

import contextlib


class Suppressor:
    """
    Class take exception and suppress it
    """

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is self.exception


@contextlib.contextmanager
def suppressor(exception):
    """
    Function take exception and suppress it
    :param exception: type of exception
    :return: -
    """
    try:
        yield
    except exception:
        pass
    finally:
        pass
