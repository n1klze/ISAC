import datetime

from django import forms

from .models import Auxiliary, Bus, Taxi, Truck


class DateInput(forms.DateInput):
    input_type = "date"


class TruckForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of receiving",
    )

    class Meta:
        model = Truck
        fields = ["brand", "garage", "capacity"]


class BusForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of receiving",
    )

    class Meta:
        model = Bus
        fields = ["brand", "garage", "passenger_capacity"]


class TaxiForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of receiving",
    )

    class Meta:
        model = Taxi
        fields = ["brand", "garage", "passenger_capacity"]


class AuxiliaryForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of receiving",
    )

    class Meta:
        model = Auxiliary
        fields = ["brand", "garage", "description"]


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
