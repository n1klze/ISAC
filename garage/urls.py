from django.urls import path

from . import views

urlpatterns = [
    path("garages/", views.garage_list, name="garage_list"),
    path("garages/<int:pk>/", views.garage_detail, name="garage_detail"),
    path("garages/edit/<int:pk>/", views.garage_edit, name="garage_edit"),
    path("add/garage/", views.garage_add, name="garage_add"),
    path("garage/delete/<int:pk>/", views.garage_delete, name="garage_delete"),
]
