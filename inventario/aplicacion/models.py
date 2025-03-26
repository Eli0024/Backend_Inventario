from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo para registrar usuario (ya heredado de AbstractUser)
class RegistrarUsuario(AbstractUser):
    def __str__(self):
        return self.username

# Modelo para registrar equipo
class RegistrarEquipo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, default='sin memoria')
    memoria = models.CharField(max_length=50, default='sin memoria')
    procesador = models.CharField(max_length=50, default='sin procesador')
    office = models.CharField(max_length=60)
    serial = models.CharField(max_length=60, unique=True)
    sistema_operativo = models.CharField(max_length=60)
    fecha_adquisicion = models.DateField()  # Usar DateField en lugar de CharField
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='equipos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.estado}"

# Modelo para registrar colaborador
class RegistrarColaborador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    empresa = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.empresa}"

# Modelo para registrar mantenimiento
class Mantenimiento(models.Model):
    equipo = models.CharField(max_length=50)
    fecha = models.DateField()  # Usar DateField
    tipo = models.CharField(max_length=50)  # Preventivo, correctivo, etc.
    descripcion = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)

    def __str__(self):
        return f"Mantenimiento de {self.equipo} - {self.fecha}"

# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    correo = models.CharField(max_length=60, default='sin memoria')
    contrasena = models.CharField(max_length=60)
    serial_office = models.CharField(max_length=60, default='sin serial')
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)

    def __str__(self):
        return self.correo

# Modelo para registrar impresoras    
class Impresora(models.Model):
    nombre = models.CharField(max_length=60)
    ip = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

# Modelo para registrar periféricos
class Perifericos(models.Model):
    nombre = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    numero_serie = models.CharField(max_length=60)
    fecha_adquisicion = models.DateField()  # Usar DateField en lugar de CharField
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
