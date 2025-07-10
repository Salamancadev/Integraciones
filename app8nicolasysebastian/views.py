from django.shortcuts import render
from rest_framework import generics
from .models import Rol, Cultivo, Sensor, LecturaSensor, Cosecha, Alerta, Informe
from .serializers import (
    RolSerializer, CultivoSerializer, SensorSerializer,
    LecturaSensorSerializer, CosechaSerializer, AlertaSerializer, InformeSerializer
)

class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

#class UsuarioListCreateView(generics.ListCreateAPIView):
    #queryset = Usuario.objects.all()
    #serializer_class = UsuarioSerializer

#class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Usuario.objects.all()
    #serializer_class = UsuarioSerializer

class CultivoListCreateView(generics.ListCreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class CultivoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class LecturaSensorListCreateView(generics.ListCreateAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer

class LecturaSensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer

class CosechaListCreateView(generics.ListCreateAPIView):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer

class CosechaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer

class AlertaListCreateView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class InformeListCreateView(generics.ListCreateAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer

class InformeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer
