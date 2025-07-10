from rest_framework import serializers
from .models import  Cultivo, ZonaRiego, SensorHumedad, LecturaHumedad, Riego, PronosticoClima



class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'

class ZonaRiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaRiego
        fields = '__all__'

class SensorHumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorHumedad
        fields = '__all__'

class LecturaHumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaHumedad
        fields = '__all__'

class RiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riego
        fields = '__all__'

class PronosticoClimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PronosticoClima
        fields = '__all__'