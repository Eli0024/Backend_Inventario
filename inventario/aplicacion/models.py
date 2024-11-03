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
    fecha_adquisicion = models.CharField(max_length=50)
    vida_util = models.IntegerField(null=True, blank=True)   
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


class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(RegistrarEquipo, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)  # Preventivo, correctivo, etc.
    descripcion = models.TextField()

    def __str__(self):
        return f"Mantenimiento de {self.equipo} - {self.fecha}"


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)  # Solicitud, carta, etc.
    archivo = models.FileField(upload_to='documentos/')
    fecha_subida = models.DateField(auto_now_add=True)
    equipo = models.ForeignKey(RegistrarEquipo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.fecha_subida}"


# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    id_licencia = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=60)
    contrasena = models.CharField(max_length=60)


    def __str__(self):
        return self.nombre

# Modelo para registrar mapa 
class RegistrarMapa(models.Model):
    id_mapa = models.AutoField(primary_key=True) 
    ubicacion_switches = models.CharField(max_length=60)
    fibra_optica = models.CharField(max_length=60)
    interconexion_de_nodo_a_nodo = models.CharField(max_length=60)


    def __str__(self):
        return self.nombre