from django.db import models

from Apps.Usuarios.models import Usuario
from Apps.motivos.models import motivo as transferencia_Motivo

# Create your models here.

class transferencia(models.Model):
    usuarioEmisorId = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_emisor")
    usuarioEmisorMontoAnterior = models.IntegerField(default=1)
    usuarioReceptorId = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_receptor")
    usuarioReceptorMontoAnterior = models.IntegerField(default=1)
    monto = models.IntegerField(default=1)
    motivo = models.ForeignKey(transferencia_Motivo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)