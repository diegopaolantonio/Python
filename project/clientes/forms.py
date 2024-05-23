from django import forms

from . import models


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = models.Ubicacion
        fields = ["pais", "provincia"]


class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["RazonSocial", "Cuit", "Ubicacion_id"]
