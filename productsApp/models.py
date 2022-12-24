from django.db import models

class ProductsApp(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

# Create your models here.
