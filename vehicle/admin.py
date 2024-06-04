from django.contrib import admin

from .models import Auxiliary, Bus, Taxi, Truck, Vehicle

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Truck)
admin.site.register(Bus)
admin.site.register(Taxi)
admin.site.register(Auxiliary)
