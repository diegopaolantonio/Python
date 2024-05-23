from django.db import models


class Ubicacion(models.Model):
    pais = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pais} - {self.provincia}"
    
    class Meta:
        verbose_name = "ubicacion"
        verbose_name_plural = "ubicaciones"

class Cliente(models.Model):
    RazonSocial = models.CharField(max_length=100, unique=True)
    Cuit = models.CharField(max_length=50, null=True, blank=True)
    Ubicacion_id = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ubicacion de origen")

    def __str__(self) -> str:
        return self.RazonSocial
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
