from django.db import models

# Create your models here.

class Cocktail(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=300)
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
