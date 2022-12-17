from django.db import models


class items(models.Model):
    objetos=models.CharField(max_length=40)
    precio=models.DateField()
    cualidades=models.IntegerField()

    def __str__(self):
        return f"{self.objetos} -> precio: {self.precio}"

class PERSONAJES(models.Model):
    campeonLOL=models.CharField(max_length=40)
    buffonerfeo=models.DateField()
    modificaciones=models.IntegerField()

class comunity(models.Model):
    campeon=models.CharField(max_length=20)
    runas=models.CharField(max_length=100)
    build=models.CharField(max_length=100)