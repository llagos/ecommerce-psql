from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    existencia = models.IntegerField()
    imagen_url = models.CharField(max_length=255)

class Oferta(models.Model):
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=255)
    descuento = models.FloatField()