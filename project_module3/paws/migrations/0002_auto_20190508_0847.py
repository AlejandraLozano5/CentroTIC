# Generated by Django 2.1.7 on 2019-05-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicedescriptor',
            name='ruleset_Ids',
            field=models.CharField(max_length=25),
        ),
    ]
