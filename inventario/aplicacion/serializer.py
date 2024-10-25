from . models import RegistrarEquipo, RegistrarUsuario, RegistrarLicencia
from rest_framework import serializers

class RegistrarEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrar_equipos
        fields = '__all__'

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = '__all__'

class RegistrarLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = licencias
        fields = '__all__'        