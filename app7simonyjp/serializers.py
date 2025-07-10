from rest_framework import serializers
from .models import Humedad, Luz, Temperatura

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = ['id', 'humedad_actual', 'humedad_maxima', 'humedad_minima', 'humedad_solicitada']
    
class LuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luz
        fields = ['id', 'luz_actual', 'luz_maxima', 'luz_minima', 'luz_solicitada']
    
class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = ['id', 'temperatura_actual', 'temperatura_maxima', 'temperatura_minima', 'temperatura_solicitada']