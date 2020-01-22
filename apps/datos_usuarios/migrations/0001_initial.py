# Generated by Django 3.0.1 on 2020-01-22 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=25)),
                ('numero_contacto', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=15)),
                ('tipo_usuario', models.CharField(max_length=15)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_usuarios.Persona')),
            ],
        ),
    ]
