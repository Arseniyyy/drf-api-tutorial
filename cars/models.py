from django.db import models
from django.conf import settings


class Car(models.Model):
    class CarType(models.IntegerChoices):
        SEDAN = 1
        HATCHBACK = 2
        UNIVERSAL = 3
        COUPE = 4
    vin = models.CharField(verbose_name='Vin', unique=True, db_index=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=15)
    brand = models.CharField(verbose_name='Brand', max_length=30)
    car_type = models.CharField(verbose_name='Car type', choices=CarType.choices, max_length=8)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)
