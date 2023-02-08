from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    cargo=(
        ('Estudiante','Estudiante'),
        ('Docente','Docente'),
        ('Administrador','Administrador'),
    )
    cargo=models.CharField(max_length=150, choices=cargo, default='Estudiante')
    telefono=models.CharField(max_length=50, null=False)
    tipo=(
        ('Cedula','Cedula'),
        ('T.I.','T.I.'),
        ('Pasaporte','Pasaporte'),
    )
    tipo=models.CharField(max_length=150, choices=tipo, default='Cedula')
    documento=models.IntegerField()
    ValidacionEquipo=models.BooleanField(default=False)
    ValidacionBalon=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'

    def __str__(self):
        return self.user.username