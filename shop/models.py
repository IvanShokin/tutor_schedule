from django.db.models import Model, CharField, DateTimeField


class Lesson(Model):
    student = CharField(max_length=256)
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()
