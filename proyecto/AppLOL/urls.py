from django.urls import path
from AppLOL.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="MENU" ) ,
    path("jungla/",jungla, name= "jungle") ,
    path("items/", items, name="objetos") ,
    path("campeones/", campeones, name="champs") ,
    path("comunidad/", comunidad, name="people") ,
    path("about/", quienessomos, name="abouut") ,
    path("login/", Login, name="inicio-sesion") , 
     path("loginavatar/", Login2, name="inicio-sesionavatar") ,
    path("register/", registrar_usuario, name= "Registrar-Usuario") ,
    path("resultados/", resultado_busqueda, name= "Resultado") ,
    path("inicio/", lobby, name= "inicio") ,
    path("logout/", LogoutView.as_view(template_name= "AppLOL/logout.html"), name="CERRAR-SESION"),
]
