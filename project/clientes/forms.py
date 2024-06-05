from django import forms

from . import models


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = models.Ubicacion
        fields = [
            "pais",
            "provincia",
        ]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = [
            "razonSocial",
            "cuit",
            "ubicacion_id",
        ]
