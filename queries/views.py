from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from repair.models import Detail, Repair
from vehicle.models import Auxiliary, Bus, Taxi, Truck, Vehicle
from waybill.models import CargoWaybill, Waybill
from workers.models import Worker


# Create your views here.
def queries_list(request):
    return render(request, "queries/queries_list.html")


def mileage_query(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if vehicle and start_date and end_date:
        waybills = Waybill.objects.filter(
            Q(object_id=pk) & Q(created_at__range=(start_date, end_date))
        )
        total_mileage = sum(waybill.mileage for waybill in waybills)
    else:
        waybills = Waybill.objects.none()
        total_mileage = 0

    context = {
        "vehicle": vehicle,
        "waybills": waybills,
        "total_mileage": total_mileage,
    }
    return render(request, "queries/mileage_query.html", context)


def cargo_query(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if truck and start_date and end_date:
        waybills = Waybill.objects.filter(
            Q(object_id=pk) & Q(created_at__range=(start_date, end_date))
        )
        cargo_waybills = CargoWaybill.objects.select_related("waybill")
    else:
        waybills = Waybill.objects.none()
        cargo_waybills = Waybill.objects.none()

    context = {
        "vehicle": truck,
        "waybills": waybills,
        "cargo_waybills": cargo_waybills,
    }
    return render(request, "queries/cargo_query.html", context)


def repair_query(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if vehicle and start_date and end_date:
        repairs = Repair.objects.filter(
            Q(vehicle_id=pk) & Q(created_at__range=(start_date, end_date))
        )
        details = Detail.objects.select_related("repair")
    else:
        repairs = Repair.objects.none()
        details = Detail.objects.none()

    context = {
        "vehicle": vehicle,
        "repairs": repairs,
        "details": details,
    }
    return render(request, "queries/repair_query.html", context)


def work_query(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    vehicles = Vehicle.objects.all()
    vehicle = request.GET.get("vehicle")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if worker and start_date and end_date and vehicle:
        repairs = Repair.objects.filter(
            Q(worker_id=pk)
            & Q(vehicle_id=vehicle)
            & Q(created_at__range=(start_date, end_date))
        )
        details = Detail.objects.select_related("repair")
    elif worker and start_date and end_date:
        repairs = Repair.objects.filter(
            Q(worker_id=pk) & Q(created_at__range=(start_date, end_date))
        )
        details = Detail.objects.select_related("repair")
    else:
        repairs = Repair.objects.none()
        details = Detail.objects.none()

    context = {
        "vehicles": vehicles,
        "worker": worker,
        "repairs": repairs,
        "details": details,
    }
    return render(request, "queries/work_query.html", context)


def receiving_query(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    is_decommissioned = request.GET.get("is_decommissioned") == "on"

    if start_date and end_date:
        trucks = Truck.objects.filter(
            Q(is_decommissioned=is_decommissioned)
            & Q(created_at__range=(start_date, end_date))
        )
        buses = Bus.objects.filter(
            Q(is_decommissioned=is_decommissioned)
            & Q(created_at__range=(start_date, end_date))
        )
        taxis = Taxi.objects.filter(
            Q(is_decommissioned=is_decommissioned)
            & Q(created_at__range=(start_date, end_date))
        )
        auxiliaries = Auxiliary.objects.filter(
            Q(is_decommissioned=is_decommissioned)
            & Q(created_at__range=(start_date, end_date))
        )
    else:
        trucks = Truck.objects.none()
        buses = Bus.objects.none()
        taxis = Taxi.objects.none()
        auxiliaries = Auxiliary.objects.none()

    context = {
        "trucks": trucks,
        "buses": buses,
        "taxis": taxis,
        "auxiliaries": auxiliaries,
    }
    return render(request, "queries/receiving_query.html", context)
