"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:
@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:
@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead
f()
? 1
'1'
 f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
 f()
? 2
'2'
"""

from typing import Callable


def cache(times: int) -> Callable:
    """
    Give out cached value up to times number only.
    :param func: integer
    :return: cached
    """
    if not isinstance(times, int):
        raise TypeError("times should be integer")

    def cache_decorator(func: Callable):
        if times == 0:
            return func
        # create a dict to store the value and result of the function in it
        cache_time = {}  # is's look like {function_param : [result_func, cache_timer]}
        cache_timer = 0

        def memo(*args):
            nonlocal cache_time
            nonlocal cache_timer

            if args not in cache_time:
                cache_timer = 0
                cache_time[args] = [func(*args), cache_timer]
            elif cache_time[args][1] == times:
                del cache_time[args]
            else:
                cache_time[args][1] += 1
            return cache_time[args][0]

        return memo

    return cache_decorator
