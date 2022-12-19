from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username= forms.CharField(label="Nombre de Usuario")
    email= forms.EmailField(label= "Correo Electronico")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Repita su Contraseña", widget= forms.PasswordInput)


    class Meta:
        model= User
        fields= ["username", "email","password1", "password2"]
<<<<<<< HEAD
    
class UserEditForm(UserCreationForm):
    email= forms.EmailField(label= "Correo Electronico")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput, required= False)
    password2= forms.CharField(label="Repita su Contraseña", widget= forms.PasswordInput, required= False) 

    class Meta:
        model= User
        fields= ["email","password1", "password2"]

class AvatarForm(forms.Form):
    imagen =forms.ImageField()

<<<<<<< HEAD
    
=======
    pass
>>>>>>> parent of 9c15975 (intento avatar)
=======
        


>>>>>>> parent of 28473a0 (mesajeria)

