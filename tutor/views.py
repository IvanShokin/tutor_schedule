from rest_framework.generics import ListCreateAPIView
from tutor.models import Lesson, ProfileStudent
from tutor.serializers import LessonSerializer, \
    ProfileStudentResponseSerializer


class LessonCreateView(ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ProfileStudentCreateView(ListCreateAPIView):
    serializer_class = ProfileStudentResponseSerializer
    queryset = ProfileStudent.objects.all()
