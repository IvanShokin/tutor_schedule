from django.http import JsonResponse

from tutor.models import Student


def lessons(request):
    # TODO values_list
    a = {}
    for student in Student.objects.all():
        a[student.first_name] = []
        for lesson in student.lesson.values_list('start_datetime', 'end_datetime'):
            datetime_list = [
                lesson[0].strftime("%Y %m %d %H:%M"),
                lesson[1].strftime("%Y %m %d %H:%M")
            ]
            a[student.first_name].append(datetime_list)
    return JsonResponse(a)