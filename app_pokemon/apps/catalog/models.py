from django.db import models

# Create your models here.

class Catalog(models.Model):
    nombre_catalogo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    #especie = models.CharField(max_length=20)
    #genero = models.CharField(max_length=1)