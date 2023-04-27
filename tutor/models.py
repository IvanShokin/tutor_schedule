from django.db.models import Model, IntegerField, DateTimeField, CASCADE, TextField, \
    CharField, ForeignKey, OneToOneField, ManyToManyField

from django.conf import settings


class ProfileTeacher(Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class ProfileStudent(Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE, primary_key=True)
    teachers = ManyToManyField(ProfileTeacher, related_name='students', through='Lesson')


class Lesson(Model):
    student = ForeignKey(ProfileStudent, related_name='lesson', on_delete=CASCADE)
    teacher = ForeignKey(ProfileTeacher, related_name='lesson', on_delete=CASCADE)
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()
    age = IntegerField(default=0)                             # возраст
    price_lesson = IntegerField(default=0)                    # цена занятия
    home_work = TextField(default='')                          # домашка
    lesson_topic = CharField(max_length=256, default='')       # тема урока
    theory = TextField(default='')                             # теория
