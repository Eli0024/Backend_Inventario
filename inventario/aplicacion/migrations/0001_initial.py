# Generated by Django 5.1.2 on 2024-10-25 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarEquipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=60)),
                ('memoria', models.CharField(max_length=50)),
                ('procesador', models.CharField(max_length=60)),
                ('office', models.CharField(max_length=60)),
                ('serial', models.CharField(max_length=60)),
                ('serial_office', models.CharField(max_length=50)),
                ('fecha_adquisicion', models.DateField(blank=True, null=True)),
                ('vida_util', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(max_length=50)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarLicencia',
            fields=[
                ('id_licencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('contraseña', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarMapa',
            fields=[
                ('id_mapa', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion_switches', models.CharField(max_length=60)),
                ('fibra_optica', models.CharField(max_length=60)),
                ('interconexion_de_nodo_a_nodo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_mantenimiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.registrarequipo')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('fecha_subida', models.DateField(auto_now_add=True)),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.registrarequipo')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarUsuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('empresa', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('licencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.registrarlicencia')),
            ],
        ),
        migrations.AddField(
            model_name='registrarequipo',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.registrarusuario'),
        ),
    ]