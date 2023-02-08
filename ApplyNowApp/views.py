from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from Solicitar.models import *
from ApplyNowApp.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.filter(user=request.user).first()

        if perfil.cargo == "Administrador":
            cantidadSolicitudes1 = solicitudesEquipos.objects.all()
            cantidadSolicitudes2 = solicitudesBalones.objects.all()
            cantidadSolicitudes3 = solicitudesAccesorios.objects.all()
            cantidadSolicitudes4 = solicitudesEntretenimientos.objects.all()
            cantidadSolicitudes = len(cantidadSolicitudes1) + len(
                cantidadSolicitudes2) + len(cantidadSolicitudes3) + len(cantidadSolicitudes4)

            return render(request, "index.html", {"perfil": perfil, "cantidad_solicitudes": cantidadSolicitudes, "Qequipo": len(cantidadSolicitudes1), "Qbalon": len(cantidadSolicitudes2), "Qaccesorio": len(cantidadSolicitudes3), "Qentretenimiento": len(cantidadSolicitudes4)})
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")


def loguear(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        password = request.POST["contraseña"]
        user = authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ha Iniciado Sesión Con Éxito")
            return redirect("Index")
        else:
            logout(request)
            messages.warning(
                request, "Nombre De Usuario o Contraseña No Valido")
            return redirect("Index")
    return redirect("../")


def cerrar_sesion(request):
    logout(request)
    messages.error(request, "Cerro Sesión Con Exito")

    return redirect("Index")


def perfil(request):
    if request.user.is_authenticated:
        perfilUsuario = Perfil.objects.filter(user=request.user).first()
        return render(request, "perfil.html", {"perfil_usuario": perfilUsuario})
    else:
        return redirect("Index")


def changedate(request):
    Notificador = 0
    if request.user.is_authenticated:
        if request.method == "POST":
            perfilUsuario = Perfil.objects.filter(user=request.user).first()
            usuario = request.user
            perfilA = User.objects.filter(username=usuario).first()
            tel = request.POST["telefono"]
            mail = request.POST["email"]
            perfilUsuario.telefono = tel
            perfilA.email = mail

            perfilUsuario.save()
            perfilA.save()
            Notificador += 1
            messages.success(request, "Cambios Realizados Correctamente")
            return render(request, "perfil.html", {"Notificador": Notificador})
        else:
            return redirect("Index")
    else:
        return redirect("Index")


def change_password(request):
    Notificador = 0
    if request.method == 'POST':
        passwordA = request.POST["passwordA"]
        passwordN = request.POST["passwordN"]
        minimo = 8
        user = request.POST["usuario"]

        if len(passwordN) >= minimo:
            logout(request)
            perfilA = User.objects.filter(username=user).first()
            user1 = authenticate(username=user, password=passwordA)
            if user1 is not None:
                perfilA.set_password(passwordN)
                perfilA.save()
                update_session_auth_hash(request, perfilA.username)
                Notificador += 1
                messages.success(
                    request, "Cambios Realizados Correctamente, ¡Vuelve a iniciar sesión!")
                name = perfilA.first_name
                lastname = perfilA.last_name
                mail = perfilA.email
                subject = "ApplyNow-Cambio de contraseña"
                mensaje = render_to_string("emails/change_password_msg.html", {
                    "email": mail,
                    "nombre": name,
                    "apellido": lastname,
                    "documento": user
                })
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [mail]
                send_mail(subject, mensaje, email_from,
                          recipient_list, html_message=mensaje)
                logout(request)
                return render(request, "index.html", {"Notificador": Notificador})
            else:
                logout(request)
                Notificador += 2
                messages.success(
                    request, "Se a cerrado la sesión por seguridad a la cuenta.")
                messages.success(request, "La Contraseña actual no coincide!")
                return render(request, "index.html", {"Notificador": Notificador})
        else:
            Notificador += 3
            messages.warning(
                request, "La Contraseña debe tener minimo 8 caracteres")
            return render(request, "perfil.html", {"Notificador": Notificador})
    else:
        return redirect("Index")


def contacto(request):
    subject = "Comunicado"
    mensaje = render_to_string("emails/contacto.html", {
        "nombre": request.POST["nombre"],
        "mensaje": request.POST["mensaje"],
        "telefono": request.POST["telefono"],
        "email": request.POST["email"]
    })
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["brayansayrez400@gmail.com"]
    send_mail(subject, mensaje, email_from,
              recipient_list, html_message=mensaje)
    Notificador = 4
    messages.success(request, "Correo Enviado Correctamente")
    return render(request, "index.html", {"Notificador": Notificador})


def recover(request):
    perfilA = User.objects.all
    return render(request, "recover.html", {"perfilA": perfilA})


def recovermsg(request):
    Notificador = 0
    if request.method == 'POST':
        prueba = request.POST["email"]
        perfilA = User.objects.filter(email=prueba).first()
        password="False"
        if perfilA:
            nombre = perfilA.first_name
            apellido = perfilA.last_name
            documento = perfilA.username
            subject = "Comunicado-ApplyNow"
            mensaje = render_to_string("emails/recovermsg.html", {
                "email": request.POST["email"],
                "nombre": nombre,
                "apellido": apellido,
                "documento": documento
            })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST["email"]]
            send_mail(subject, mensaje, email_from,
                      recipient_list, html_message=mensaje)

            Notificador += 1
            perfilA.set_password(password)
            perfilA.save()
            messages.success(request, "Encontramos tu cuenta! Revisa tu bandeja de entrada.")
            return render(request, "index.html", {"Notificador": Notificador})
        else:
            Notificador += 2
            messages.error(
                request, "Direccion de correo electronico No Valido")
            return render(request, "recover.html", {"Notificador": Notificador})
    else:
        Notificador += 3
        messages.error(request, "XD")
        return render(request, "recover.html", {"Notificador": Notificador})


