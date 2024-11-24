from django.db import models

# Create your models here.

class rol(models.Model):
    nombre = models.CharField(max_length=40)