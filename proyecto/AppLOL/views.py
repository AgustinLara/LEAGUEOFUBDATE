from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppLOL.models import *
from django.contrib.auth.models import User
from AppLOL.forms import AvatarForm, UserRegisterForm, UserEditForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


def inicio(request):

    if request.user.is_authenticated:
        imagen_model= avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url

    else:

        imagen_url= ""
    return render(request,"AppLOL/base.html", {"imagen_url": imagen_url})

@login_required
def jungla(request):
    if request.user.is_authenticated:
        imagen_model= avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url

    else:

        imagen_url= ""
    return render(request, "AppLOL/jungla.html", {"imagen_url": imagen_url})    



@login_required
def itemslol(request):

    
    
    item= items.objects.all()
    
    contexto = {"listado_items": item}
        

    return render(request, "AppLOL/item.html", contexto,) 



@login_required
def lobby(request):

    if request.user.is_authenticated:
        imagen_model= avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url

    else:

        imagen_url= ""
       

    return render(request, "AppLOL/inicio.html", {"imagen_url": imagen_url})
   
@login_required  
def campeoneslol(request):


    campeones= PERSONAJES.objects.all()
    
    contexto = {"listado_campeones": campeones}

 
    return render(request, "AppLOL/campeones.html", contexto) 


@login_required
def comunidad(request):
    
    if request.user.is_authenticated:
        imagen_model= avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url

    else:

        imagen_url= ""

    if request.method == "POST":

        nombre_campeon = request.POST ["campeon"]
        nombre_runa = request.POST ["runas"]
        nombre_build = request.POST ["build"]

        comuni= comunity(campeon= nombre_campeon, runas= nombre_runa, build= nombre_build)

        comuni.save()


    return render(request, "AppLOL/comunidad.html", {"imagen_url": imagen_url}) 

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
                return redirect("inicio")
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
            return redirect("Avatar")
       
        else:
                return render(request, "AppLOL/register.html", { "form": formulario, "errors": formulario.errors})

    
    return render(request, "AppLOL/register.html", { "form": formulario})

@login_required
def editarusuario(request):
    usuario= request.user

    if request.method == "POST":

       miformulario= UserEditForm(request.POST)

       if miformulario.is_valid():
            informacion = miformulario.cleaned_data

            usuario.email= informacion["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]
            usuario.save()

            return redirect("inicio")
            


    else:
        miformulario= UserEditForm(initial= {"email": usuario.email})

    return render(request, "AppLOL/editarperfil.html",{"form": miformulario})

@login_required
def  agregar_avatar(request):

    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            Avatar = avatar(user= usuario, imagen=data ["imagen"])
            Avatar.save()

            return redirect("inicio")
        else:
            return render(request, "AppLOL/agregaravatar.html", {"form": formulario, "errors":formulario.errors})    

    formulario = AvatarForm()
    

    return render(request, "AppLOL/agregaravatar.html", {"form": formulario})