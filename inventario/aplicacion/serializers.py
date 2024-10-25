from . models import RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, RegistrarMapa, Mantenimiento,Documento
from rest_framework import serializers

class RegistrarEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarEquipo
        fields = '__all__'

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = '__all__'

class RegistrarLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarLicencia
        fields = '__all__'        

class RegistrarMapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarMapa
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

