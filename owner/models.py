from django.db import models


class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=2)
    pais = models.CharField(max_length=20, default='')

    def __str__(self):
        return "{}", "{}", format(self.nombre, self.edad)
