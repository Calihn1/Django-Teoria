from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get( id = 1 )
    context1 = {
        'nombres' : obj.nombre,
        'edad' : obj.edad,
    }

    context2 = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context2)

def personaCreateView(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})