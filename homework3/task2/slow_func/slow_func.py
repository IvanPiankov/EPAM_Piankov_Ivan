# Here's a not very efficient calculation function that calculates something important:
#
# import time
# import struct
# import random
# import hashlib
#
# def slow_calculate(value):
#     """Some weird voodoo magic calculations"""
#     time.sleep(random.randint(1,3))
#     data = hashlib.md5(str(value).encode()).digest()
#     return sum(struct.unpack('<' + 'B' * len(data), data))
# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute.
# Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.

import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Any


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def multiproc_Pool_function() -> Any:
    """
    Function which start slow_calculate function with using multiprocessing
    :return:result of slow_calculate function
    """
    with Pool(40) as pool:
        result = sum(pool.map(slow_calculate, range(500)))
    return result
