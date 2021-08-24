# Generated by Django 3.2.6 on 2021-08-20 15:20


from django.db import migrations


def add_teacher(apps, schema_editor):
    Teacher = apps.get_model("migrations", "Teacher")
    Teacher.objects.bulk_create(
        [
            Teacher(first_name="Vity", last_name="Top"),
            Teacher(first_name="Ivan", last_name="Krot"),
            Teacher(first_name="Eva", last_name="New"),
        ]
    )


def add_student(apps, schema_editor):
    Student = apps.get_model("migrations", "Student")
    Student.objects.bulk_create(
        [
            Student(first_name="Moy", last_name="Philips"),
            Student(first_name="Row", last_name="Feel"),
            Student(first_name="Good", last_name="Food"),
        ]
    )


def add_homework(apps, schema_editor):
    Homework = apps.get_model("migrations", "Homework")
    Homework.objects.bulk_create(
        [
            Homework(text="Odin", teacher_id=1, student_id=1),
            Homework(text="Dva", teacher_id=2, student_id=2),
            Homework(text="Tri", teacher_id=3, student_id=3),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("migrations", "initial"),
    ]

    operations = [
        migrations.RunPython(add_teacher),
        migrations.RunPython(add_student),
        migrations.RunPython(add_homework),
    ]
