from django.contrib import admin
from django.urls import path
from Solicitar import views
from ApplyNowApp.views import index 
urlpatterns = [
    path('equipos', views.equipos, name="Equipos"),
    path('solicitar_equipo/<str:serial_equipo>', views.solicitarEquipo, name="Solicitar_equipo"),
    path('solicitud_equipo/<str:serial_equipo>', views.solicitudEquipo, name="Solicitud_equipo"),
    path('solicitudes_equipos', views.solicitudesEquipo, name="Solicitudes_equipos"),
    path('entregar_equipo/<str:serial_equipo>', views.entregarEquipo, name="Entregar_equipo"),
    path('historial_equipos', views.historialEquipo, name="Historial_equipos"),

    path('balones', views.balones, name="Balones"),
    path('solicitar_balon/<int:id_balon>', views.solicitarBalon, name="Solicitar_balon"),
    path('solicitud_balon/<int:id_balon>', views.solicitudBalon, name="Solicitud_balon"),
    path('solicitudes_balones', views.solicitudesBalon, name="Solicitudes_balones"),
    path('entregar_balon/<str:tipo_balon>', views.entregarBalon, name="Entregar_balon"),
    path('historial_balones', views.historialBalon, name="Historial_balones"),

    path('accesorios', views.accesorios, name="Accesorios"),
    path('solicitar_accesorio/<int:id_accesorio>', views.solicitarAccesorio, name="Solicitar_accesorio"),
    path('solicitud_accesorio', views.solicitudAccesorio, name="Solicitud_accesorio"),
    path('solicitudes_accesorios', views.solicitudesAccesorio, name="Solicitudes_accesorios"),
    path('entregar_accesorio', views.entregarAccesorio, name="Entregar_accesorio"),
    path('historial_accesorio', views.historialAccesorio, name="Historial_accesorio"),

    path('entretenimiento', views.entretenimiento, name="Entretenimiento"),
    path('solicitar_entretenimiento/<int:id_entretenimiento>', views.solicitarEntretenimiento, name="Solicitar_entretenimiento"),
    path('solicitud_entretenimiento', views.solicitudEntretenimiento, name="Solicitud_entretenimiento"),
    path('solicitudes_entretenimiento', views.solicitudesEntretenimiento, name="Solicitudes_entretenimiento"),
    path('entregar_entretenimiento', views.entregarEntretenimiento, name="Entregar_entretenimiento"),
    path('historial_entretenimiento', views.historialEntretenimiento, name="Historial_entretenimiento"),

    
]