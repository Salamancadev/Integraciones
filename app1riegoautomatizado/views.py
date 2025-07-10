from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cultivo, ZonaRiego, SensorHumedad, LecturaHumedad, Riego, PronosticoClima
from .serializers import CultivoSerializer, ZonaRiegoSerializer, SensorHumedadSerializer, LecturaHumedadSerializer, RiegoSerializer, PronosticoClimaSerializer

# Create your views here.
# Vista para listar y crear

#Cultivos
class CultivoListCreateView(generics.ListCreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class CultivoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

#Zona de riego

class ZonaRiegoListCreateView(generics.ListCreateAPIView):
    queryset = ZonaRiego.objects.all()
    serializer_class = ZonaRiegoSerializer

class ZonaRiegoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZonaRiego.objects.all()
    serializer_class = ZonaRiegoSerializer

#Sensor de humedad

class SensorHumedadListCreateView(generics.ListCreateAPIView):
    queryset = SensorHumedad.objects.all()
    serializer_class = SensorHumedadSerializer

class SensorHumedadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorHumedad.objects.all()
    serializer_class = SensorHumedadSerializer

#Lectura humedad
class LecturaHumedadListCreateView(generics.ListCreateAPIView):
    queryset = LecturaHumedad.objects.all()
    serializer_class = LecturaHumedadSerializer

class LecturaHumedadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LecturaHumedad.objects.all()
    serializer_class = LecturaHumedadSerializer

#Riego
class RiegoListCreateView(generics.ListCreateAPIView):
    queryset = Riego.objects.all()
    serializer_class = RiegoSerializer

class RiegoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Riego.objects.all()
    serializer_class = RiegoSerializer

#Pronostico Clima
class PronosticoClimaListCreateView(generics.ListCreateAPIView):
    queryset = PronosticoClima.objects.all()
    serializer_class = PronosticoClimaSerializer

class PronosticoClimaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PronosticoClima.objects.all()
    serializer_class = PronosticoClimaSerializer