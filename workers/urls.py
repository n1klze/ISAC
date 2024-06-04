# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.worker_list, name="worker_list"),
    path("workers/<int:pk>/", views.worker_detail, name="worker_detail"),
    path("drivers/", views.driver_list, name="driver_list"),
    path("drivers/<int:pk>/", views.driver_detail, name="driver_detail"),
    path("add/driver/", views.driver_add, name="driver_add"),
    path("mechanics/", views.mechanic_list, name="mechanic_list"),
    path("mechanics/<int:pk>/", views.mechanic_detail, name="mechanic_detail"),
    path("add/mechanic/", views.mechanic_add, name="mechanic_add"),
    path("technicians/", views.technician_list, name="technician_list"),
    path("technicians/<int:pk>/", views.technician_detail, name="technician_detail"),
    path("add/technician/", views.technician_add, name="technician_add"),
    path("welders/", views.welder_list, name="welder_list"),
    path("welders/<int:pk>/", views.welder_detail, name="welder_detail"),
    path("add/welder/", views.welder_add, name="welder_add"),
    path("assemblers/", views.assembler_list, name="assembler_list"),
    path("assemblers/<int:pk>/", views.assembler_detail, name="assembler_detail"),
    path("add/assembler/", views.assembler_add, name="assembler_add"),
]
