from django.db import models


class Proyecto(models.Model):
    Nombre = models.CharField(max_length=100)
    Pais = models.CharField(max_length=100, null=True, blank=True)
    FechaInicio = models.DateField()
    FechaFin = models.DateField(null=True, blank=True)
    Estado = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Nombre} - {self.Pais}"
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
