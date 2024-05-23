from django import forms

from . import models


class GastosForm(forms.ModelForm):
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


class FacturasForm(forms.ModelForm):
    class Meta:
        model = models.Factura
        fields = [
            "Numero",
            "Cliente",
            "Proyecto",
            "FechaEmision",
            "FechaVencimiento",
            "Moneda",
            "Monto",
            "Detalle",
        ]
