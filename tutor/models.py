import datetime
from pathlib import Path

from django.db.models import Model, CharField, ForeignKey, DateTimeField, CASCADE, FileField


class Student(Model):
    first_name = CharField(max_length=256)


class Lesson(Model):
    student = ForeignKey(Student, related_name='lesson', on_delete=CASCADE)
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()
    fole = FileField(upload_to=Path(str(datetime.date.today()), ''))
