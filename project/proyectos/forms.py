from django import forms

from . import models


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = [
            "nombre",
            "cliente",
            "pais",
            "fechaInicio",
            "fechaFin",
            "estado",
        ]
