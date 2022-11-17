from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=35)
    tipo = models.CharField(max_length=40)
    generacion = models.CharField(max_length=20, default='')