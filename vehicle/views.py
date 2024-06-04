from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from route.models import Route

from .forms import AuxiliaryForm, BusForm, TaxiForm, TruckForm
from .models import Auxiliary, Bus, Taxi, Truck, Vehicle


# Create your views here.
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicle/vehicle_list.html", {"vehicles": vehicles})


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    context = {"truck": vehicle}
    return render(request, "vehicle/vehicle_detail.html", context)


def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, "vehicle/truck/truck_list.html", {"trucks": trucks})


def truck_detail(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    drivers = truck.drivers.all()
    context = {"truck": truck, "drivers": drivers}
    return render(request, "vehicle/truck/truck_detail.html", context)


def truck_add(request):
    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.created_at = form.cleaned_data.get("created_at")
            truck.save()
            return redirect("truck_list")
    else:
        form = TruckForm()
    return render(request, "vehicle/truck/truck_add.html", {"form": form})


def truck_decommission(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        truck.modified_at = datetime.today()
        truck.is_decommissioned = 1
        truck.save()
        return redirect("truck_list")
    return render(request, "vehicle/truck/truck_decommission.html", {"truck": truck})


def taxi_list(request):
    taxis = Taxi.objects.all()
    return render(request, "vehicle/taxi/taxi_list.html", {"taxis": taxis})


def taxi_detail(request, pk):
    taxi = get_object_or_404(Taxi, pk=pk)
    drivers = taxi.drivers.all()
    route = Route.objects.get(pk=taxi.route.pk)
    context = {"taxi": taxi, "drivers": drivers, "route": route}
    return render(request, "vehicle/taxi/taxi_detail.html", context)


def taxi_add(request):
    if request.method == "POST":
        form = TaxiForm(request.POST)
        if form.is_valid():
            taxi = form.save(commit=False)
            taxi.created_at = form.cleaned_data.get("created_at")
            taxi.save()
            return redirect("taxi_list")
    else:
        form = TaxiForm()
    return render(request, "vehicle/taxi/taxi_add.html", {"form": form})


def bus_list(request):
    buses = Bus.objects.all()
    return render(request, "vehicle/bus/bus_list.html", {"buses": buses})


def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    drivers = bus.drivers.all()
    route = Route.objects.get(pk=bus.route.pk)
    context = {"bus": bus, "drivers": drivers, "route": route}
    return render(request, "vehicle/bus/bus_detail.html", context)


def bus_add(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.created_at = form.cleaned_data.get("created_at")
            bus.save()
            return redirect("bus_list")
    else:
        form = BusForm()
    return render(request, "vehicle/bus/bus_add.html", {"form": form})


def auxiliary_list(request):
    auxiliaries = Auxiliary.objects.all()
    return render(
        request, "vehicle/auxiliary/auxiliary_list.html", {"auxiliaries": auxiliaries}
    )


def auxiliary_detail(request, pk):
    auxiliary = get_object_or_404(Auxiliary, pk=pk)
    drivers = auxiliary.drivers.all()
    context = {"auxiliary": auxiliary, "drivers": drivers}
    return render(request, "vehicle/auxiliary/auxiliary_detail.html", context)


def auxiliary_add(request):
    if request.method == "POST":
        form = AuxiliaryForm(request.POST)
        if form.is_valid():
            auxiliary = form.save(commit=False)
            auxiliary.created_at = form.cleaned_data.get("created_at")
            auxiliary.save()
            return redirect("auxiliary_list")
    else:
        form = AuxiliaryForm()
    return render(request, "vehicle/auxiliary/auxiliary_add.html", {"form": form})


def mileage_request(request):
    if request.method == "POST":
        form = AuxiliaryForm(request.POST)
        if form.is_valid():
            auxiliary = form.save(commit=False)
            auxiliary.created_at = form.cleaned_data.get("created_at")
            auxiliary.save()
            return redirect("auxiliary_list")
    else:
        form = AuxiliaryForm()
    return render(request, "vehicle/auxiliary/auxiliary_add.html", {"form": form})
