from django.shortcuts import render
from random import randint as ran, choice as ch
import string
from django.http import JsonResponse


def password_generator(request):
    str1 = string.ascii_lowercase + string.ascii_uppercase + string.digits
    new_password = ''
    dict_password = {}
    for i in range(ran(10, 20)):
        new_password = new_password + ch(str1)
    dict_password['password'] = new_password
    return JsonResponse(dict_password)

