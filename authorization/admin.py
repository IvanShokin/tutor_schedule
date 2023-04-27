from django.contrib import admin

from authorization.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)