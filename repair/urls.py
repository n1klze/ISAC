from django.urls import path

from . import views

urlpatterns = [
    path("repairs/", views.repair_list, name="repair_list"),
    path("repairs/<int:pk>/", views.repair_detail, name="repair_detail"),
    path("add/repair/", views.repair_add, name="repair_add"),
    path(
        "details/<int:pk>/",
        views.detail_detail,
        name="detail_detail",
    ),
    path("add/detail/", views.detail_add, name="detail_add"),
]
