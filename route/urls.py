from django.urls import path

from . import views

urlpatterns = [
    path("routes/", views.route_list, name="route_list"),
    path("routes/<int:pk>/", views.route_detail, name="route_detail"),
    path("add/route/", views.route_add, name="route_add"),
]
