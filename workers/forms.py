from django import forms
from vehicle.models import Vehicle

from .models import Assembler, Driver, Mechanic, Technician, Welder


class DateInput(forms.DateInput):
    input_type = "date"


class DriverForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)

    class Meta:
        model = Driver
        fields = ["name", "brigade", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)

        super(DriverForm, self).__init__(*args, **kwargs)

        if instance:
            self.initial["created_at"] = instance.created_at
            self.initial["vehicle"] = Vehicle.objects.get(pk=instance.vehicle.pk)


class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ["name", "brigade", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}


class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ["name", "brigade", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}


class WelderForm(forms.ModelForm):
    class Meta:
        model = Welder
        fields = ["name", "brigade", "welding_machine", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}


class AssemblerForm(forms.ModelForm):
    class Meta:
        model = Assembler
        fields = ["name", "brigade", "assembly_machine", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of employment"}
