from django.contrib import admin

from .models import Object, Student, Estimation

# Register your models here.

admin.site.register(Object)
admin.site.register(Student)
admin.site.register(Estimation)