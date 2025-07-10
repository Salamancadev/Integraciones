from rest_framework import serializers
from .models import Registro, InicioSecion, admInventario, adminGestio, adminPerdidas, invetarioCosecha, reportesadministrador, semillaTipo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('__all__')

class InisioSesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioSecion
        fields = ('__all__')

class AdminInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = admInventario
        fields = ('__all__')

class AdminGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = adminGestio
        fields = ('__all__')

class AdminPerdidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = adminPerdidas
        fields = ('__all__')

class InventarioCosechaSerializar(serializers.ModelSerializer):
    class Meta:
        model = invetarioCosecha
        fields = ('__all__')

class ReportesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = reportesadministrador
        fields = ('__all__')

class SemillaTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = semillaTipo
        fields = ('__all__')