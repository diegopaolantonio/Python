from django.db import models
from clientes.models import Cliente


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.DO_NOTHING,
        related_name="proyecto_cliente",
        null=True,
        blank=True,
    )
    pais = models.CharField(max_length=100, null=True, blank=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}"

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
