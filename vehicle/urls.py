from django.urls import path

from . import views

urlpatterns = [
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("vehicles/<int:pk>/", views.vehicle_detail, name="vehicle_detail"),
    path("trucks/", views.truck_list, name="truck_list"),
    path("trucks/<int:pk>/", views.truck_detail, name="truck_detail"),
    path("add/truck/", views.truck_add, name="truck_add"),
    path(
        "truck/decommission/<int:pk>/",
        views.truck_decommission,
        name="truck_decommission",
    ),
    path("buses/", views.bus_list, name="bus_list"),
    path("buses/<int:pk>/", views.bus_detail, name="bus_detail"),
    path("add/bus/", views.bus_add, name="bus_add"),
    path("taxis/", views.taxi_list, name="taxi_list"),
    path("taxis/<int:pk>/", views.taxi_detail, name="taxi_detail"),
    path("add/taxi/", views.taxi_add, name="taxi_add"),
    path("auxiliaries/", views.auxiliary_list, name="auxiliary_list"),
    path("auxiliaries/<int:pk>/", views.auxiliary_detail, name="auxiliary_detail"),
    path("add/auxiliary/", views.auxiliary_add, name="auxiliary_add"),
]
