from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    permisos = models.TextField()

    def __str__(self):
        return self.nombre

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_cosecha_estimada = models.DateField()

    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    TIPO_CHOICES = [
        ('humedad', 'Humedad'),
        ('temperatura', 'Temperatura'),
        # Agrega más tipos si es necesario
    ]
    tipo_sensor = models.CharField(max_length=50, choices=TIPO_CHOICES)
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f"{self.tipo_sensor} - {self.ubicacion}"

class LecturaSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    fecha_hora = models.DateTimeField()
    valor = models.FloatField()

    def __str__(self):
        return f"{self.sensor} - {self.fecha_hora}"

class Cosecha(models.Model):
    #cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='cosechas')
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cosechas')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    produccion_total = models.FloatField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Cosecha de {self.cultivo.nombre} por {self.usuario.nombre}"

class Alerta(models.Model):
    mensaje = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField()
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='alertas')
    lectura_sensor = models.ForeignKey(LecturaSensor, on_delete=models.SET_NULL, null=True, blank=True, related_name='alertas')

    def __str__(self):
        return f"Alerta: {self.tipo} - {self.mensaje}"

class Informe(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='informes')
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='informes')

    def __str__(self):
        return f"Informe de {self.cultivo.nombre}"
