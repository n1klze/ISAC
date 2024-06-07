from django.urls import path

from . import views

urlpatterns = [
    path("routes/", views.route_list, name="route_list"),
    path("routes/<int:pk>/", views.route_detail, name="route_detail"),
    path("add/route/", views.route_add, name="route_add"),
    path("edit/route/<int:pk>", views.route_edit, name="route_edit"),
    path("delete/route/<int:pk>", views.route_delete, name="route_delete"),
]
