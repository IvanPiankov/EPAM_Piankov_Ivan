"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from typing import Callable


def outher_function(other_func: Callable):
    """get function for decorate"""

    def function_decorate(any_other_function: Callable):
        """get function for wrapper"""

        def wrap(*args, **kwargs):
            wrap.__doc__ = other_func.__doc__
            wrap.__name__ = other_func.__name__
            wrap.__original_func = other_func
            return any_other_function(*args, **kwargs)

        return wrap

    return function_decorate


def print_result(func):
    # Place for new decorator
    @outher_function(other_func=func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
