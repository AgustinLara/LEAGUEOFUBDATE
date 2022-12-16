from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def inicio(request):
    return render(request,"AppLOL/base.html")
def items(request):
    return HttpResponse("Los cambios de los items")
def campeones(request):
    return HttpResponse("Buffeos y Nerfeos")

def Login(request):

    errors = ""

    if request.method == "POST" :
        formulario = AuthenticationForm(request, data=request.POST)
        if  formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username= data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("MENU")
            else:
                return render(request, "AppLOL/login.html", {"form": formulario, "errors": "Credenciales INVALIDAS"})
        else:
            return render(request, "AppLOL/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "AppLOL/login.html", {"form": formulario, "errors": errors})