import pytest
import pytest_timeout
from homework3.task2.slow_func.slow_func import *


@pytest.mark.timeout(60)
def test_slow_func():
    multiproc_Pool_function()
