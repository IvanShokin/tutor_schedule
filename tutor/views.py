from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from tutor.models import Student, Lesson


def lessons(request):
    # TODO values_list
    a = {}
    for student in Student.objects.all():
        a[student.first_name] = []
        L1 = student.lesson.filter(start_datetime__iso_week_day__gte=1) & student.lesson.filter(
            start_datetime__iso_week_day__lte=7)
        for lesson in L1.values_list('start_datetime', 'end_datetime'):
            datetime_list = [
                lesson[0].strftime("%Y %m %d %H:%M"),
                lesson[1].strftime("%Y %m %d %H:%M")
            ]
            a[student.first_name].append(datetime_list)
    return JsonResponse(a)


def index(request):
    lesson1 = Lesson.objects.all()
    return render(request, "index.html", {'lessons': lesson1})


def create(request):
    if request.method == 'POST':
        student = Student()
        student.first_name = request.POST.get('first_name')
        student.save()
        lesson = Lesson(student=student, start_datetime=request.POST.get('start_datetime'), end_datetime=request.POST.get('end_datetime'))
        lesson.save()
    return HttpResponseRedirect("/")