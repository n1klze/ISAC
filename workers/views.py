from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AssemblerForm, DriverForm, MechanicForm, TechnicianForm, WelderForm
from .models import Assembler, Driver, Mechanic, Technician, Welder, Worker


# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    return render(request, "worker/worker_list.html", {"workers": workers})


def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    return render(request, "worker/worker_detail.html", {"worker": worker})


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, "worker/driver/driver_list.html", {"drivers": drivers})


def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, "worker/driver/driver_detail.html", {"driver": driver})


def driver_add(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.object_id = form.cleaned_data.get("vehicle").pk
            try:
                if form.cleaned_data.get("vehicle").truck:
                    driver.content_type = ContentType.objects.get(
                        app_label="vehicle", model="truck"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").bus:
                    driver.content_type = ContentType.objects.get(
                        app_label="vehicle", model="bus"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").taxi:
                    driver.content_type = ContentType.objects.get(
                        app_label="vehicle", model="taxi"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").auxiliary:
                    driver.content_type = ContentType.objects.get(
                        app_label="vehicle", model="auxiliary"
                    )
            except:
                ...
            driver.created_at = form.cleaned_data.get("created_at")
            driver.save()
            return redirect("driver_list")
    else:
        form = DriverForm()
    return render(request, "worker/driver/driver_add.html", {"form": form})


def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    return render(
        request, "worker/mechanic/mechanic_list.html", {"mechanics": mechanics}
    )


def mechanic_detail(request, pk):
    mechanic = get_object_or_404(Mechanic, pk=pk)
    return render(
        request, "worker/mechanic/mechanic_detail.html", {"mechanic": mechanic}
    )


def mechanic_add(request):
    if request.method == "POST":
        form = MechanicForm(request.POST)
        if form.is_valid():
            mechanic = form.save(commit=False)
            mechanic.created_at = form.cleaned_data.get("created_at")
            mechanic.save()
            return redirect("mechanic_list")
    else:
        form = MechanicForm()
    return render(request, "worker/mechanic/mechanic_add.html", {"form": form})


def technician_list(request):
    technicians = Technician.objects.all()
    return render(
        request, "worker/technician/technician_list.html", {"technicians": technicians}
    )


def technician_detail(request, pk):
    technician = get_object_or_404(Technician, pk=pk)
    return render(
        request, "worker/technician/technician_detail.html", {"technician": technician}
    )


def technician_add(request):
    if request.method == "POST":
        form = TechnicianForm(request.POST)
        if form.is_valid():
            technician = form.save(commit=False)
            technician.created_at = form.cleaned_data.get("created_at")
            technician.save()
            return redirect("technician_list")
    else:
        form = TechnicianForm()
    return render(request, "worker/technician/technician_add.html", {"form": form})


def welder_list(request):
    welders = Welder.objects.all()
    return render(request, "worker/welder/welder_list.html", {"welders": welders})


def welder_detail(request, pk):
    welder = get_object_or_404(Welder, pk=pk)
    return render(request, "worker/welder/welder_detail.html", {"welder": welder})


def welder_add(request):
    if request.method == "POST":
        form = WelderForm(request.POST)
        if form.is_valid():
            welder = form.save(commit=False)
            welder.created_at = form.cleaned_data.get("created_at")
            welder.save()
            return redirect("welder_list")
    else:
        form = WelderForm()
    return render(request, "worker/welder/welder_add.html", {"form": form})


def assembler_list(request):
    assemblers = Assembler.objects.all()
    return render(
        request, "worker/assembler/assembler_list.html", {"assemblers": assemblers}
    )


def assembler_detail(request, pk):
    assembler = get_object_or_404(Assembler, pk=pk)
    return render(
        request, "worker/assembler/assembler_detail.html", {"assembler": assembler}
    )


def assembler_add(request):
    if request.method == "POST":
        form = AssemblerForm(request.POST)
        if form.is_valid():
            assembler = form.save(commit=False)
            assembler.created_at = form.cleaned_data.get("created_at")
            assembler.save()
            return redirect("assembler_list")
    else:
        form = AssemblerForm()
    return render(request, "worker/assembler/assembler_add.html", {"form": form})
