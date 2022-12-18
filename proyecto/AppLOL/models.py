from django.db import models
from django.contrib.auth.models import User

class items(models.Model):
    objetos=models.CharField(max_length=50)
    precio=models.CharField(max_length=40)
    cualidades=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.objetos} -> precio: {self.precio}-> cualidades: {self.cualidades}"

class PERSONAJES(models.Model):
    campeonLOL=models.CharField(max_length=40)
    buffonerfeo=models.CharField(max_length=100)
    modificaciones=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.campeonLOL} -> {self.buffonerfeo}: {self.modificaciones}"


class comunity(models.Model):
    campeon=models.CharField(max_length=20)
    runas=models.CharField(max_length=100)
    build=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.campeon} -> runas: {self.runas} -> build: {self.build}"

class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
