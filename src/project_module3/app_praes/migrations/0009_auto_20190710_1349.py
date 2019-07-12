# Generated by Django 2.1.7 on 2019-07-10 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_praes', '0008_sensores_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flujo_agua',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='humedad',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='ph_agua',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='presionatmosferica',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='temperatura_agua',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
        migrations.AlterField(
            model_name='turbidez_agua',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_praes.Kit'),
        ),
    ]
