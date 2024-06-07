from django import forms
from vehicle.models import Vehicle

from .models import CargoWaybill, Waybill


class DateInput(forms.DateInput):
    input_type = "date"


class WaybillForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)

    class Meta:
        model = Waybill
        fields = ["driver", "mileage", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)

        super(WaybillForm, self).__init__(*args, **kwargs)

        if instance:
            self.initial["created_at"] = instance.created_at
            self.initial["vehicle"] = Vehicle.objects.get(pk=instance.vehicle.pk)


class CargoWaybillForm(forms.ModelForm):
    class Meta:
        model = CargoWaybill
        fields = ["product", "cost"]
