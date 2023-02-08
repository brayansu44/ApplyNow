from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Perfil, PerfilAdmin)    

