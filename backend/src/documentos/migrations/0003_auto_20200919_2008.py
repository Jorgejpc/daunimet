# Generated by Django 3.1.1 on 2020-09-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_auto_20200919_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre del documento', max_length=150, verbose_name='Nombre documento:'),
        ),
    ]
