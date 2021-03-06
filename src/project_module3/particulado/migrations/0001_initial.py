# Generated by Django 2.1.7 on 2019-08-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PMS5003A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muestra', models.CharField(max_length=100)),
                ('dato1', models.FloatField()),
                ('dato2', models.FloatField()),
                ('dato3', models.FloatField()),
            ],
            options={
                'verbose_name': 'PMS5003A',
                'db_table': '',
                'managed': True,
                'verbose_name_plural': 'PMS5003As',
            },
        ),
        migrations.CreateModel(
            name='PMS5003B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muestra', models.CharField(max_length=100)),
                ('dato1', models.FloatField()),
                ('dato2', models.FloatField()),
                ('dato3', models.FloatField()),
                ('temp', models.FloatField()),
                ('hum', models.FloatField()),
            ],
            options={
                'verbose_name': 'PMS5003B',
                'db_table': '',
                'managed': True,
                'verbose_name_plural': 'PMS5003Bs',
            },
        ),
    ]
