import datetime

from django import forms
from vehicle.models import Vehicle

from .models import CargoWaybill, Waybill


class DateInput(forms.DateInput):
    input_type = "date"


class WaybillForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)

    class Meta:
        model = Waybill
        fields = ["driver", "mileage"]


class CargoWaybillForm(forms.ModelForm):
    class Meta:
        model = CargoWaybill
        fields = ["product", "cost", "waybill"]
