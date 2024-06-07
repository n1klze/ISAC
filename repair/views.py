from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DetailForm, RepairForm
from .models import Detail, Repair


# Create your views here.
def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, "repair/repair/repair_list.html", {"repairs": repairs})


def repair_detail(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    details = Detail.objects.filter(repair=repair)
    return render(
        request,
        "repair/repair/repair_detail.html",
        {"repair": repair, "details": details},
    )


def repair_add(request):
    if request.method == "POST":
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.vehicle_id = form.cleaned_data.get("vehicle").pk
            try:
                if form.cleaned_data.get("vehicle").truck:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="truck"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").bus:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="bus"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").taxi:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="taxi"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").auxiliary:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="auxiliary"
                    )
            except:
                ...

            repair.worker_id = form.cleaned_data.get("worker").pk
            try:
                if form.cleaned_data.get("worker").driver:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="driver"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").mechanic:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="mechanic"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").technician:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="technician"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").welder:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="welder"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").assembler:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="assembler"
                    )
            except:
                ...
            repair.created_at = form.cleaned_data.get("created_at")
            repair.save()
            return redirect("repair_list")
    else:
        form = RepairForm()
    return render(request, "repair/repair/repair_form.html", {"form": form})


def repair_edit(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == "POST":
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.vehicle_id = form.cleaned_data.get("vehicle").pk
            try:
                if form.cleaned_data.get("vehicle").truck:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="truck"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").bus:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="bus"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").taxi:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="taxi"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").auxiliary:
                    repair.vehicle_type = ContentType.objects.get(
                        app_label="vehicle", model="auxiliary"
                    )
            except:
                ...

            repair.worker_id = form.cleaned_data.get("worker").pk
            try:
                if form.cleaned_data.get("worker").driver:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="driver"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").mechanic:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="mechanic"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").technician:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="technician"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").welder:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="welder"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("worker").assembler:
                    repair.worker_type = ContentType.objects.get(
                        app_label="workers", model="assembler"
                    )
            except:
                ...
            repair.created_at = form.cleaned_data.get("created_at")
            repair.save()
            return redirect("repair_list")
    else:
        form = RepairForm(instance=repair)
    return render(request, "repair/repair/repair_form.html", {"form": form})


def repair_delete(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == "POST":
        Detail.objects.filter(repair=repair).delete()
        repair.delete()
        return redirect("repair_list")
    return render(request, "repair/repair/repair_delete.html", {"repair": repair})


def detail_list(request):
    details = Detail.objects.all()
    return render(
        request,
        "repair/detail/detail_list.html",
        {"details": details},
    )


def detail_detail(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    total = detail.amount * detail.cost
    return render(
        request,
        "repair/detail/detail_detail.html",
        {"detail": detail, "total": total},
    )


def detail_add(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("repair_detail", pk=form.cleaned_data["repair"].pk)
    else:
        form = DetailForm()
    return render(request, "repair/detail/detail_add.html", {"form": form})


def detail_delete(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    repair = detail.repair
    detail.delete()
    return redirect("repair_detail", pk=repair.pk)


def detail_edit(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    if request.method == "POST":
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect("repair_detail", pk=form.cleaned_data["repair"].pk)
    else:
        form = DetailForm(instance=detail)
    return render(request, "repair/detail/detail_edit.html", {"form": form})
