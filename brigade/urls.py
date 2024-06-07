# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("teams/", views.team_list, name="team_list"),
    path("brigades/", views.brigade_list, name="brigade_list"),
    path("brigades/<int:pk>/", views.brigade_detail, name="brigade_detail"),
    path("brigade/delete/<int:pk>/", views.brigade_delete, name="brigade_delete"),
    path("brigade/edit/<int:pk>/", views.brigade_edit, name="brigade_edit"),
    path("add/brigade/", views.brigade_add, name="brigade_add"),
    path("districts/", views.district_list, name="district_list"),
    path("districts/<int:pk>/", views.district_detail, name="district_detail"),
    path("add/district/", views.district_add, name="district_add"),
    path("district/edit/<int:pk>/", views.district_edit, name="district_edit"),
    path("district/delete/<int:pk>/", views.district_delete, name="district_delete"),
    path("workshops/", views.workshop_list, name="workshop_list"),
    path("workshops/<int:pk>/", views.workshop_detail, name="workshop_detail"),
    path("add/workshop/", views.workshop_add, name="workshop_add"),
    path("workshop/edit/<int:pk>/", views.workshop_edit, name="workshop_edit"),
    path("workshop/delete/<int:pk>/", views.workshop_delete, name="workshop_delete"),
]
