# Generated by Django 2.1.7 on 2019-08-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioastronomia', '0003_auto_20190807_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='RBW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_muestreo', models.IntegerField()),
                ('nfft', models.IntegerField()),
                ('rbw', models.FloatField()),
            ],
            options={
                'verbose_name': 'RBW',
                'verbose_name_plural': 'RBWs',
                'db_table': '',
                'ordering': ['rbw'],
                'managed': True,
            },
        ),
    ]
