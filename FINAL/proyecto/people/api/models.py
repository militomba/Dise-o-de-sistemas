from django.db import models
from django.conf import settings

# Create your models here.
class DatosUsuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    
