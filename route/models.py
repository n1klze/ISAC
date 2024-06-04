from django.db import models


# Create your models here.
class Route(models.Model):
    number = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return f"Маршрут  №{self.number}"
