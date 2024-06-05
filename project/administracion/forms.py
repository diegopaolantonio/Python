from django import forms

from . import models


class GastoForm(forms.ModelForm):
    class Meta:
        model = models.Gasto
        fields = [
            "referencia",
            "fechaEmision",
            "fechaVencimiento",
            "moneda",
            "monto",
            "detalle",
        ]


class FacturaForm(forms.ModelForm):
    class Meta:
        model = models.Factura
        fields = [
            "numero",
            "proyecto",
            "fechaEmision",
            "fechaVencimiento",
            "moneda",
            "monto",
            "detalle",
        ]
