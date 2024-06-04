from django import forms

from .models import Brigade, District, Workshop


class BrigadeForm(forms.ModelForm):
    class Meta:
        model = Brigade
        fields = ["brigadier", "district"]


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ["master", "workshop"]


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ["head"]
