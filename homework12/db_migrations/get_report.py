import os

PROJECT_NAME = "db_migrations"


def main():
    import csv

    from db_migrations.migrations.models import Homework, Student

    column_names = ["Teacher name", "Student name"]

    with open("my_report.csv", "w") as csv_file:
        result_objects = Homework.objects.all()
        writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(column_names)
        for object in result_objects:
            student_obj = Student.objects.get(id=object.student_id)
            student_field = student_obj.first_name + " " + student_obj.last_name
            teacher_obj = Homework.objects.get(id=object.teacher_id)
            teacher_field = teacher_obj.first_name + " " + teacher_obj.last_name
            row = [teacher_field, student_field]
            writer.writerow(row)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_NAME)
    import django

    django.setup()
    main()
