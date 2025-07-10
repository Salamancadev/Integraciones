from rest_framework import serializers
from .models import (
    Usuario, Terreno, Dron,
    ParametroFertilizacion, Ruta,
    Ejecucion, Reporte
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol']

class TerrenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terreno
        fields = '__all__'

class DronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dron
        fields = '__all__'

class ParametroFertilizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroFertilizacion
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class EjecucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejecucion
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'