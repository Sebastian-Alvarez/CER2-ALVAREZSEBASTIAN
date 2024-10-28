from django.db import models
from django import forms


# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name