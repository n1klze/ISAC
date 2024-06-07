from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from vehicle.models import Auxiliary, Bus, Taxi, Truck

from .forms import GarageForm
from .models import Garage


# Create your views here.
def garage_list(request):
    garages = Garage.objects.all()
    return render(request, "garage/garage_list.html", {"garages": garages})


def garage_detail(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    trucks = Truck.objects.filter(garage=garage.pk)
    buses = Bus.objects.filter(garage=garage.pk)
    taxis = Taxi.objects.filter(garage=garage.pk)
    auxiliaries = Auxiliary.objects.filter(garage=garage.pk)
    context = {
        "garage": garage,
        "trucks": trucks,
        "buses": buses,
        "taxis": taxis,
        "auxiliaries": auxiliaries,
    }
    return render(request, "garage/garage_detail.html", context)


def garage_add(request):
    if request.method == "POST":
        form = GarageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("garage_list")
    else:
        form = GarageForm()
    return render(request, "garage/garage_form.html", {"form": form})


def garage_edit(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    if request.method == "POST":
        form = GarageForm(request.POST, instance=garage)
        if form.is_valid():
            form.save()
            return redirect("garage_list")
    else:
        form = GarageForm(instance=garage)
    return render(request, "garage/garage_form.html", {"form": form})


def garage_delete(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    if request.method == "POST":
        try:
            garage.delete()
        except ProtectedError:
            messages.error(request, "There are still cars in the garage.")
            return render(request, "garage/garage_delete.html", {"garage": garage})
        return redirect("garage_list")
    return render(request, "garage/garage_delete.html", {"garage": garage})
