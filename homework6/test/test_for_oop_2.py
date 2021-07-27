from collections import defaultdict

import pytest

from homework6.task2.oop_2 import *

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_not_homework_object():
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(good_student, "fff", "Solution")


def test_for_true_homework_result():
    assert opp_teacher.check_homework(result_1)
    assert opp_teacher.check_homework(result_2)
    assert not opp_teacher.check_homework(result_3)


def test_for_list_dic():
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_for_doing_homework_result():
    result = ["I have done this hw"]
    assert Teacher.homework_done[oop_hw] == result


def test_for_reset_result():
    assert Teacher.reset_results() == defaultdict(list)
