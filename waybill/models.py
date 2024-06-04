from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from workers.models import Driver


# Create your models here.
class Waybill(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    vehicle = GenericForeignKey("content_type", "object_id")
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    created_at = models.DateField()

    def __str__(self) -> str:
        return f"Автомобиль {self.vehicle} числа {self.created_at} прошел {self.mileage} км. Водитель {self.driver.name}"


class CargoWaybill(models.Model):
    product = models.CharField(max_length=50)
    cost = models.IntegerField()
    waybill = models.ForeignKey(Waybill, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Продукт {self.product} по цене {self.cost}"
