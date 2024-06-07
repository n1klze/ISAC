from django.urls import path

from . import views

urlpatterns = [
    path("bills/", views.bill_list, name="bill_list"),
    path("waybills/", views.waybill_list, name="waybill_list"),
    path("waybills/<int:pk>/", views.waybill_detail, name="waybill_detail"),
    path("add/waybill/", views.waybill_add, name="waybill_add"),
    path("edit/waybill/<int:pk>/", views.waybill_edit, name="waybill_edit"),
    path("delete/waybill/<int:pk>", views.waybill_delete, name="waybill_delete"),
    path("cargo_waybills/", views.cargo_waybill_list, name="cargo_waybill_list"),
    path(
        "cargo_waybills/<int:pk>/",
        views.cargo_waybill_detail,
        name="cargo_waybill_detail",
    ),
    path(
        "waybill/<int:pk>/add/cargo/", views.cargo_waybill_add, name="cargo_waybill_add"
    ),
    path(
        "cargo_waybill/edit/<int:pk>",
        views.cargo_waybill_edit,
        name="cargo_waybill_edit",
    ),
    path(
        "cargo_waybill/delete/<int:pk>",
        views.cargo_waybill_delete,
        name="cargo_waybill_delete",
    ),
]
