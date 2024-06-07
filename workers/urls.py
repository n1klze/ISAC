# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.worker_list, name="worker_list"),
    path("workers/<int:pk>/", views.worker_detail, name="worker_detail"),
    path("drivers/", views.driver_list, name="driver_list"),
    path("drivers/<int:pk>/", views.driver_detail, name="driver_detail"),
    path("add/driver/", views.driver_add, name="driver_add"),
    path("edit/driver/<int:pk>/", views.driver_edit, name="driver_edit"),
    path("driver/delete/<int:pk>/", views.driver_delete, name="driver_delete"),
    path("mechanics/", views.mechanic_list, name="mechanic_list"),
    path("mechanics/<int:pk>/", views.mechanic_detail, name="mechanic_detail"),
    path("add/mechanic/", views.mechanic_add, name="mechanic_add"),
    path("edit/mechanic/<int:pk>/", views.mechanic_edit, name="mechanic_edit"),
    path("mechanic/delete/<int:pk>/", views.mechanic_delete, name="mechanic_delete"),
    path("technicians/", views.technician_list, name="technician_list"),
    path("technicians/<int:pk>/", views.technician_detail, name="technician_detail"),
    path("add/technician/", views.technician_add, name="technician_add"),
    path("edit/technician/<int:pk>/", views.technician_edit, name="technician_edit"),
    path(
        "technician/delete/<int:pk>/", views.technician_delete, name="technician_delete"
    ),
    path("welders/", views.welder_list, name="welder_list"),
    path("welders/<int:pk>/", views.welder_detail, name="welder_detail"),
    path("add/welder/", views.welder_add, name="welder_add"),
    path("edit/welder/<int:pk>/", views.welder_edit, name="welder_edit"),
    path("welder/delete/<int:pk>/", views.welder_delete, name="welder_delete"),
    path("assemblers/", views.assembler_list, name="assembler_list"),
    path("assemblers/<int:pk>/", views.assembler_detail, name="assembler_detail"),
    path("add/assembler/", views.assembler_add, name="assembler_add"),
    path("edit/assembler/<int:pk>/", views.assembler_edit, name="assembler_edit"),
    path("assembler/delete/<int:pk>/", views.assembler_delete, name="assembler_delete"),
]
