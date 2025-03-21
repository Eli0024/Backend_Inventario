# Generated by Django 5.1.2 on 2025-01-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_registrarcolaborador_delete_custom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrarusuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registrarusuario',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='registrarusuario',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
