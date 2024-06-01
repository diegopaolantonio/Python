from django.db import models
from clientes.models import Cliente


class Proyecto(models.Model):
    Nombre = models.CharField(max_length=100)
    Cliente = models.OneToOneField(Cliente, on_delete=models.DO_NOTHING, related_name="proyecto_cliente", null=True, blank=True)
    Pais = models.CharField(max_length=100, null=True, blank=True)
    FechaInicio = models.DateField()
    FechaFin = models.DateField(null=True, blank=True)
    Estado = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Nombre} - {self.Pais}"
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
