from django.http import JsonResponse

from shop.models import Lesson


def lessons(request):
    return JsonResponse([entry for entry in Lesson.objects.values()], safe=False)
