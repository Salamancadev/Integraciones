from django.db import models

class SensorHumedad(models.Model):
    ubicacion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class Medicion(models.Model):
    sensor = models.CharField()
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

class Alerta(models.Model):
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    critica = models.BooleanField(default=False)

class ConfiguracionRiego(models.Model):
    umbral_minimo = models.FloatField()
    riego_automatico = models.BooleanField(default=False)
