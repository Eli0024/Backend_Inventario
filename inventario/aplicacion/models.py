from django.db import models
from django.contrib.auth.models import AbstractUser


class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    activa = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    color_gradient = models.CharField(max_length=250, null=True,blank=True)

    def __str__(self):
        return self.nombre

class RegistrarUsuario(AbstractUser):
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class RegistroTarea(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE,null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    class Meta:
        ordering = ['-fecha'] 

    def __str__(self):
        return f"{self.fecha} - {self.descripcion[:500]}"     


# Modelo para registrar equipo
class RegistrarEquipo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, default='sin memoria')
    memoria = models.CharField(max_length=50, default='sin memoria')
    procesador = models.CharField(max_length=50, default='sin procesador')
    office = models.CharField(max_length=60)
    serial = models.CharField(max_length=60, unique=True)
    sistema_operativo = models.CharField(max_length=60)
    fecha_adquisicion = models.DateField()  
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    archivo = models.FileField(upload_to='equipos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.estado}"

# Modelo para registrar colaborador
class RegistrarColaborador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    area = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.empresa}"

# Modelo para registrar mantenimiento
class Mantenimiento(models.Model):
    TIPO_MANTENIMIENTO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
        ('predictivo', 'Predictivo'),
    ]
    
    TIPO_SERVICIO_CHOICES = [
        ('software', 'Software'),
        ('hardware', 'Hardware'),
        ('ambos', 'Software y Hardware'),
    ]
    
    equipo = models.ForeignKey('RegistrarEquipo', on_delete=models.CASCADE, help_text="Equipo al que se le realizó el mantenimiento")
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=20, choices=TIPO_MANTENIMIENTO_CHOICES, default='preventivo')
    tipo_servicio = models.CharField(max_length=20, choices=TIPO_SERVICIO_CHOICES, default='software')
    descripcion = models.TextField(max_length=500)
    realizado_por = models.CharField(max_length=100,default='')
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Mantenimiento {self.get_tipo_mantenimiento_display()} - {self.equipo} - {self.fecha_mantenimiento}"
    

class CalendarioEvento(models.Model):
    COLOR_CHOICES = [
        ("#3593F1", 'Azul'),
        ('#28a745', 'Verde'),
        ('#dc3545', 'Rojo'),
        ('#ffc107', 'Amarillo'),
        ('#6f42c1', 'Morado'),
    ]

    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True,blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='#1E90FF',null=True,blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha_inicio} - {self.fecha_fin})"   

# Modelo para registrar licencias
class RegistrarLicencia(models.Model):
    TIPO_LICENCIA_CHOICES = [
        ('office', 'Microsoft Office'),
        ('project_2013', 'Microsoft Project 2013'),
        ('project_2019', 'Microsoft Project 2019'),
        ('visio', 'Microsoft Visio'),
        ('antivirus', 'Antivirus'),
        ('windows', 'Windows'),
        ('autocad 2019', 'AutoCAD 2019'),
        ('autocad 2024', 'AutoCAD 2024'),
        ('otros', 'Otros'),
    ]
    
    tipo_licencia = models.CharField(max_length=20, choices=TIPO_LICENCIA_CHOICES, default='office')
    correo = models.CharField(max_length=60, default='sin correo',null=True,blank=True)
    contrasena = models.CharField(max_length=60,null=True,blank=True)
    clave_producto = models.CharField(max_length=100, default='sin clave')
    fecha_compra = models.DateField(null=True, blank=True)
    equipo = models.ForeignKey('RegistrarEquipo', on_delete=models.CASCADE,null=True,blank=True, 
                              help_text="Equipo al que está asignada la licencia")
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_licencia_display()} - {self.correo}"
    
    

# Modelo para registrar impresoras    
class Impresora(models.Model):
    nombre = models.CharField(max_length=60)
    direccion_ip = models.CharField(max_length=60)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class MantenimientoImpresora(models.Model):
    impresora = models.ForeignKey('Impresora', on_delete=models.CASCADE, related_name='mantenimientos')
    fecha = models.DateField()
    descripcion = models.TextField()
    realizado_por = models.CharField(max_length=100, blank=True)  
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Mantenimiento de {self.impresora} el {self.fecha}"
    

# Modelo para registrar periféricos
class Perifericos(models.Model):
    nombre = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    numero_serie = models.CharField(max_length=60)
    fecha_adquisicion = models.DateField() 
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

# Contraseña Siesa
class ContrasenaSiesa(models.Model):
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='contrasenas/siesa/', null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.usuario

# Contraseña Antivirus
class ContrasenaAntivirus(models.Model):
    link = models.URLField(max_length=200, blank=True)
    archivo = models.FileField(upload_to='contrasenas/antivirus/', null=True, blank=True)
    descripcion = models.TextField(blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Antivirus - {self.link or 'Sin link'}"

# Contraseña VPN
class ContrasenaVPN(models.Model):
    direccion_ip = models.GenericIPAddressField()
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='contrasenas/vpn/', null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.direccion_ip}"

# Contraseña Servidores (puedes diferenciar el tipo con un campo)
class ContrasenaServidor(models.Model):
    TIPO_CHOICES = [
        ('datos', 'Servidor de Datos'),
        ('solido', 'Servidor Sólido Fequiva'),
        ('lineas', 'Servidor Líneas Telefónicas'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    direccion_ip = models.GenericIPAddressField()
    contrasena = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='contrasenas/servidores/', null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.direccion_ip}"

# Contraseña Equipos
class ContrasenaEquipo(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.EmailField(null=True, blank=True)
    contrasena = models.CharField(max_length=100)
    responsable = models.ForeignKey('RegistrarColaborador', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='contrasenas/equipos/', null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.correo}"


