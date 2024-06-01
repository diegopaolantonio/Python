from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.pais}"
    
    class Meta:
        verbose_name = "area"
        verbose_name_plural = "areas"

class Personal(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100, null=True, blank=True)
    DNI = models.DecimalField(max_digits=20, decimal_places=0, unique=True)
    Area_id = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Area de trabajo")
    Usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name="usuario", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Apellido}, {self.Nombre}"
    
    class Meta:
        verbose_name = "personal"
        verbose_name_plural = "personal"
