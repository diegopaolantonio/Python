from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Factura)
admin.site.register(models.Gasto)