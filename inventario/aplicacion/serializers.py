from . models import MantenimientoImpresora, Perifericos, RegistrarColaborador, RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, Mantenimiento,Impresora,ContrasenaSiesa, ContrasenaAntivirus,ContrasenaVPN,ContrasenaServidor,ContrasenaEquipo, Empresa,CalendarioEvento,RegistroTarea
import re 
from rest_framework import serializers
from django.contrib.auth.models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = ['username','password', 'is_staff']  
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        user = RegistrarUsuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False)
        )
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    
class RegistroTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistroTarea
        fields=['id','fecha','descripcion']
        read_only_fields=['id','fecha']



#SERIALIZER EMPRESA
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id','nombre'] 

#SERIALIZER RESPONSABLE
class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarColaborador
        fields = ['id','nombre', 'apellido']          


class RegistrarEquipoSerializer(serializers.ModelSerializer):
    responsable = ResponsableSerializer(read_only=True)
    empresa=EmpresaSerializer(read_only=True)

    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=RegistrarColaborador.objects.none(),
        source='responsable',
        write_only=True,
        required=True
    )
    
    class Meta:
        model = RegistrarEquipo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and hasattr(request, "empresa_actual") and request.empresa_actual:
            self.fields["responsable_id"].queryset = RegistrarColaborador.objects.filter(
                empresa=request.empresa_actual
            )    
        
    
     
class RegistrarColaboradorSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(
        read_only=True,
    )
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa',
        write_only=True,
        required=True
    )

    class Meta:
        model = RegistrarColaborador
        fields = ['id', 'nombre', 'apellido','area','cargo' ,'empresa', 'empresa_id']

    

class RegistrarLicenciaSerializer(serializers.ModelSerializer):
    equipo = serializers.SerializerMethodField(read_only=True)
    empresa=EmpresaSerializer(read_only=True)
    
    equipo_id = serializers.PrimaryKeyRelatedField(
        queryset=RegistrarEquipo.objects.none(),
        source='equipo',
        write_only=True,
        required=False,   
        allow_null=True
    )

    class Meta:
        model = RegistrarLicencia
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True}
        }


    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        request = self.context.get("request")
        if request and hasattr(request, "empresa_actual") and request.empresa_actual:
            self.fields["equipo_id"].queryset = RegistrarEquipo.objects.filter(
                empresa=request.empresa_actual
            )

    def get_equipo(self, obj):
        if obj.equipo:
            return {
                "id": obj.equipo.id,
                "marca": obj.equipo.marca,
                "serial": obj.equipo.serial,
                "responsable": {
                    "id": obj.equipo.responsable.id,
                    "nombre": obj.equipo.responsable.nombre,
                    "apellido": obj.equipo.responsable.apellido
                },
                "empresa": {"id": obj.equipo.empresa.id, "nombre": obj.equipo.empresa.nombre
                }   
            }
        return None    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('equipo') is None:
            representation['equipo'] = self.get_equipo(instance)
        return representation
    
    

class ResponsableEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarColaborador
        fields = ['id','nombre', 'apellido']  

class EquipoSerializer(serializers.ModelSerializer):
    responsable = ResponsableEquipoSerializer()

    class Meta:
        model = RegistrarEquipo
        fields = ['id','marca', 'serial','responsable']

class MantenimientoSerializer(serializers.ModelSerializer):
    equipo = serializers.SerializerMethodField(read_only=True)
    empresa=EmpresaSerializer(read_only=True)
    
    equipo_id = serializers.PrimaryKeyRelatedField(
        queryset=RegistrarEquipo.objects.all(),
        source='equipo',
        write_only=True,
        required=True,
        allow_null=True
    )


    class Meta:
        model = Mantenimiento
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True},
        }

    def get_equipo(self, obj):
        if obj.equipo:
            return {
                "id": obj.equipo.id,
                "marca": obj.equipo.marca,
                "serial": obj.equipo.serial,
                "responsable": {
                    "id": obj.equipo.responsable.id,
                    "nombre": obj.equipo.responsable.nombre,
                    "apellido": obj.equipo.responsable.apellido
                },
                "empresa": {
                    "id": obj.equipo.empresa.id,
                    "nombre": obj.equipo.empresa.nombre
                }
            }
        return None

        

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

#CALENDARIO 
class CalendarioEventoSerializer(serializers.ModelSerializer):
    fecha_fin = serializers.DateTimeField(required=False, allow_null=True)
    color = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = CalendarioEvento
        fields = ('id',
            'titulo',
            'fecha_inicio',
            'fecha_fin',
            'color',)

#IMPRESORA
class ImpresoraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Impresora
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True},
        }
    
class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = '__all__'

class RegistrarPerifericoSerializer(serializers.ModelSerializer):
    responsable = ResponsableSerializer(read_only=True)
    empresa=EmpresaSerializer(read_only=True)
    # Para recibir solo el ID (POST/PUT)
    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=RegistrarColaborador.objects.all(),
        write_only=True,
        source='responsable',
        required=True
    )

    class Meta:
        model = Perifericos
        fields = '__all__'
        extra_kwargs = {
            'responsable': {'read_only': True},
            'empresa': {'read_only': True}
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    

class ImpresoraNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = ['id','nombre','direccion_ip'] 


class RegistrarMantenImpreSerializer(serializers.ModelSerializer):
    impresora = ImpresoraNombreSerializer(read_only=True)
    
    impresora_id = serializers.PrimaryKeyRelatedField(
        queryset=Impresora.objects.none(),
        write_only=True,
        source='impresora',
        required=True
    )
    
    class Meta:
        model = MantenimientoImpresora  
        fields = '__all__'
        extra_kwargs = {
            'impresora': {'read_only': True},
            'empresa': {'read_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and hasattr(request, "empresa_actual") and request.empresa_actual:
            self.fields["impresora_id"].queryset = Impresora.objects.filter(
                empresa=request.empresa_actual
            )    


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# Siesa
class ContrasenaSiesaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ContrasenaSiesa
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True}
        }
    

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
# Antivirus
class ContrasenaAntivirusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContrasenaAntivirus
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True}
        }


    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance  

# VPN
class ContrasenaVPNSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContrasenaVPN
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True}
        }


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# Servidor
class ContrasenaServidorSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = ContrasenaServidor
        fields = '__all__'
        extra_kwargs = {
            'empresa': {'read_only': True}
        }


    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ContrasenaEquipoSerializer(serializers.ModelSerializer):
    responsable = ResponsableSerializer(read_only=True)
    empresa=EmpresaSerializer(read_only=True) 
    
    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=RegistrarColaborador.objects.all(),
        write_only=True,
        source='responsable',
        required=True
    )

    class Meta:
        model = ContrasenaEquipo
        fields = '__all__'
        extra_kwargs = {
            'responsable': {'read_only': True},
            'empresa': {'read_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and hasattr(request, "empresa_actual") and request.empresa_actual:
            self.fields["responsable_id"].queryset = RegistrarColaborador.objects.filter(
                empresa=request.empresa_actual
            )    


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance