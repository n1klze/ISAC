from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Repair(models.Model):
    vehicle_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="vehicle"
    )
    vehicle_id = models.PositiveIntegerField()
    vehicle = GenericForeignKey("vehicle_type", "vehicle_id")

    worker_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="worker"
    )
    worker_id = models.PositiveIntegerField()
    worker = GenericForeignKey("worker_type", "worker_id")

    created_at = models.DateField()

    def __str__(self) -> str:
        return f"{self.created_at} произведён ремонт автомобиля {self.vehicle} работником {self.worker}"


class Detail(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"Деталь: {self.name} стоимостью {self.cost}x{self.amount}={self.cost * self.amount}"
