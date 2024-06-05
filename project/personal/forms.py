from django import forms

from . import models


class AreaForm(forms.ModelForm):
    class Meta:
        model = models.Area
        fields = [
            "nombre",
            "sede",
        ]


class PersonalForm(forms.ModelForm):
    class Meta:
        model = models.Personal
        fields = [
            "usuario",
            "nombre",
            "apellido",
            "dni",
            "area_id",
            "avatar",
        ]
