from django.db import models
from ApplyNowApp.models import *

# Create your models here.
class Equipo(models.Model):
    serial=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    cargador=models.BooleanField(default=True)
    disponibilidad=models.BooleanField(default=True)
    area=(
        ('Prestamo','Prestamo'),
        ('Área Comercial','Área Comercial'),
        ('Área Financiera','Área Financiera'),
        ('Área Administrativa','Área Administrativa'),
        ('Área Academica','Área Academica'),
    )
    area=models.CharField(max_length=150, choices=area, default='Prestamo')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='equipo'
        verbose_name_plural='equipos'

    def __str__(self):
        return self.serial

class Balon(models.Model):
    tipo=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='balon'
        verbose_name_plural='balones'

    def __str__(self):
        return self.tipo

class Accesorio(models.Model):
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='accesorio'
        verbose_name_plural='accesorios'

    def __str__(self):
        return self.tipo

class Entretenimiento(models.Model):
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='entretenimiento'
        verbose_name_plural='entretenimientos'

    def __str__(self):
        return self.tipo

class solicitudesEquipos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    serial=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    cargador=models.BooleanField()
    area=(
        ('Prestamo','Prestamo'),
        ('Área Comercial','Área Comercial'),
        ('Área Financiera','Área Financiera'),
        ('Área Administrativa','Área Administrativa'),
        ('Área Academica','Área Academica'),
    )
    area=models.CharField(max_length=150, choices=area)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes de equipos'

    def __str__(self):
        return self.user.username
        
class solicitudesBalones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes de balones'

    def __str__(self):
        return self.user.username

class solicitudesAccesorios(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes de accesorios'

    def __str__(self):
        return self.user.username

class solicitudesEntretenimientos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes de entretenimientos'

    def __str__(self):
        return self.user.username

class historialEquipos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    serial=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    cargador=models.BooleanField()
    area=(
        ('Prestamo','Prestamo'),
        ('Área Comercial','Área Comercial'),
        ('Área Financiera','Área Financiera'),
        ('Área Administrativa','Área Administrativa'),
        ('Área Academica','Área Academica'),
    )
    area=models.CharField(max_length=150, choices=area)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='historial'
        verbose_name_plural='historial de equipos'

    def __str__(self):
        return self.user.username


class historialBalones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name='historial'
        verbose_name_plural='historial de balones'

    def __str__(self):
        return self.user.username

class historialAccesorios(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name='historial'
        verbose_name_plural='historial de accesorios'

    def __str__(self):
        return self.user.username

class historialEntretenimientos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name='historial'
        verbose_name_plural='historial de entretenimientos'

    def __str__(self):
        return self.user.username        
