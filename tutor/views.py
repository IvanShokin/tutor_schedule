from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from tutor.models import Lesson, ProfileStudent
from tutor.serializers import LessonSerializer, \
    ProfileStudentResponseSerializer, ProfileStudentRequestSerializer


class LessonCreateView(ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ProfileStudentCreateView(ListCreateAPIView):
    serializer_class = ProfileStudentResponseSerializer
    queryset = ProfileStudent.objects.all()
