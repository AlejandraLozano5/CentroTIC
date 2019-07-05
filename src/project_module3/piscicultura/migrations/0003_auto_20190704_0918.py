# Generated by Django 2.1.7 on 2019-07-04 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piscicultura', '0002_voltajebateria_pozo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperaturaCaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('valor', models.FloatField()),
                ('pozo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piscicultura.Pozo')),
            ],
        ),
        migrations.CreateModel(
            name='TomaDatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='TemperaturaAmbiente',
            new_name='HumedadCaja',
        ),
    ]