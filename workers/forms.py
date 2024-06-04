import datetime

from django import forms
from vehicle.models import Vehicle

from .models import Assembler, Driver, Mechanic, Technician, Welder


class DateInput(forms.DateInput):
    input_type = "date"


class DriverForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)

    class Meta:
        model = Driver
        fields = ["name", "brigade"]


class MechanicForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )

    class Meta:
        model = Mechanic
        fields = ["name", "brigade"]


class TechnicianForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )

    class Meta:
        model = Technician
        fields = ["name", "brigade"]


class WelderForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )

    class Meta:
        model = Welder
        fields = ["name", "brigade", "welding_machine"]


class AssemblerForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of employment",
    )

    class Meta:
        model = Assembler
        fields = ["name", "brigade", "assembly_machine"]
