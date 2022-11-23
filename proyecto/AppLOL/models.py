from django.db import models


class nuevoitem(models.Model):
    items=models.CharField(max_length=40)
    precio=models.DateField()
    cualidades=models.IntegerField()