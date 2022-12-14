from django.db import models
from django.conf import settings
import uuid
# Create your models here.

User = settings.AUTH_USER_MODEL 

class ModelBase (models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True, db_index=True, editable=False)
    tiempo= models.DateTimeField(auto_now_add=True)
    actualizar= models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class CanalMensaje(ModelBase):

    canal= models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

class CanalUsuario(ModelBase):
    canal = models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
    usuario =models.ForeignKey(User, on_delete=models, on_delete=models.CASCADE)

class Canal(ModelBase):

    usuarios = models.ManyToManyField(User, blank=True, through=CanalUsuario)