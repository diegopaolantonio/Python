from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Area)
admin.site.register(models.Personal)