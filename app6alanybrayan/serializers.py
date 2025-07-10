from rest_framework import serializers
from .models import historial, control

class historialSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial
        fields = ['id', 'mes', 'estado']

class controlSerializer(serializers.ModelSerializer):
    class Meta:
        model = control
        fields = ['id', 'temperatura', 'humedad', 'carbono']