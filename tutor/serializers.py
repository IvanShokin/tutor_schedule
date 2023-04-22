from rest_framework import serializers

from tutor.models import Lesson, ProfileStudent


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['student', 'teacher', 'start_datetime', 'end_datetime', 'age',
                  'price_lesson', 'home_work', 'lesson_topic', 'theory']


class ProfileStudentRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProfileStudentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStudent
        fields = ['pk']
