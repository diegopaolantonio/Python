from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    sede = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}"

    class Meta:
        verbose_name = "area"
        verbose_name_plural = "areas"


class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.DecimalField(max_digits=20, decimal_places=0, unique=True)
    area_id = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Area de trabajo",
    )
    usuario = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name="usuario", null=True, blank=True
    )
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "personal"
        verbose_name_plural = "personal"
