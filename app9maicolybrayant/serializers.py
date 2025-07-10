from rest_framework import serializers
from .models import EstandarCalidad, LoteGrano, MedicionCalidad

class EstandarCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstandarCalidad
        fields = '__all__'

class LoteGranoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteGrano
        fields = '__all__'

class MedicionCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicionCalidad
        fields = '__all__'

