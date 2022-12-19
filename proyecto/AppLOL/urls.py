from django.urls import path
from AppLOL.views import *
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

urlpatterns = [
    path("", inicio, name="MENU" ) ,
    path("jungla/",jungla, name= "jungle") ,
    path("items/", itemslol, name="objetos") ,
    path("campeones/", campeoneslol, name="champs") ,
    path("comunidad/", comunidad, name="people") ,
    path("about/", quienessomos, name="abouut") ,
    path("login/", Login, name="inicio-sesion") , 
     path("loginavatar/", Login2, name="inicio-sesionavatar") ,
    path("register/", registrar_usuario, name= "Registrar-Usuario") ,
    path("resultados/", resultado_busqueda, name= "Resultado") ,
    path("inicio/", lobby, name= "inicio") ,
    path("agregaravatar/", agregar_avatar, name= "Avatar") ,
    path("editarperfil/", editarusuario, name="editar"),
    path("logout/", LogoutView.as_view(template_name= "AppLOL/logout.html"), name="CERRAR-SESION"),
]
