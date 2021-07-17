"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Homework:
    """
    This class stores homework for student
    """

    def __init__(self, text_of_task: str, day_number: int):
        self.text = text_of_task
        self.deadline = datetime.timedelta(day_number)
        self.created = datetime.datetime.now()

    def is_active(self):
        """
        Checking status of homework
        :return: bool
        """
        return (self.deadline + self.created) > self.created


class DeadlineError(Exception):
    """Exception for deadline"""

    pass


class People_Name:
    """
    This simple class to store first and last names for student and teacher
    """

    def __init__(self, last_name_string: str, first_name_string: str):
        self.last_name = last_name_string
        self.first_name = first_name_string


class Student(People_Name):
    """
    Class which store information about students
    """

    def do_homework(self, homework: Homework, solution: str):
        """
        Save solution of homework
        :param homework: class Homework
        :param solution: str
        :return: object HomeworkResult or error
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")
            return None


class HomeworkResult:
    """
    This class save result of homework students
    """

    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Teacher(People_Name):
    """
    Class which store information about teacher
    """

    homework_done = defaultdict(list)

    @staticmethod
    def check_homework(homework_result: HomeworkResult) -> bool:
        """
        Function checking homework and if solution of homework more than 5 chars append
        this solution in defaultdict

        :param homework_result: object HomeworkResult
        :return: bool
        """
        if len(homework_result.solution) < 5:
            return False
        if (
            homework_result.solution
            not in Teacher.homework_done[homework_result.homework]
        ):
            Teacher.homework_done[homework_result.homework].append(
                homework_result.solution
            )
        return True

    @staticmethod
    def reset_results(result=None):
        """
        Function reset results of Homework in defaultdict
        :param result: Homework
        :return: dict
        """
        if result is None:
            Teacher.homework_done = defaultdict(list)
            return Teacher.homework_done
        if isinstance(result, Homework):
            del Teacher.homework_done[result]

    def create_homework(self, text_of_task: str, day_number: int):
        """
        Function which create homework object
        :param text_of_task: str
        :param day_number: int
        :return: object Homework
        """
        return Homework(text_of_task, day_number)
