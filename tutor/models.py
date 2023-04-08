from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=256)


class Lesson(models.Model):
    student = models.ForeignKey(Student, related_name='lesson', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

