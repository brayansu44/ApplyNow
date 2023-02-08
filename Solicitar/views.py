
from django.shortcuts import render, redirect
from .models import *
from ApplyNowApp.models import *
from django.contrib import messages
from django.http.response import JsonResponse 

#variables

# Create your views here.
# Equipos
def equipos(request):
    if request.user.is_authenticated:
        perfil=Perfil.objects.filter(user=request.user).first()
        if perfil.ValidacionEquipo:
            messages.warning(request, "Ya tienes un equipo solicitado.")
            return redirect("Index")
        else:
            equipos=Equipo.objects.all()
            return render(request, "equipos/equipos.html", {"equipos":equipos})
    else:
        return redirect("Index")

def solicitarEquipo(request, serial_equipo):
    if request.user.is_authenticated:
        perfilUsuario=Perfil.objects.filter(user=request.user).first()
        equipo=Equipo.objects.filter(serial=serial_equipo).first()
        return render(request, "equipos/solicitar_equipo.html", {"perfil_usuario":perfilUsuario, "equipo":equipo})
    else:
        return redirect("Index")

def historialEquipo(request):
    if request.user.is_authenticated:
        historial = historialEquipos.objects.all()
        return render(request, "equipos/historial.html", {"historial":historial})
    else:
        return redirect("Index")    

# Balones
def balones(request):
    if request.user.is_authenticated:
        perfil=Perfil.objects.filter(user=request.user).first()
        if perfil.ValidacionBalon:
            messages.warning(request, "Ya tienes un balon solicitado.")
            return redirect("Index")
        else:
            balones=Balon.objects.all()
            return render(request, "balones/balones.html", {"balones":balones})
    else:
        return redirect("Index")

def solicitarBalon(request, id_balon):
    if request.user.is_authenticated:
        perfilUsuario=Perfil.objects.filter(user=request.user).first()
        balon=Balon.objects.filter(id=id_balon).first()
        return render(request, "balones/solicitar_balon.html", {"perfil_usuario":perfilUsuario, "balon":balon})
    else:
        return redirect("Index")

def historialBalon(request):
    if request.user.is_authenticated:
        historial = historialBalones.objects.all()
        return render(request, "balones/historial.html", {"historial":historial})
    else:
        return redirect("Index")             



# Entretenimiento
def entretenimiento(request):
    if request.user.is_authenticated:
        entretenimientos=Entretenimiento.objects.all()
        return render(request, "entretenimiento/entretenimiento.html", {"entretenimientos":entretenimientos})
    else:
        return redirect("Index")

def solicitarEntretenimiento(request, id_entretenimiento):
    if request.user.is_authenticated:
        perfilUsuario=Perfil.objects.filter(user=request.user).first()
        entretenimiento=Entretenimiento.objects.filter(id=id_entretenimiento).first()
        return render(request, "entretenimiento/solicitar_entretenimiento.html", {"perfil_usuario":perfilUsuario, "entretenimiento":entretenimiento})
    else:
        return redirect("Index")

def historialEntretenimiento(request):
    if request.user.is_authenticated:
        historial = historialEntretenimientos.objects.all()
        return render(request, "entretenimiento/historial.html", {"historial":historial})
    else:
        return redirect("Index")  


# accesorios
def accesorios(request):
    if request.user.is_authenticated:
        accesorios=Accesorio.objects.all()
        return render(request, "accesorios/accesorios.html", {"accesorios":accesorios})
    else:
        return redirect("Index")

def solicitarAccesorio(request, id_accesorio):
    if request.user.is_authenticated:
        perfilUsuario=Perfil.objects.filter(user=request.user).first()
        accesorio=Accesorio.objects.filter(id=id_accesorio).first()
        return render(request, "accesorios/solicitar_accesorio.html", {"perfil_usuario":perfilUsuario, "accesorio":accesorio})
    else:
        return redirect("Index")

def historialAccesorio(request):
    if request.user.is_authenticated:
        historial = historialAccesorios.objects.all()
        return render(request, "accesorios/historial.html", {"historial":historial})
    else:
        return redirect("Index") 

