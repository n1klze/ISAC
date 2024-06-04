from django.urls import path

from . import views

urlpatterns = [
    path("", views.queries_list, name="queries_list"),
    path("mileage/<int:pk>/", views.mileage_query, name="mileage_query"),
    path("cargo/<int:pk>/", views.cargo_query, name="cargo_query"),
    path("repair/<int:pk>/", views.repair_query, name="repair_query"),
    path("work/<int:pk>/", views.work_query, name="work_query"),
    path("receiving/", views.receiving_query, name="receiving_query"),
]
