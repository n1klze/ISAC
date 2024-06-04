import datetime

from django import forms
from vehicle.models import Vehicle
from workers.models import Worker

from .models import Detail, Repair


class DateInput(forms.DateInput):
    input_type = "date"


class RepairForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=DateInput(format="%d/%m/%Y"),
        initial=datetime.date.today,
        label="Date of repair",
    )
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), required=False)

    class Meta:
        model = Repair
        fields = ["created_at"]


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ["repair", "name", "cost", "amount"]
