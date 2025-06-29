from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Persona

#Create your views here
class PersonaListView(ListView):
    model = Persona

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    template_name = 'personas/persona_form.html'     
    success_url = reverse_lazy('personas:persona-list')
    
class PersonaUpdateView(UpdateView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    template_name = 'personas/persona_form.html'     
    success_url = reverse_lazy('personas:persona-list')