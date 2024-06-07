import datetime

from django import forms

from .models import Auxiliary, Bus, Taxi, Truck


class DateInput(forms.DateInput):
    input_type = "date"


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ["brand", "garage", "capacity", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of receiving"}


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ["brand", "garage", "passenger_capacity", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of receiving"}


class TaxiForm(forms.ModelForm):
    class Meta:
        model = Taxi
        fields = ["brand", "garage", "passenger_capacity", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of receiving"}


class AuxiliaryForm(forms.ModelForm):
    class Meta:
        model = Auxiliary
        fields = ["brand", "garage", "description", "created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of receiving"}


class MileageRequestForm(forms.ModelForm):
    date_from = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="From",
    )
    date_to = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="To",
    )
