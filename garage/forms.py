from django import forms

from .models import Garage


class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ["address"]
