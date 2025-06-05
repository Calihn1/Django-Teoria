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
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form' : form
    }
    return render(request, 'personas/personasCreate.html', context)
