from django.db import models


# Create your models here.
class Workshop(models.Model):
    head = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Цех №{self.pk}. Начальник: {self.head}"


class District(models.Model):
    master = models.CharField(max_length=50)
    workshop = models.OneToOneField(Workshop, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"Участок №{self.pk}. Мастер: {self.master}"


class Brigade(models.Model):
    brigadier = models.CharField(max_length=50)
    district = models.OneToOneField(District, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"Бригада №{self.pk}. Бригадир: {self.brigadier}"