def confirmedrecover(request, userP):
    perfilA = User.objects.filter(username=userP).first()
    if perfilA.password == "pbkdf2_sha256$390000$FLGVqBucfT2Fk46mKx6bo9$AARwXHVQ075loUEdIsOb90BtxGy7S3XFb4zsQFYFRX8=":
        return render(request, "confirmedrecover.html", {"perfilA": perfilA, "userP": userP})
    else:
        print(perfilA.password)
        messages.error(request, "Ya se restablecio la contraseña")
        return redirect("Index")


def recoversuccess(request, userP):
    Notificador=0
    perfilA = User.objects.filter(username=userP).first()
    if perfilA.password == "pbkdf2_sha256$390000$FLGVqBucfT2Fk46mKx6bo9$AARwXHVQ075loUEdIsOb90BtxGy7S3XFb4zsQFYFRX8=":
        if request.method == 'POST':
            user = userP
            passwordN = request.POST["passwordN"]
            passwordNC = request.POST["passwordNC"]
            minimo = 8
            if len(passwordN) >= minimo:
                if passwordN == passwordNC:
                    perfilA = User.objects.filter(username=userP).first()
                    perfilA.set_password(passwordN)
                    perfilA.save()
                    update_session_auth_hash(request, perfilA.username)
                    Notificador += 1
                    messages.success(request, "Cambios Realizados Correctamente, ¡Vuelve a iniciar sesión!")
                    name = perfilA.first_name
                    lastname = perfilA.last_name
                    mail = perfilA.email
                    subject = "ApplyNow-Cambio de contraseña"
                    mensaje = render_to_string("emails/change_password_msg.html", {
                        "email": mail,
                        "nombre": name,
                        "apellido": lastname,
                        "documento": user
                    })
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [mail]
                    send_mail(subject, mensaje, email_from,
                            recipient_list, html_message=mensaje)
                    return render(request, "index.html", {"Notificador": Notificador})
                else:
                    messages.warning(request, "Las Contraseñas no coinciden")
                    return render(request, "confirmedrecover.html", {"userP": userP})
            else:
                messages.warning(request, "La Contraseña debe tener minimo 8 caracteres")
                return render(request, "confirmedrecover.html", {"userP": userP})
        else:
            return redirect("Index")
    else:
        messages.error(request, "Ya se restablecio la contraseña")
        return redirect("Index")
