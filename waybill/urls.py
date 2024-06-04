from django.urls import path

from . import views

urlpatterns = [
    path("bills/", views.bill_list, name="bill_list"),
    path("waybills/", views.waybill_list, name="waybill_list"),
    path("waybills/<int:pk>/", views.waybill_detail, name="waybill_detail"),
    path("add/waybill/", views.waybill_add, name="waybill_add"),
    path("cargo_waybills/", views.cargo_waybill_list, name="cargo_waybill_list"),
    path(
        "cargo_waybills/<int:pk>/",
        views.cargo_waybill_detail,
        name="cargo_waybill_detail",
    ),
    path("add/cargo_waybill/", views.cargo_waybill_add, name="cargo_waybill_add"),
]
