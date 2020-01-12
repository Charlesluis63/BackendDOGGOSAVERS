# Generated by Django 3.0.1 on 2020-01-12 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos_usuarios', '0001_initial'),
        ('Mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad_aproximada',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.CreateModel(
            name='Mascota_Perdida_Encontrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_mascota', models.CharField(choices=[('PE', 'perdido'), ('EN', 'encontrado')], max_length=2)),
                ('sector_encuentro_perdida', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=300)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mascotas.Mascota')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota_En_Adopcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_juego', models.DecimalField(decimal_places=2, max_digits=4)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mascotas.Mascota')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota_Adoptada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('detalle', models.CharField(max_length=200)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mascotas.Mascota')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_usuarios.Usuario')),
            ],
        ),
    ]