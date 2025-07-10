from rest_framework import serializers
from .models import Rol, Cultivo, Sensor, LecturaSensor, Cosecha, Alerta, Informe

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class LecturaSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaSensor
        fields = '__all__'

class CosechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosecha
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = '__all__'