from django.db import models

class ProductsApp(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()

# Create your models here.
