from django import forms
from vehicle.models import Vehicle
from workers.models import Worker

from .models import Detail, Repair


class DateInput(forms.DateInput):
    input_type = "date"


class RepairForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=True)
    worker = forms.ModelChoiceField(
        queryset=Worker.objects.filter(driver__isnull=True), required=True
    )

    class Meta:
        model = Repair
        fields = ["created_at"]
        widgets = {"created_at": DateInput(format="%d/%m/%Y")}
        labels = {"created_at": "Date of repair"}

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)

        super(RepairForm, self).__init__(*args, **kwargs)

        if instance:
            self.initial["created_at"] = instance.created_at
            self.initial["vehicle"] = Vehicle.objects.get(pk=instance.vehicle_id)
            self.initial["worker"] = Worker.objects.get(pk=instance.worker_id)


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ["repair", "name", "cost", "amount"]
