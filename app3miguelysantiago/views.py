
from django.shortcuts import render

# Create your views here.

from .models import Registro, InicioSecion, admInventario, adminGestio, adminPerdidas, invetarioCosecha, reportesadministrador, semillaTipo
from rest_framework import generics
from .serializers import UsuarioSerializer, InisioSesionSerializer, AdminInventarioSerializer, AdminGestionSerializer, AdminPerdidasSerializer, InventarioCosechaSerializar, ReportesAdminSerializer, SemillaTipoSerializer


# ------Registro------  
class RegistroGetViewSet(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer

class RegistroUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer




# ----Inicio Sesion----
class iniciaSecioViewSet(generics.ListCreateAPIView):
    queryset = InicioSecion.objects.all() 
    serializer_class = InisioSesionSerializer

class iniciaSecioUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = InicioSecion.objects.all()   
    serializer_class = InisioSesionSerializer



# ----Inventario de Administrador----
class AdminInventarioViewSet(generics.ListCreateAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer

class AdminInventarioUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer




# ----Gestion de Administrador----
class AdminGestionViewSet(generics.ListCreateAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer

class AdminGestionUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer




# ----Perdidas de Administrador----
class AdminPerdidasViewSet(generics.ListCreateAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer

class AdminPerdidasUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer





# ----Inventario de Cosechas----
class InventarioCosechaViewSet(generics.ListCreateAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar

class InventarioCosechaUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar




# ----Reporte de Administrador----
class ReporteAdminViewSet(generics.ListCreateAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer

class ReporteAdminUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer




# ----Tipo de semilla----
class SemillaViewSet(generics.ListCreateAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer

class SemillaUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer




