from django.http import JsonResponse, HttpResponse

from shop.models import Lesson, Student


def lessons(request):
    a = {}
    for entry in Student.objects.values():
        a[entry['first_name']] = list(i['start_datetime'] for i in Lesson.objects.filter(student_id=entry['id']).values())
    return JsonResponse(a)