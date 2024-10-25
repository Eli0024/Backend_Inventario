from django.db import models

# Modelo para registrar equipos
class RegistrarEquipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=60)
    memoria = models.CharField(max_length=50)
    procesador = models.CharField(max_length=60)
    office = models.CharField(max_length=60)
    serial = models.CharField(max_length=60)
    serial_office = models.CharField(max_length=50)  
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarUsuario', on_delete=models.CASCADE)  
    archivo = models.FileField(upload_to='archivos/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.estado}"

# Modelo para registrar usuarios
class RegistrarUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    empresa = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    licencia = models.OneToOneField('RegistrarLicencia', on_delete=models.CASCADE)  # Relación uno a uno

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.empresa}"

# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    id_licencia = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=60)


    def __str__(self):
        return self.nombre
