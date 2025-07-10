from rest_framework import serializers
from .models import SensorHumedad, Medicion, Alerta, ConfiguracionRiego

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
