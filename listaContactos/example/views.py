from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Language, Framework
from .forms import FrameworkForm
from django import forms
from django.shortcuts import redirect

class LanguageListView(ListView):
    model = Language
    template_name = 'frameworks/language_list.html'

class LanguageDetailView(DetailView):
    model = Language
    template_name = 'frameworks/language_detail.html'

class FrameworkCreateView(CreateView):
    model = Framework
    form_class = FrameworkForm
    template_name = 'frameworks/framework_form.html'
    success_url = reverse_lazy('frameworks:language-list')

class FrameworkUpdateView(UpdateView):
    model = Framework
    fields = ['name', 'language']
    template_name = 'frameworks/framework_form.html'
    success_url = reverse_lazy('frameworks:language-list')

class FrameworkDeleteView(DeleteView):
    model = Framework
    template_name = 'frameworks/framework_confirm_delete.html'
    success_url = reverse_lazy('frameworks:language-list')
