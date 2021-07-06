"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime


class Homework:
    def __init__(self, text_of_task: str, day_number: int):
        self.text = text_of_task
        self.deadline = datetime.timedelta(day_number)
        self.created = datetime.datetime.now()

    def is_active(self):
        if (self.deadline + self.created) > self.created:
            return True
        else:
            return False


class Student:
    def __init__(self, last_name_string: str, first_name_string: str):
        self.last_name = last_name_string
        self.first_name = first_name_string

    def do_homework(self, homework: Homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None


class Teacher:
    def __init__(self, last_name_string: str, first_name_string: str):
        self.last_name = last_name_string
        self.first_name = first_name_string

    def create_homework(self, text_of_task: str, day_number: int):
        return Homework(text_of_task, day_number)
