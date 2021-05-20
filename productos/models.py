from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    moneda = models.CharField(max_length=3,default='CLP')
    existencia = models.IntegerField()
    descripcion = models.CharField(max_length=2000,default='')
    imagen_url = models.CharField(max_length=255)
    ##objects = models.Manager()

class Oferta(models.Model):
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=255)
    descuento = models.FloatField()