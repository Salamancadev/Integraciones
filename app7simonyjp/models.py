from django.db import models

# Create your models here.
class Humedad(models.Model):
    humedad_actual = models.CharField(max_length=10)
    humedad_maxima = models.CharField(max_length=10)
    humedad_minima = models.CharField(max_length=10)
    humedad_solicitada = models.CharField(max_length=10)

    def __str__(self):
        return self.humedad_actual

class Luz(models.Model):
    luz_actual = models.CharField(max_length=10)
    luz_maxima = models.CharField(max_length=10)
    luz_minima = models.CharField(max_length=10)
    luz_solicitada = models.CharField(max_length=10)

    def __str__(self):
        return self.luz_actual

class Temperatura(models.Model):
    temperatura_actual = models.CharField(max_length=10)
    temperatura_maxima = models.CharField(max_length=10)
    temperatura_minima = models.CharField(max_length=10)
    temperatura_solicitada = models.CharField(max_length=10)

    def __str__(self):
        return self.temperatura_actual

