from django.db import models
# from django.core.validators import *
# from .validator import *

class Brand(models.Model):
    name = models.CharField(max_length=100, null=False)
    origin_country = models.CharField(max_length=100, null=False)
    establishment_date = models.DateField()

class Option(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField()

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, null=False, on_delete=models.CASCADE, related_name="models" )
    name = models.CharField(max_length=100, null=False)
    assembled_country = models.CharField(max_length=100, null=False)
    release_date = models.DateField()
    base_price = models.IntegerField()
    options = models.ManyToManyField(Option, through="ModelOptions")

class ModelOptions(models.Model):
    option = models.ForeignKey(Option, null=False, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, null=False, on_delete=models.CASCADE)