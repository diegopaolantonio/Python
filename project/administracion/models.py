from django.db import models
from proyectos.models import Proyecto


class Factura(models.Model):
    Numero = models.DecimalField(max_digits=20, decimal_places=0, unique=True)
    Proyecto = models.ManyToManyField(Proyecto)
    # OneToOneField(Proyecto, on_delete=models.DO_NOTHING, related_name="factura_proyecto", null=True, blank=True)
    FechaEmision = models.DateField()
    FechaVencimiento = models.DateField(null=True, blank=True)
    Moneda = models.CharField(max_length=10, default="USD")
    Monto = models.FloatField()
    Detalle = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Numero} - {self.Moneda}{self.Monto}"
    
    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"

class Gasto(models.Model):
    Referencia = models.CharField(max_length=50)
    FechaEmision = models.DateField()
    FechaVencimiento = models.DateField(null=True, blank=True)
    Moneda = models.CharField(max_length=10, null=True, blank=True)
    Monto = models.FloatField()
    Detalle = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Referencia} - {self.FechaEmision}"
    
    class Meta:
        verbose_name = "gasto"
        verbose_name_plural = "gastos"