from django.db import models




class historial(models.Model):
    mes = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.mes
    
class control(models.Model):
    temperatura = models.IntegerField()
    humedad = models.IntegerField()
    carbono = models.IntegerField()


    def __str__(self):
        return self.temperatura
    