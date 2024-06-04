from django.shortcuts import get_object_or_404, redirect, render
from workers.models import Assembler, Driver, Mechanic, Technician, Welder

from .forms import BrigadeForm, DistrictForm, WorkshopForm
from .models import Brigade, District, Workshop


# Create your views here.
def team_list(request):
    workers = Brigade.objects.all()
    return render(request, "brigade/team_list.html", {"workers": workers})


def brigade_list(request):
    brigades = Brigade.objects.all()
    return render(request, "brigade/brigade/brigade_list.html", {"brigades": brigades})


def brigade_detail(request, pk):
    brigade = get_object_or_404(Brigade, pk=pk)
    drivers = Driver.objects.filter(brigade=brigade.pk)
    mechanics = Mechanic.objects.filter(brigade=brigade.pk)
    technicians = Technician.objects.filter(brigade=brigade.pk)
    welders = Welder.objects.filter(brigade=brigade.pk)
    assemblers = Assembler.objects.filter(brigade=brigade.pk)
    context = {
        "brigade": brigade,
        "drivers": drivers,
        "mechanics": mechanics,
        "technicians": technicians,
        "welders": welders,
        "assemblers": assemblers,
    }
    return render(request, "brigade/brigade/brigade_detail.html", context)


def brigade_add(request):
    if request.method == "POST":
        form = BrigadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brigade_list")
    else:
        form = BrigadeForm()
    return render(request, "brigade/brigade/brigade_add.html", {"form": form})


def district_list(request):
    districts = District.objects.all()
    return render(
        request, "brigade/district/district_list.html", {"districts": districts}
    )


def district_detail(request, pk):
    district = get_object_or_404(District, pk=pk)
    brigades = Brigade.objects.filter(district=district.pk)
    context = {"district": district, "brigades": brigades}
    return render(request, "brigade/district/district_detail.html", context)


def district_add(request):
    if request.method == "POST":
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("district_list")
    else:
        form = DistrictForm()
    return render(request, "brigade/district/district_add.html", {"form": form})


def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(
        request, "brigade/workshop/workshop_list.html", {"workshops": workshops}
    )


def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    districts = District.objects.filter(workshop=workshop)
    context = {"workshop": workshop, "districts": districts}
    return render(request, "brigade/workshop/workshop_detail.html", context)


def workshop_add(request):
    if request.method == "POST":
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("workshop_list")
    else:
        form = WorkshopForm()
    return render(request, "brigade/workshop/workshop_add.html", {"form": form})
