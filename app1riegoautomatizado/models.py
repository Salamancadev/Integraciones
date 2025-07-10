from django.db import models
from django.utils import timezone

# Create your models here.
    

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class ZonaRiego(models.Model):
    nombre = models.CharField(max_length=100)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='zonas')
    area_m2 = models.FloatField()

    def __str__(self):
        return f'Zona {self.nombre} - {self.cultivo.nombre}'
    
class SensorHumedad(models.Model):
    zona = models.ForeignKey(ZonaRiego, on_delete=models.CASCADE, related_name='sensores')
    identificador = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return f'Sensor {self.identificador} - {self.zona.nombre}'

class LecturaHumedad(models.Model):
    sensor = models.ForeignKey(SensorHumedad, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.FloatField(help_text='Porcentaje de humedad (%)')
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sensor.identificador} - {self.valor}% - {self.fecha}'
    
class Riego(models.Model):
    zona = models.ForeignKey(ZonaRiego, on_delete=models.CASCADE, related_name='riegos')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    cantidad_agua_litros = models.FloatField()

    def __str__(self):
        return f'Riego en {self.zona.nombre} - {self.fecha_inicio.strftime("%Y-%m-%d %H:%M")}'


class PronosticoClima(models.Model):
    zona = models.ForeignKey(ZonaRiego, on_delete=models.CASCADE, related_name='pronosticos')
    fecha = models.DateField()
    temperatura = models.FloatField()
    precipitacion = models.FloatField(help_text='Precipitación esperada en mm')
    humedad = models.FloatField()

    def __str__(self):
        return f'{self.zona.nombre} - {self.fecha}'