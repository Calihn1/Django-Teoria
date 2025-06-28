from django.db import models
from django.urls import reverse

# Create your models here.
class Persona(models.Model):
    nombres    = models.CharField(max_length = 100, null = False, blank = False) #Campo obligatorio
    apellidos = models.CharField(max_length = 100, null = True, blank = False)
    edad      = models.IntegerField(null = True, blank = True, default = 18)#(max_digitS = 3)
    donador   = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('personas:persona-detail', kwargs = {'pk': self.id})