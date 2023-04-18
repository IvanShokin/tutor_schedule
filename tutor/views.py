from django.http import HttpRequest
from django.shortcuts import render

from tutor.models import Lesson, ProfileStudent


def index(request):
    lessons_of_the_current_week = Lesson.objects.filter(
        start_datetime__iso_week_day__gte=1, start_datetime__iso_week_day__lte=7)
    return render(request, "tutor/index.html", {'lessons': lessons_of_the_current_week})


def student(request: HttpRequest, student_id):
    students = ProfileStudent.objects.all()

    if request.method == 'DELETE':
        # student_id = json.loads(request.body.decode()).get('student_id')
        ProfileStudent.objects.get(id=student_id).delete()
    return render(request=request, template_name="tutor/student.html", context={'students': students})

