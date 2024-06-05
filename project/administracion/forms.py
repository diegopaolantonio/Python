from django import forms

from . import models


class GastoForm(forms.ModelForm):
    class Meta:
        model = models.Gasto
        fields = [
            "Referencia",
            "FechaEmision",
            "FechaVencimiento",
            "Moneda",
            "Monto",
            "Detalle",
        ]


class FacturaForm(forms.ModelForm):
    class Meta:
        model = models.Factura
        fields = [
            "Numero",
            "Proyecto",
            "FechaEmision",
            "FechaVencimiento",
            "Moneda",
            "Monto",
            "Detalle",
        ]
