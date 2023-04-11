from django.http import HttpResponseRedirect
from django.shortcuts import render
from tutor.models import Student, Lesson


def index(request):
    lessons_of_the_current_week = Lesson.objects.filter(
        start_datetime__iso_week_day__gte=1, start_datetime__iso_week_day__lte=7)
    return render(request, "index.html", {'lessons': lessons_of_the_current_week})


def create(request):
    if request.method == 'POST':
        student = Student.objects.create(first_name=request.POST.get('first_name'))
        Lesson.objects.create(student=student, start_datetime=request.POST.get('start_datetime'), end_datetime=request.POST.get('end_datetime'))
    return HttpResponseRedirect("/")