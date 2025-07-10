from django.urls import path
from rest_framework import generics
from .models import Humedad, Luz, Temperatura
from .serializers import HumedadSerializer, LuzSerializer, TemperaturaSerializer
# Create your views here.

class Humedadgenerics(generics.ListCreateAPIView):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer

class Luzgenerics(generics.ListCreateAPIView):
    queryset = Luz.objects.all()
    serializer_class = LuzSerializer

class Temperaturagenerics(generics.ListCreateAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer


