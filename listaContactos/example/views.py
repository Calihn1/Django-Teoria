from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Language, Framework
from .forms import FrameworkForm
from django import forms
from django.shortcuts import redirect

class LanguageListView(ListView):
    model = Language
    template_name = 'example/language_list.html'

class LanguageDetailView(DetailView):
    model = Language
    template_name = 'example/language_detail.html'

class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'example/language_confirm_delete.html'
    success_url = reverse_lazy('examples:language-list')

class FrameworkCreateView(CreateView):
    model = Framework
    form_class = FrameworkForm
    template_name = 'example/framework_form.html'
    success_url = reverse_lazy('examples:language-list')

class FrameworkUpdateView(UpdateView):
    model = Framework
    fields = ['name', 'language']
    template_name = 'example/framework_form.html'
    success_url = reverse_lazy('examples:language-list')

class FrameworkDeleteView(DeleteView):
    model = Framework
    template_name = 'example/framework_confirm_delete.html'
    success_url = reverse_lazy('examples:language-list')
