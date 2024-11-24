from django.db import models

from Apps.Usuarios.models import Usuario

# Create your models here.

class usuarioContacto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario")
    contacto = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contactos")
    favorito = models.BooleanField(default=False)

    class Meta:
        unique_together = ('usuario', 'contacto')  # Llave primaria compuesta equivalente