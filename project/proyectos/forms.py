from django import forms

from . import models


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = ["Nombre", "Cliente", "Pais", "FechaInicio", "FechaFin", "Estado"]
