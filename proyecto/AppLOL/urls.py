from django.urls import path
from AppLOL.views import *


urlpatterns = [
    path("", inicio, name="MENU" ) ,
    path("items/",items) ,
    path("campenes/", campeones) ,
    path("login/", Login, name="inicio-sesion") , 
]
