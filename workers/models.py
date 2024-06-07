from brigade.models import Brigade
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50)
    brigade = models.ForeignKey(Brigade, on_delete=models.PROTECT)
    created_at = models.DateField()
    modified_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Driver(Worker):
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    vehicle = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return f"Водитель {self.worker_ptr.name} бригады №{self.worker_ptr.brigade.id} закреплён за автомобилем {self.vehicle}"


class Mechanic(Worker):
    def __str__(self) -> str:
        return f"Механик {self.worker_ptr.name} бригады №{self.worker_ptr.brigade.id}"


class Technician(Worker):
    def __str__(self) -> str:
        return f"Техник {self.worker_ptr.name} бригады №{self.worker_ptr.brigade.id}"


class Welder(Worker):
    welding_machine = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Сварщик {self.worker_ptr.name} бригады №{self.worker_ptr.brigade}. Используемый аппарат: {self.welding_machine}"


class Assembler(Worker):
    assembly_machine = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Сборщик {self.worker_ptr.name} бригады №{self.worker_ptr.brigade}. Используемый аппарат: {self.assembly_machine}"
