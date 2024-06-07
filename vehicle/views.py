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
    return render(request, "vehicle/truck/truck_form.html", {"form": form})


def truck_edit(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        form = TruckForm(request.POST, instance=truck)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.created_at = form.cleaned_data.get("created_at")
            truck.save()
            return redirect("truck_list")
    else:
        form = TruckForm(instance=truck)
    return render(request, "vehicle/truck/truck_form.html", {"form": form})


def truck_decommission(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        truck.modified_at = datetime.today()
        truck.is_decommissioned = True
        for driver in truck.drivers.all():
            driver.vehicle = None
            driver.save()
        truck.save()
        return redirect("truck_list")
    return render(request, "vehicle/truck/truck_decommission.html", {"truck": truck})


def taxi_list(request):
    taxis = Taxi.objects.all()
    return render(request, "vehicle/taxi/taxi_list.html", {"taxis": taxis})


def taxi_detail(request, pk):
    taxi = get_object_or_404(Taxi, pk=pk)
    drivers = taxi.drivers.all()
    if taxi.route:
        route = Route.objects.get(pk=taxi.route.pk)
    else:
        route = None
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
    return render(request, "vehicle/taxi/taxi_form.html", {"form": form})


def taxi_edit(request, pk):
    taxi = get_object_or_404(Taxi, pk=pk)
    if request.method == "POST":
        form = TaxiForm(request.POST, instance=taxi)
        if form.is_valid():
            taxi = form.save(commit=False)
            taxi.created_at = form.cleaned_data.get("created_at")
            taxi.save()
            return redirect("taxi_list")
    else:
        form = TaxiForm(instance=taxi)
    return render(request, "vehicle/taxi/taxi_form.html", {"form": form})


def taxi_decommission(request, pk):
    taxi = get_object_or_404(Taxi, pk=pk)
    if request.method == "POST":
        taxi.modified_at = datetime.today()
        taxi.is_decommissioned = True
        taxi.route = None
        for driver in taxi.drivers.all():
            driver.vehicle = None
            driver.save()
        taxi.save()
        return redirect("taxi_list")
    return render(request, "vehicle/taxi/taxi_decommission.html", {"taxi": taxi})


def bus_list(request):
    buses = Bus.objects.all()
    return render(request, "vehicle/bus/bus_list.html", {"buses": buses})


def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    drivers = bus.drivers.all()
    if bus.route:
        route = Route.objects.get(pk=bus.route.pk)
    else:
        route = None
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
    return render(request, "vehicle/bus/bus_form.html", {"form": form})


def bus_edit(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.created_at = form.cleaned_data.get("created_at")
            bus.save()
            return redirect("bus_list")
    else:
        form = BusForm(instance=bus)
    return render(request, "vehicle/bus/bus_form.html", {"form": form})


def bus_decommission(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        bus.modified_at = datetime.today()
        bus.is_decommissioned = True
        bus.route = None
        for driver in bus.drivers.all():
            driver.vehicle = None
            driver.save()
        bus.save()
        return redirect("bus_list")
    return render(request, "vehicle/bus/bus_decommission.html", {"bus": bus})


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
    return render(request, "vehicle/auxiliary/auxiliary_form.html", {"form": form})


def auxiliary_edit(request, pk):
    auxiliary = get_object_or_404(Auxiliary, pk=pk)
    if request.method == "POST":
        form = AuxiliaryForm(request.POST, instance=auxiliary)
        if form.is_valid():
            auxiliary = form.save(commit=False)
            auxiliary.created_at = form.cleaned_data.get("created_at")
            auxiliary.save()
            return redirect("auxiliary_list")
    else:
        form = AuxiliaryForm(instance=auxiliary)
    return render(request, "vehicle/auxiliary/auxiliary_form.html", {"form": form})


def auxiliary_decommission(request, pk):
    auxiliary = get_object_or_404(Auxiliary, pk=pk)
    if request.method == "POST":
        auxiliary.modified_at = datetime.today()
        auxiliary.is_decommissioned = True
        for driver in auxiliary.drivers.all():
            driver.vehicle = None
            driver.save()
        auxiliary.save()
        return redirect("auxiliary_list")
    return render(
        request,
        "vehicle/auxiliary/auxiliary_decommission.html",
        {"auxiliary": auxiliary},
    )
