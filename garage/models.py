from django.db import models


# Create your models here.
class Garage(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Гараж №{self.pk}"
