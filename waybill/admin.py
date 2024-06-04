from django.contrib import admin

from .models import CargoWaybill, Waybill

# Register your models here.
admin.site.register(Waybill)
admin.site.register(CargoWaybill)
