from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CargoWaybillForm, WaybillForm
from .models import CargoWaybill, Waybill


def bill_list(request):
    return render(request, "waybill/bill_list.html")


def waybill_list(request):
    waybills = Waybill.objects.exclude(
        content_type=ContentType.objects.get(app_label="vehicle", model="truck")
    )
    return render(request, "waybill/waybill/waybill_list.html", {"waybills": waybills})


def waybill_detail(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    context = {"waybill": waybill}
    return render(request, "waybill/waybill/waybill_detail.html", context)


def waybill_add(request):
    if request.method == "POST":
        form = WaybillForm(request.POST)
        if form.is_valid():
            waybill = form.save(commit=False)
            waybill.object_id = form.cleaned_data.get("vehicle").pk
            try:
                if form.cleaned_data.get("vehicle").truck:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="truck"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").bus:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="bus"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").taxi:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="taxi"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").auxiliary:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="auxiliary"
                    )
            except:
                ...
            waybill.created_at = form.cleaned_data.get("created_at")
            waybill.save()
            return redirect("bill_list")
    else:
        form = WaybillForm()
    return render(request, "waybill/waybill/waybill_form.html", {"form": form})


def waybill_edit(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    if request.method == "POST":
        form = WaybillForm(request.POST, instance=waybill)
        if form.is_valid():
            waybill = form.save(commit=False)
            waybill.object_id = form.cleaned_data.get("vehicle").pk
            try:
                if form.cleaned_data.get("vehicle").truck:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="truck"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").bus:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="bus"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").taxi:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="taxi"
                    )
            except:
                ...
            try:
                if form.cleaned_data.get("vehicle").auxiliary:
                    waybill.content_type = ContentType.objects.get(
                        app_label="vehicle", model="auxiliary"
                    )
            except:
                ...
            waybill.created_at = form.cleaned_data.get("created_at")
            waybill.save()
            return redirect("bill_list")
    else:
        form = WaybillForm(instance=waybill)
    return render(request, "waybill/waybill/waybill_form.html", {"form": form})


def waybill_delete(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    if request.method == "POST":
        CargoWaybill.objects.filter(waybill=waybill).delete()
        waybill.delete()
        return redirect("bill_list")
    return render(request, "waybill/waybill/waybill_delete.html", {"waybill": waybill})


def cargo_waybill_list(request):
    cargo_waybills = Waybill.objects.filter(
        content_type=ContentType.objects.get(app_label="vehicle", model="truck")
    )
    return render(
        request,
        "waybill/cargo_waybill/cargo_waybill_list.html",
        {"cargo_waybills": cargo_waybills},
    )


def cargo_waybill_detail(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    cargo_waybills = CargoWaybill.objects.filter(waybill=waybill)
    return render(
        request,
        "waybill/cargo_waybill/cargo_waybill_detail.html",
        {"waybill": waybill, "cargo_waybills": cargo_waybills},
    )


def cargo_waybill_add(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    if request.method == "POST":
        form = CargoWaybillForm(request.POST)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.waybill = waybill
            cargo.save()
            return redirect("cargo_waybill_detail", pk=waybill.pk)
    else:
        form = CargoWaybillForm()
    return render(
        request, "waybill/cargo_waybill/cargo_waybill_add.html", {"form": form}
    )


def cargo_waybill_delete(request, pk):
    cargo = get_object_or_404(CargoWaybill, pk=pk)
    waybill = cargo.waybill
    cargo.delete()
    return redirect("cargo_waybill_detail", pk=waybill.pk)


def cargo_waybill_edit(request, pk):
    cargo = get_object_or_404(CargoWaybill, pk=pk)
    if request.method == "POST":
        form = CargoWaybillForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect("cargo_waybill_detail", pk=form.cleaned_data["waybill"].pk)
    else:
        form = CargoWaybillForm(instance=cargo)
    return render(request, "waybill/cargo_waybill/waybill_edit.html", {"form": form})
