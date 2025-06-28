from django.shortcuts import render
from django.views.generic import ListView
from .models import Persona

#Create your views here
class PersonaListView(ListView):
    model = Persona