"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from typing import Any, Callable


def instances_counter(cls: Callable) -> Any:
    """Some code"""

    class Inst_count(cls):
        """
        This decorator for class which
        have specific method get_created_instances and reset_instances_counter
        """

        counter = 0

        def __init__(self, *args, **kwargs):
            Inst_count.counter += 1
            super(Inst_count, self).__init__(*args, **kwargs)

        @staticmethod
        def get_created_instances():
            return Inst_count.counter

        @staticmethod
        def reset_instances_counter():
            count_before_zeroing = Inst_count.counter
            Inst_count.counter = 0
            return count_before_zeroing

    return Inst_count
