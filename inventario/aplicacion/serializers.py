from . models import MantenimientoImpresora, Perifericos, RegistrarColaborador, RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, Mantenimiento,Impresora
from rest_framework import serializers
from django.contrib.auth.models import User


class userSerializer(serializers.ModelSerializer):
     class Meta:
         model = RegistrarUsuario
         fields = ['username','password','is_staff']
        
         extra_kwargs = {
             'is_staff': {'read_only': False}, 
         }
        
         def create(self, validated_data):
             user = RegistrarUsuario.objects.create_user(
                 username=validated_data['username'],
                 password=validated_data['password']
             )
             if 'is_staff' in validated_data:
                 user.is_staff = validated_data['is_staff']
                 user.save()
             return user
        

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarColaborador
        fields = ['nombre', 'apellido']  # Puedes incluir otros campos si los necesitas


class RegistrarEquipoSerializer(serializers.ModelSerializer):
   

    responsable = ResponsableSerializer() 


    class Meta:
        model = RegistrarEquipo
        fields = '__all__'

    
    # responsable = serializers.PrimaryKeyRelatedField(queryset=RegistrarUsuario.objects.all())
    def create(self, validated_data):
        responsable_data = validated_data.pop('responsable')  # Extraer datos del campo anidado
        responsable_instance, created = RegistrarColaborador.objects.get_or_create(**responsable_data)
        equipo = RegistrarEquipo.objects.create(responsable=responsable_instance, **validated_data)
        return equipo
    
     
class RegistrarColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarColaborador
        fields = '__all__'

class RegistrarLicenciaSerializer(serializers.ModelSerializer):
    
    responsable = ResponsableSerializer() 


    class Meta:
        model = RegistrarLicencia
        fields = '__all__'

    
    # responsable = serializers.PrimaryKeyRelatedField(queryset=RegistrarUsuario.objects.all())
    def create(self, validated_data):
        responsable_data = validated_data.pop('responsable')  # Extraer datos del campo anidado
        responsable_instance, created = RegistrarColaborador.objects.get_or_create(**responsable_data)
        licencia = RegistrarLicencia.objects.create(responsable=responsable_instance, **validated_data)
        return licencia        


class MantenimientoSerializer(serializers.ModelSerializer):
    responsable = ResponsableSerializer() 


    class Meta:
        model = Mantenimiento
        fields = '__all__'

    
    # responsable = serializers.PrimaryKeyRelatedField(queryset=RegistrarUsuario.objects.all())
    def create(self, validated_data):
        responsable_data = validated_data.pop('responsable')  # Extraer datos del campo anidado
        responsable_instance, created = RegistrarColaborador.objects.get_or_create(**responsable_data)
        mantenimiento = Mantenimiento.objects.create(responsable=responsable_instance, **validated_data)
        return mantenimiento

class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = '__all__'

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = '__all__'

class RegistrarPerifericoSerializer(serializers.ModelSerializer):

    responsable = ResponsableSerializer()

    class Meta:
        model = Perifericos
        fields = '__all__'        

    def create(self, validated_data):
        responsable_data = validated_data.pop('responsable')  # Extraer datos del campo anidado
        responsable_instance, created = RegistrarColaborador.objects.get_or_create(**responsable_data)
        periferico = Perifericos.objects.create(responsable=responsable_instance, **validated_data)
        return periferico
    

class ImpresoraNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = ['nombre']     

class RegistrarMantenImpreSerializer(serializers.ModelSerializer):
    
    impresora = ImpresoraNombreSerializer()  # Campo anidado para los datos de la impresora

    class Meta:
        model = MantenimientoImpresora  # Asegúrate de que este sea el modelo correcto
        fields = '__all__'

    def create(self, validated_data):
        # 1. Extrae los datos de la impresora (no 'nombre')
        impresora_data = validated_data.pop('impresora')  # ¡Corregido!
        
        # 2. Busca o crea la Impresora (no MantenimientoImpresora)
        impresora_instance, created = Impresora.objects.get_or_create(**impresora_data)
        
        # 3. Crea el MantenimientoImpresora con la impresora asociada
        mantenimiento = MantenimientoImpresora.objects.create(
            impresora=impresora_instance,
            **validated_data
        )
        return mantenimiento
    