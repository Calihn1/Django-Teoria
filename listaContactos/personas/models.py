from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres    = models.CharField(max_length = 100, null = False, blank = False) #Campo obligatorio
    apellidos = models.CharField(max_length = 100, null = True, blank = False)
    edad      = models.IntegerField(null = True, blank = True, default = 18)#(max_digitS = 3)
    donador   = models.BooleanField(default = True)