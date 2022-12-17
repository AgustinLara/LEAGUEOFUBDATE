from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from AppLOL.models import *

from AppLOL.forms import UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request,"AppLOL/base.html")
def jungla(request):
    return render(request, "AppLOL/jungla.html")    
def items(request):
    return render(request, "AppLOL/item.html") 
def lobby(request):
    return render(request, "AppLOL/inicio.html")       
def campeones(request):

   
        

    return render(request, "AppLOL/campeones.html") 
def comunidad(request):

    if request.method == "POST":

        nombre_campeon = request.POST ["campeon"]
        nombre_runa = request.POST ["runas"]
        nombre_build = request.POST ["build"]

        comuni= comunity(campeon= nombre_campeon, runas= nombre_runa, build= nombre_build)

        comuni.save()


    return render(request, "AppLOL/comunidad.html") 


def buscar_curso(request):

    return render(request, "AppLOL/comunidad.html")

def resultado_busqueda(request):

    nombre_campeon= request.GET["nombre_campeon"]
    comunidad= comunity.objects.filter(campeon__contains=nombre_campeon)

    return render(request, "AppLOL/resultadosbusqueda.html", {"comunidad": comunidad})


    

def quienessomos(request):
    return render(request, "AppLOL/quienessomos.html") 

def Login(request):

    errors = ""

    if request.method == "POST" :
        formulario = AuthenticationForm(request, data=request.POST)
        if  formulario.is_valid():
            data = formulario.cleaned_data
            
            user = authenticate(username= data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("CERRAR-SESION")
            else:
                return render(request, "AppLOL/login.html", {"form": formulario, "errors": "Credenciales INVALIDAS"})
        else:
            return render(request, "AppLOL/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "AppLOL/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):

    if request.method == "POST" :

        formulario = UserRegisterForm(request.POST)
            
        if formulario.is_valid():
               
            formulario.save()
            return redirect("inicio-sesion")
       
        else:
                return render(request, "AppLOL/register.html", { "form": formulario, "errors": formulario.errors})

    
    formulario= UserRegisterForm()
    return render(request, "AppLOL/register.html", { "form": formulario})