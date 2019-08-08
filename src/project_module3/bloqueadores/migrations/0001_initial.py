# Generated by Django 2.1.7 on 2019-08-07 15:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_id', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloqueadores.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Espectro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espectro_iq', django.contrib.postgres.fields.jsonb.JSONField(encoder='')),
                ('frec_central', models.FloatField()),
                ('samp_rate', models.FloatField()),
                ('fft_size', models.IntegerField()),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloqueadores.Dispositivos')),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosPrimarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia', models.FloatField()),
                ('nombre_emisora', models.CharField(max_length=100)),
                ('clase_emisora', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloqueadores.Ciudad')),
            ],
        ),
    ]
