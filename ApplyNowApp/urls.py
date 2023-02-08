
from django.contrib import admin
from django.urls import path, include
from ApplyNowApp import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('loguear', views.loguear),
    path('cerrar_sesion', views.cerrar_sesion),
    path('perfil', views.perfil, name="Perfil"),
    path('changedate', views.changedate),
    path('change_password', views.change_password),
    path('contacto', views.contacto),
    path('recover', views.recover, name="Recover"),
    path('recovermsg', views.recovermsg),
    path('confirmedrecover/<str:userP>', views.confirmedrecover, name="ConfirmedRecover"),
    path('recoversuccess/<str:userP>', views.recoversuccess, name="Recoversuccess"),
    
]
