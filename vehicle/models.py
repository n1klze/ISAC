from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from garage.models import Garage
from repair.models import Repair
from route.models import Route
from waybill.models import Waybill
from workers.models import Driver


# Create your models here.
class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    garage = models.ForeignKey(Garage, on_delete=models.PROTECT, null=True, blank=True)
    is_decommissioned = models.BooleanField(default=False)
    created_at = models.DateField()
    modified_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.brand}"


class Truck(Vehicle):
    capacity = models.IntegerField()
    drivers = GenericRelation(Driver, related_query_name="truck")
    waybills = GenericRelation(Waybill, related_query_name="truck")
    repairs = GenericRelation(Repair, related_query_name="truck")

    def __str__(self) -> str:
        return (
            f"Грузовой автомобиль {self.vehicle_ptr.brand} грузоподъёмностью {self.capacity} кг."
            + (
                f" СПИСАН {self.vehicle_ptr.modified_at}"
                if self.vehicle_ptr.is_decommissioned
                else ""
            )
        )


class Bus(Vehicle):
    passenger_capacity = models.IntegerField()
    drivers = GenericRelation(Driver, related_query_name="bus")
    waybills = GenericRelation(Waybill, related_query_name="bus")
    repairs = GenericRelation(Repair, related_query_name="bus")
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return (
            f"Автобус {self.vehicle_ptr.brand} {self.passenger_capacity} посадочных мест."
            + (
                f" СПИСАН {self.vehicle_ptr.modified_at}"
                if self.vehicle_ptr.is_decommissioned
                else ""
            )
        )


class Taxi(Vehicle):
    passenger_capacity = models.IntegerField()
    drivers = GenericRelation(Driver, related_query_name="taxi")
    waybills = GenericRelation(Waybill, related_query_name="taxi")
    repairs = GenericRelation(Repair, related_query_name="taxi")
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return (
            f"Маршрутное такси {self.vehicle_ptr.brand} {self.passenger_capacity} посадочных мест."
            + (
                f" СПИСАН {self.vehicle_ptr.modified_at}"
                if self.vehicle_ptr.is_decommissioned
                else ""
            )
        )


class Auxiliary(Vehicle):
    description = models.CharField(max_length=50)
    drivers = GenericRelation(Driver, related_query_name="auxiliary")
    waybills = GenericRelation(Waybill, related_query_name="auxiliary")
    repairs = GenericRelation(Repair, related_query_name="auxiliary")

    def __str__(self) -> str:
        return f"{self.description} {self.vehicle_ptr.brand}." + (
            f" СПИСАН {self.vehicle_ptr.modified_at}"
            if self.vehicle_ptr.is_decommissioned
            else ""
        )
