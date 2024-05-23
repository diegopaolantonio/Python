from django import forms

from . import models


class AreaForm(forms.ModelForm):
    class Meta:
        model = models.Area
        fields = ["nombre", "pais"]


class PersonalForm(forms.ModelForm):
    class Meta:
        model = models.Personal
        fields = ["Nombre", "Apellido", "DNI" ,"Area_id"]
