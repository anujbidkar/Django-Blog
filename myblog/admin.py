from django.contrib import admin

# Register your models here.

from .models import Myblog

admin.site.register(Myblog)