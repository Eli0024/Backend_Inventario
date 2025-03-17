from django.db import models
from django.contrib.auth.models import AbstractUser

class RegistrarUsuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)  # Agrega un valor por defecto o elimínalo si no es obligatorio

    def __str__(self):
        return self.username


class RegistrarEquipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, default='sin memoria')
    memoria = models.CharField(max_length=50, default='sin memoria')
    procesador = models.CharField(max_length=50, default='sin procesador')
    office = models.CharField(max_length=60)
    serial = models.CharField(max_length=60,  unique=True)
    sistema_operativo = models.CharField(max_length=60)
    fecha_adquisicion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='equipos/', null=True, blank=True)



    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.estado}"

# Modelo para registrar usuarios
class RegistrarColaborador(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    empresa = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    licencia = models.OneToOneField('RegistrarLicencia', on_delete=models.CASCADE)  # Relación uno a uno

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.empresa}"


class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    equipo = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)  # Preventivo, correctivo, etc.
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f"Mantenimiento de {self.equipo} - {self.fecha}"


# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    id_licencia = models.AutoField(primary_key=True) 
    correo = models.CharField(max_length=60, default='sin memoria')
    contrasena = models.CharField(max_length=60)
    serial_office = models.CharField(max_length=60, default='sin serial') 


    def __str__(self):
        return self.correo

# Modelo para registrar mapa 
class RegistrarMapa(models.Model):
    id_mapa = models.AutoField(primary_key=True) 
    ubicacion_switches = models.CharField(max_length=60)
    fibra_optica = models.CharField(max_length=60)
    interconexion_de_nodo_a_nodo = models.CharField(max_length=60)


    def __str__(self):
        return self.nombre
    
class Impresora(models.Model):
    id_impre = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=60)
    ip = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Perifericos(models.Model):
    id_peri = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    numero_serie = models.CharField(max_length=60)
    fecha_adquisicion = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)