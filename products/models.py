from django.db import models


class Product(models.Model):
    name = models.CharField(max_lenght=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_lenght=2083)
