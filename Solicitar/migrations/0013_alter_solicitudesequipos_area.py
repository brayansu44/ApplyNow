# Generated by Django 4.1 on 2022-12-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitar', '0012_alter_solicitudesaccesorios_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudesequipos',
            name='area',
            field=models.CharField(choices=[('Prestamo', 'Prestamo'), ('Área Comercial', 'Área Comercial'), ('Área Financiera', 'Área Financiera'), ('Área Administrativa', 'Área Administrativa'), ('Área Academica', 'Área Academica')], max_length=150),
        ),
    ]
