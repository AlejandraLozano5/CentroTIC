# Generated by Django 2.1.7 on 2019-08-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioastronomia', '0005_auto_20190813_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicasantena',
            name='vswr',
            field=models.ImageField(blank=True, upload_to='album/vswr'),
        ),
    ]
