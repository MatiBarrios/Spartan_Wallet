from django.db import models

# Create your models here.

class motivo(models.Model):
    nombre = models.CharField(max_length=60)