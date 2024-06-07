from django.urls import path

from . import views

urlpatterns = [
    path("repairs/", views.repair_list, name="repair_list"),
    path("repairs/<int:pk>/", views.repair_detail, name="repair_detail"),
    path("add/repair/", views.repair_add, name="repair_add"),
    path("repair/edit/<int:pk>/", views.repair_edit, name="repair_edit"),
    path("repair/delete/<int:pk>/", views.repair_delete, name="repair_delete"),
    path(
        "details/<int:pk>/",
        views.detail_detail,
        name="detail_detail",
    ),
    path("add/detail/", views.detail_add, name="detail_add"),
    path("detail/edit/<int:pk>", views.detail_edit, name="detail_edit"),
    path("detail/delete/<int:pk>", views.detail_delete, name="detail_delete"),
]
