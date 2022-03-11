from atexit import register
import site
from django.contrib import admin
from .models import course,std

# Register your models here.


admin.site.register(course)
admin.site.register(std)