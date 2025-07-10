from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Medicion, Alerta
from .serializers import MedicionSerializer, AlertaSerializer

class MedicionList(generics.ListCreateAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class AlertaList(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer