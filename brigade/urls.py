# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("teams/", views.team_list, name="team_list"),
    path("brigades/", views.brigade_list, name="brigade_list"),
    path("brigades/<int:pk>/", views.brigade_detail, name="brigade_detail"),
    path("add/brigade/", views.brigade_add, name="brigade_add"),
    path("districts/", views.district_list, name="district_list"),
    path("districts/<int:pk>/", views.district_detail, name="district_detail"),
    path("add/district/", views.district_add, name="district_add"),
    path("workshops/", views.workshop_list, name="workshop_list"),
    path("workshops/<int:pk>/", views.workshop_detail, name="workshop_detail"),
    path("add/workshop/", views.workshop_add, name="workshop_add"),
]
