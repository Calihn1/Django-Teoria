from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Persona

#Create your views here
class PersonaListView(ListView):
    model = Persona

class PersonaDetailView(DetailView):
    model = Persona