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
    return render(request, "garage/garage_add.html", {"form": form})
