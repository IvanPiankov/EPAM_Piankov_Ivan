import datetime

import pytest

import homework5.task1.oop_1 as task1


def test_teacher_name():
    teacher = task1.Teacher("Daniil", "Shadrin")
    assert teacher.last_name == "Daniil"


def test_student_name():
    student = task1.Student("Roman", "Petrov")
    assert student.first_name == "Petrov"


def test_teacher_homework():
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    assert expired_homework.text == "Learn functions"
    assert expired_homework.deadline == datetime.timedelta(0)


def test_for_time_created(monkeypatch):
    class Time_Deadline:
        def __init__(self, *args):
            self.created = datetime.datetime(2019, 5, 26, 16, 44, 30)

    monkeypatch.setattr(task1, "Homework", Time_Deadline)
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    assert expired_homework.created == datetime.datetime(2019, 5, 26, 16, 44, 30)


def test_deadline_homework():
    create_homework_too = task1.Teacher("Daniil", "Shadrin").create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(5)


def test_homework_late_student():
    create_homework_too = task1.Teacher("Daniil", "Shadrin").create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    student_1 = task1.Student("Roman", "Petrov")
    assert isinstance(student_1.do_homework(oop_homework), task1.Homework)


def test_for_homework_none():
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    student_1 = task1.Student("Roman", "Petrov")
    assert student_1.do_homework(expired_homework) is None


def test_for_homework_late(capsys):
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    student_1 = task1.Student("Roman", "Petrov")
    student_1.do_homework(expired_homework)
    captur = capsys.readouterr()
    assert captur.out == "You are late\n"
