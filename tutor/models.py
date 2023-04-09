from django.db.models import Model, CharField, ForeignKey, DateTimeField, CASCADE


class Student(Model):
    first_name = CharField(max_length=256)


class Lesson(Model):
    student = ForeignKey(Student, related_name='lesson', on_delete=CASCADE)
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()

