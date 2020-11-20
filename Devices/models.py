from django.db import models

# Create your models here.


class Temperatura (models.Model):

    fecha = models.DateTimeField(auto_now=True)
    valor = models.FloatField()

class Humedad (models.Model):

    fecha = models.DateTimeField(auto_now=True)
    valor = models.FloatField()