# Generated by Django 4.1 on 2022-11-22 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(choices=[('Estudiante', 'Estudiante'), ('Docente', 'Docente'), ('Administrador', 'Administrador')], default='Estudiante', max_length=150)),
                ('telefono', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('Cedula', 'Cedula'), ('T.I.', 'T.I.'), ('Pasaporte', 'Pasaporte')], default='Cedula', max_length=150)),
                ('documento', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
            },
        ),
    ]