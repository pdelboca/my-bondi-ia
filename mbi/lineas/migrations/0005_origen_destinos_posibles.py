# Generated by Django 2.1.3 on 2018-11-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0004_origen_linea'),
    ]

    operations = [
        migrations.AddField(
            model_name='origen',
            name='destinos_posibles',
            field=models.ManyToManyField(blank=True, related_name='_origen_destinos_posibles_+', to='lineas.Origen'),
        ),
    ]
