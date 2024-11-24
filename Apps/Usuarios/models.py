from django.db import models

from django.contrib.auth.models import AbstractUser

from Apps.roles.models import rol as rol_usuario
# Create your models here.

class Usuario(AbstractUser):
    cuil = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    dinero = models.IntegerField(default=0)
    alias = models.CharField(max_length=40, default="aaaaa")
    CVU = models.IntegerField(default=0)
    rol = models.ForeignKey(rol_usuario, on_delete=models.CASCADE)

#UsuarioImagenLink : Varchar 
