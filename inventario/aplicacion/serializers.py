from . models import Conexion, Nodo, RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, RegistrarMapa, Mantenimiento,Impresora, Switch
from rest_framework import serializers


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = ['nombre', 'apellido']  # Puedes incluir otros campos si los necesitas


class RegistrarEquipoSerializer(serializers.ModelSerializer):
   

    responsable = ResponsableSerializer() 


    class Meta:
        model = RegistrarEquipo
        fields = '__all__'

    
    # responsable = serializers.PrimaryKeyRelatedField(queryset=RegistrarUsuario.objects.all())
    def create(self, validated_data):
        responsable_data = validated_data.pop('responsable')  # Extraer datos del campo anidado
        responsable_instance, created = RegistrarUsuario.objects.get_or_create(**responsable_data)
        equipo = RegistrarEquipo.objects.create(responsable=responsable_instance, **validated_data)
        return equipo
    
     
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

