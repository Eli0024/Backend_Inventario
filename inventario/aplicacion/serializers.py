from . models import Conexion, Nodo, RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, RegistrarMapa, Mantenimiento,Impresora, Switch
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

class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = '__all__'

class MapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarMapa
        fields = '__all__'

class NodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodo
        fields = '__all__'

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class ConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conexion
        fields = '__all__'

