from django.http import JsonResponse

from tutor.models import Student



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