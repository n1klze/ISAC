from django.shortcuts import get_object_or_404, redirect, render
from vehicle.models import Bus, Taxi

from .forms import RouteForm
from .models import Route


# Create your views here.
def route_list(request):
    routes = Route.objects.all()
    return render(request, "route/route_list.html", {"routes": routes})


def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    buses = Bus.objects.filter(route=route.pk)
    taxis = Taxi.objects.filter(route=route.pk)
    context = {"route": route, "buses": buses, "taxis": taxis}
    return render(request, "route/route_detail.html", context)


def route_add(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("route_list")
    else:
        form = RouteForm()
    return render(request, "route/route_form.html", {"form": form})


def route_edit(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect("route_list")
    else:
        form = RouteForm(instance=route)
    return render(request, "route/route_form.html", {"form": form})


def route_delete(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        Bus.objects.filter(route=route).update(route=None)
        Taxi.objects.filter(route=route).update(route=None)
        route.delete()
        return redirect("route_list")
    return render(request, "route/route_delete.html", {"route": route})
