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
    razonSocial = models.CharField(max_length=100, unique=True)
    cuit = models.CharField(max_length=50, null=True, blank=True)
    ubicacion_id = models.ForeignKey(
        Ubicacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ubicacion de origen",
    )
    avatar = models.ImageField(upload_to="avatarCliente/", null=True, blank=True)

    def __str__(self) -> str:
        return self.razonSocial

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
