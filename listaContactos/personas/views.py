from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Persona

#Create your views here
class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hola Mundo con Clases')

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

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')