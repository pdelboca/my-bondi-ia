# Generated by Django 2.1.3 on 2018-11-27 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='color',
            field=models.CharField(default='', help_text='Color que representa a la empresa', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre_corto',
            field=models.CharField(blank=True, help_text='Nombre con el que se lo conoce en la práctica', max_length=30, null=True),
        ),
    ]
