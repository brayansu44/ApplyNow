# Generated by Django 4.1.3 on 2022-12-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitar', '0016_remove_solicitudesentretenimientos_validacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudesaccesorios',
            name='validacion',
        ),
        migrations.RemoveField(
            model_name='solicitudesbalones',
            name='validacion',
        ),
        migrations.RemoveField(
            model_name='solicitudesequipos',
            name='validacion',
        ),
    ]
