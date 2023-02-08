from django.contrib import admin

from .models import *

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class BalonAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class AccesorioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class EntretenimientoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class SolicitudesEquiposAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class SolicitudesBalonesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class SolicitudesAccesoriosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class SolicitudesEntretenimientosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
  

admin.site.register(Equipo, EquipoAdmin)    
admin.site.register(Balon, BalonAdmin)
admin.site.register(Accesorio, AccesorioAdmin)    
admin.site.register(Entretenimiento, EntretenimientoAdmin)
admin.site.register(solicitudesEquipos, SolicitudesEquiposAdmin)
admin.site.register(solicitudesBalones, SolicitudesBalonesAdmin)
admin.site.register(solicitudesAccesorios, SolicitudesAccesoriosAdmin)
admin.site.register(solicitudesEntretenimientos, SolicitudesEntretenimientosAdmin)
admin.site.register(historialEquipos)
admin.site.register(historialBalones)
admin.site.register(historialAccesorios)
admin.site.register(historialEntretenimientos)