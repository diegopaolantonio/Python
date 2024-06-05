from django.db import models
from proyectos.models import Proyecto


class Factura(models.Model):
    numero = models.DecimalField(max_digits=20, decimal_places=0, unique=True)
    proyecto = models.ManyToManyField(Proyecto, blank=True)
    fechaEmision = models.DateField()
    fechaVencimiento = models.DateField(null=True, blank=True)
    moneda = models.CharField(max_length=10, default="USD")
    monto = models.FloatField()
    detalle = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.numero} - {self.moneda}{self.monto}"

    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"


class Gasto(models.Model):
    referencia = models.CharField(max_length=50)
    fechaEmision = models.DateField()
    fechaVencimiento = models.DateField(null=True, blank=True)
    moneda = models.CharField(max_length=10, default="USD")
    monto = models.FloatField()
    detalle = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.referencia} - {self.fechaEmision}"

    class Meta:
        verbose_name = "gasto"
        verbose_name_plural = "gastos"
