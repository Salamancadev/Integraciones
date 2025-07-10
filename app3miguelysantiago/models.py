from django.db import models
from django.utils import timezone

# Create your models here.

# Registro
class Registro(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    TIPO_DOCUMENTO = [
        ('Tarjeta de Identidad','T.I'),
        ('Cedula de Ciudadania','C.C')
    ]
    tipoDocumento = models.CharField(max_length=100, choices=TIPO_DOCUMENTO)
    numeroDocumento = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.contraseña}, {self.numeroDocumento}"



# Inicio de sesion
class InicioSecion(models.Model):
    ROLE_CHOICES = [
        ('Agricultor', 'Agricultor'),
        ('Administrador', 'Administrador')
    ]
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES)
    numeroDoc = models.CharField(max_length=10)
    contraseña = models.ForeignKey(Registro, max_length=15, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.rol}"



# Gestion del administrador (CRUD)
class adminGestio(models.Model):
    fechas = models.DateTimeField(default=timezone.now)
    Cantidad_Productos = models.CharField(max_length=10)
    TIPO_COSECHA = [
        ('Cosecha Manual', 'Cosecha Manual'),
        ('Cosecha Mecanica', 'Cosecha Mecanica'),
    ]
    tipo_Cosecha = models.CharField(max_length=100, choices=TIPO_COSECHA)

    def __str__(self):
        return f"{self.fechas}, {self.Cantidad_Productos}"



# Inventario de Administrador
class admInventario(models.Model):
    Tipo_SEMILLA = [
        ('Alverja', 'Alverja'),
        ('Frijoles', 'Frijoles'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia'),
        ('Papa', 'Papa'),
        ('Aguacate', 'Aguacate'),
        ('Tomate', 'Tomate'),
        ('Mora', 'Mora'),
        ('Papaya', 'Papaya'),
        ('Uvas', 'Uvas'),
    ]
    CESECHA_REGISTRO = [
        ('Finalizada','Finalizada'),
        ('En proceso', 'En porceso')
    ]
    Semillas = models.CharField(max_length=10, choices=Tipo_SEMILLA)
    CosechasRegistradas = models.CharField(max_length=100, choices=CESECHA_REGISTRO)
    PerdidaCosechas = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.Tipo_SEMILLA}"
    def __str__(self):
        return f"{self.Semillas}"



# Inventario de Cosecha
class invetarioCosecha(models.Model):
    tipo_cosecha = models.ForeignKey(admInventario, on_delete=models.CASCADE)
    TEMPORADAS = [
        ('Temporada 1','Temporada 1'),
        ('Temporada 2','Temporada 2'),
        ('Temporada 3','Temporada 3'),
        ('Temporada 4','Temporada 4'),
    ]
    temporada = models.CharField(max_length=100, choices=TEMPORADAS)

    def __str__(self):
        return f"{self.tipo_cosecha}, {self.temporada}"
    



# Inventario de Semilla
class semillaTipo(models.Model):
    Tipo_SEMILLA = [
        ('Alverja', 'Alverja'),
        ('Frijoles', 'Frijoles'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia'),
        ('Papa', 'Papa'),
        ('Aguacate', 'Aguacate'),
        ('Tomate', 'Tomate'),
        ('Mora', 'Mora'),
        ('Papaya', 'Papaya'),
        ('Uvas', 'Uvas'),
    ]
    tipoSemilla = models.CharField(max_length=100, choices=Tipo_SEMILLA)
    cantidad = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.tipoSemilla}"
    



class adminPerdidas(models.Model):
    TEMPORADAS = [
        ('Temporada 1','Temporada 1'),
        ('Temporada 2','Temporada 2'),
        ('Temporada 3','Temporada 3'),
        ('Temporada 4','Temporada 4'),
    ]
    tempo = models.CharField(max_length=100, choices=TEMPORADAS)
    cantidadPerdidas = models.CharField(max_length=10000)




# Reporte de administrador
class reportesadministrador(models.Model):
    tipo_Reporte = [
        ('Activos', 'Activo'),
        ('Pasivos', 'Pasivo'),
        ('Ganancias', 'Ganancia'),
    ]
    TEMPORADAS = [
        ('Temporada 1','Temporada 1'),
        ('Temporada 2','Temporada 2'),
        ('Temporada 3','Temporada 3'),
        ('Temporada 4','Temporada 4'),
    ]
    reporte = models.CharField(max_length=100,choices=tipo_Reporte)
    temporada = models. CharField(max_length=100, choices=TEMPORADAS)
    cantidadReporte = models.CharField(max_length=100000000)


    def __str__(self):
        return f"{self.reporte}"
    
