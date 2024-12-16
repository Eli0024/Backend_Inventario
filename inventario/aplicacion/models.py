from django.db import models

# Modelo para registrar equipos


class RegistrarEquipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50, default='sin memoria')
    procesador = models.CharField(max_length=50, default='sin procesador')
    office = models.CharField(max_length=60)
    serial = models.CharField(max_length=60,  unique=True)
    windows = models.CharField(max_length=60)
    sistema_operativo = models.CharField(max_length=60)
    fecha_adquisicion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarUsuario', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='equipos/', null=True, blank=True)



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
    equipo = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)  # Preventivo, correctivo, etc.
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f"Mantenimiento de {self.equipo} - {self.fecha}"


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    area = models.CharField(max_length=50)  # Solicitud, carta, etc.
    
    def __str__(self):
        return self.nombre


# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    id_licencia = models.AutoField(primary_key=True) 
    correo = models.CharField(max_length=60)
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


class Nodo(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()  # Latitud de la ubicación
    longitud = models.FloatField()  # Longitud de la ubicación

    def __str__(self):
        return self.nombre

class Switch(models.Model):
    nodo = models.ForeignKey(Nodo, related_name='switches', on_delete=models.CASCADE)
    direccion_ip = models.CharField(max_length=15)
    descripcion = models.TextField()

    def __str__(self):
        return f"Switch en {self.nodo.nombre}"

class Conexion(models.Model):
    nodo_origen = models.ForeignKey(Nodo, related_name="origen", on_delete=models.CASCADE)
    nodo_destino = models.ForeignKey(Nodo, related_name="destino", on_delete=models.CASCADE)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)
    tipo_conexion = models.CharField(max_length=50)  # Ej: fibra óptica
    estado = models.BooleanField(default=True)   # Por ejemplo, 'fibra óptica'

    def __str__(self):
        return f"Conexión de {self.nodo_origen.nombre} a {self.nodo_destino.nombre}"

    