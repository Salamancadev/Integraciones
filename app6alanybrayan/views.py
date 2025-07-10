from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import historial, control
from .serializers import historialSerializer, controlSerializer


class historialView(generics.ListCreateAPIView):
    queryset = historial.objects.all()
    serializer_class = historialSerializer


class controlView(generics.ListCreateAPIView):
    queryset = control.objects.all()
    serializer_class = controlSerializer

# Create your views here.