#Solicitudes
def solicitudEquipo(request, serial_equipo):
    if request.user.is_authenticated:
        perfil=Perfil.objects.filter(user=request.user).first()
        cantidadSolicitudes1=solicitudesEquipos.objects.all()
        cantidadSolicitudes2=solicitudesBalones.objects.all()
        cantidadSolicitudes3=solicitudesAccesorios.objects.all()
        cantidadSolicitudes4=solicitudesEntretenimientos.objects.all()
        cantidadSolicitudes = len(cantidadSolicitudes1) + len(cantidadSolicitudes2) + len(cantidadSolicitudes3) + len(cantidadSolicitudes4)


        equipo=Equipo.objects.filter(serial=serial_equipo).first()
        Notificador=0
        if equipo.disponibilidad:
            equipo.disponibilidad=False
            equipo.save()
            serial=request.POST.get('serial')
            marca=request.POST.get('marca')
            cargador=request.POST.get('cargador')

            if cargador == "si":
                cargador=True

            elif cargador == "no":
                cargador=False    

            area=request.POST.get('area')

            solicitudesEquipos.objects.create(user=request.user,serial=serial, marca=marca, cargador=cargador, area=area)
            perfil.ValidacionEquipo=True
            perfil.save()
            messages.success(request, "Solicitud Enviada Correctamente")

            return redirect("Index")
        else:
            Notificador+=2
            messages.error(request, "Este equipo no esta disponible")
            
            return render(request, "index.html", {"Notificador":Notificador, "perfil":perfil, "cantidad_solicitudes":cantidadSolicitudes, "Qequipo":len(cantidadSolicitudes1), "Qbalon":len(cantidadSolicitudes2), "Qaccesorio":len(cantidadSolicitudes3), "Qentretenimiento":len(cantidadSolicitudes4)})     
    else:
        return redirect("Index")

def solicitudBalon(request, id_balon):
    if request.user.is_authenticated:
        perfil=Perfil.objects.filter(user=request.user).first()
        cantidadSolicitudes1=solicitudesEquipos.objects.all()
        cantidadSolicitudes2=solicitudesBalones.objects.all()
        cantidadSolicitudes3=solicitudesAccesorios.objects.all()
        cantidadSolicitudes4=solicitudesEntretenimientos.objects.all()
        cantidadSolicitudes = len(cantidadSolicitudes1) + len(cantidadSolicitudes2) + len(cantidadSolicitudes3) + len(cantidadSolicitudes4)
        
        Notificador=0
        balon=Balon.objects.filter(id=id_balon).first()
        if balon.disponibilidad:
            tipo=request.POST.get('tipo')
            marca=request.POST.get('marca')
            color=request.POST.get('color')
            cantidad=request.POST.get('cantidad')
            solicitudesBalones.objects.create(user=request.user, tipo=tipo, marca=marca, color=color, cantidad=cantidad)
            balon.cantidad=balon.cantidad-1
            balon.save()
            if balon.cantidad==0:
                balon.disponibilidad=False
                balon.save()
            perfil.ValidacionBalon=True
            perfil.save()
            messages.success(request, "Solicitud Enviada Correctamente")
            return redirect("Index")
        else:
            Notificador+=2
            messages.error(request, "Este balon no esta disponible")

            return render(request, "index.html", {"Notificador":Notificador, "perfil":perfil, "cantidad_solicitudes":cantidadSolicitudes, "Qequipo":len(cantidadSolicitudes1), "Qbalon":len(cantidadSolicitudes2), "Qaccesorio":len(cantidadSolicitudes3), "Qentretenimiento":len(cantidadSolicitudes4)})  
    else:
        return redirect("Index")        

def solicitudAccesorio(request):
    if request.user.is_authenticated:

        Notificador=0
        id_accesorio=int(request.POST.get('accesorio_id'))
        accesorio_qty=int(request.POST.get('accesorio_qty'))
        accesorio_tipo=(request.POST.get('accesorio_tipo'))
        accesorio=Accesorio.objects.filter(id=id_accesorio).first()
        if accesorio.disponibilidad:
            solicitudesAccesorios.objects.create(user=request.user, tipo=accesorio_tipo, cantidad=accesorio_qty)
            accesorio.cantidad=accesorio.cantidad-accesorio_qty
            accesorio.save()
            if accesorio.cantidad==0:
                accesorio.disponibilidad=False
                accesorio.save()
            Notificador+=1
            messages.success(request, "Solicitud Enviada Correctamente")
            return JsonResponse({'estado':"Solicitud Enviada Correctamente"})
        else:
            Notificador+=2
            messages.error(request, "Este accesorio no esta disponible")
            return render(request, "index.html", {"Notificador":Notificador})  
    else:
        return redirect("Index")

def solicitudEntretenimiento(request):
    if request.user.is_authenticated:

        Notificador=0
        id_entretenimiento=int(request.POST.get('entretenimiento_id'))
        entretenimiento_qty=int(request.POST.get('entretenimiento_qty'))
        entretenimiento_tipo=(request.POST.get('entretenimiento_tipo'))
        entretenimiento=Entretenimiento.objects.filter(id=id_entretenimiento).first()
        if entretenimiento.disponibilidad:
            solicitudesEntretenimientos.objects.create(user=request.user, tipo=entretenimiento_tipo, cantidad=entretenimiento_qty)
            entretenimiento.cantidad=entretenimiento.cantidad-entretenimiento_qty
            entretenimiento.save()
            if entretenimiento.cantidad==0:
                entretenimiento.disponibilidad=False
                entretenimiento.save()
            Notificador+=1
            messages.success(request, "Solicitud Enviada Correctamente")
            return JsonResponse({'estado':"Solicitud Enviada Correctamente"})
        else:
            Notificador+=2
            messages.error(request, "Este entretenimiento no esta disponible")
            return render(request, "index.html", {"Notificador":Notificador})     
    else:
        return redirect("Index")

