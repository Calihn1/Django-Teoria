from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get( id = 1 )
    context1 = {
        'nombre' : obj.nombre,
        'edad' : obj.edad,
    }

    context2 = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html',context2)