#Vista de las solicitudes ya enviadas
def solicitudesEquipo(request):
    if request.user.is_authenticated:
        solicitudes=solicitudesEquipos.objects.all()
        return render(request, "equipos/solicitudes.html", {"solicitudes":solicitudes})
    else:
        return redirect("Index")

def solicitudesBalon(request):
    if request.user.is_authenticated:
        solicitudes=solicitudesBalones.objects.all()
        return render(request, "balones/solicitudes.html", {"solicitudes":solicitudes})
    else:
        return redirect("Index")

def solicitudesAccesorio(request):
    if request.user.is_authenticated:
        solicitudes=solicitudesAccesorios.objects.all()
        return render(request, "accesorios/solicitudes.html", {"solicitudes":solicitudes})
    else:
        return redirect("Index") 

def solicitudesEntretenimiento(request):
    if request.user.is_authenticated:
        solicitudes=solicitudesEntretenimientos.objects.all()
        return render(request, "entretenimiento/solicitudes.html", {"solicitudes":solicitudes})
    else:
        return redirect("Index")                

def entregarEquipo(request, serial_equipo):
    Notificador=0
    
    if request.user.is_authenticated:
        solicitud=solicitudesEquipos.objects.filter(serial=serial_equipo).first()
        equipo=Equipo.objects.filter(serial=serial_equipo).first()
        if equipo.disponibilidad:
            Notificador+=3
            messages.warning(request, "El Equipo ya ha sido entregado")
            return render(request, "index.html", {"Notificador":Notificador})
        else: 
            equipo.disponibilidad = True
            equipo.save()
            historialEquipos.objects.create(user=request.user, serial=serial_equipo, marca=solicitud.marca, cargador=solicitud.cargador, area=solicitud.area)
            solicitud.delete()
            perfil=Perfil.objects.filter(user=solicitud.user).first()
            perfil.ValidacionEquipo=False
            perfil.save()
            messages.success(request, "Equipo Entregado")
            return redirect("Index") 
    else:
        return redirect("Index")    

def entregarBalon(request, tipo_balon):
    Notificador=0
    if request.user.is_authenticated:

        solicitud=solicitudesBalones.objects.filter(tipo=tipo_balon).first()
        balon=Balon.objects.filter(tipo=tipo_balon).first()
        
        if balon.disponibilidad:
            Notificador+=3
            messages.error(request, "El balon ya ha sido entregado")
            return render(request, "index.html", {"Notificador":Notificador})
        else:
            balon.disponibilidad = True
            balon.cantidad = balon.cantidad + 1
            balon.save()
            historialBalones.objects.create(user=request.user, tipo=solicitud.tipo, marca=solicitud.marca, color=solicitud.color, cantidad=solicitud.cantidad)
            solicitud.delete()
            perfil=Perfil.objects.filter(user=solicitud.user).first()
            perfil.ValidacionBalon=False
            perfil.save()
            messages.success(request, "Balon Entregado")

            return redirect("Index") 
            
    else:
        return redirect("Index") 

def entregarAccesorio(request):
    if request.user.is_authenticated:
        id=int(request.POST.get('accesorio_id'))
        tipo=(request.POST.get('accesorio_tipo'))
        cantidad=int(request.POST.get('accesorio_cantidad'))
        solicitud=solicitudesAccesorios.objects.get(id=id)
        accesorio=Accesorio.objects.filter(tipo=tipo).first()
        accesorio.disponibilidad = True
        accesorio.cantidad = accesorio.cantidad + cantidad
        accesorio.save()
        historialAccesorios.objects.create(user=request.user, tipo=solicitud.tipo, cantidad=solicitud.cantidad)
        solicitud.delete()
        return JsonResponse({'estado':"Accesorio Entregado"})

    else:
        return redirect("Index")   

def entregarEntretenimiento(request):
    if request.user.is_authenticated:
        id=int(request.POST.get('entretenimiento_id'))
        tipo=(request.POST.get('entretenimiento_tipo'))
        cantidad=int(request.POST.get('entretenimiento_cantidad'))
        solicitud=solicitudesEntretenimientos.objects.get(id=id)
        entretenimiento=Entretenimiento.objects.filter(tipo=tipo).first()
        entretenimiento.disponibilidad = True
        entretenimiento.cantidad = entretenimiento.cantidad + cantidad
        entretenimiento.save()
        historialEntretenimientos.objects.create(user=request.user, tipo=solicitud.tipo, cantidad=solicitud.cantidad)
        solicitud.delete()
        return JsonResponse({'estado':"Entretenimiento Entregado"})
    else:
        return redirect("Index")
