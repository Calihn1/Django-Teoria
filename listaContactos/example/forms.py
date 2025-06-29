from django import forms
from .models import Framework, Language

class FrameworkForm(forms.ModelForm):
    language_name = forms.CharField(max_length=100, label="Nombre del Lenguaje")

    class Meta:
        model = Framework
        fields = ['name', 'language_name']

    def save(self, commit=True):
        language_name = self.cleaned_data['language_name']
        language, created = Language.objects.get_or_create(name=language_name)
        self.instance.language = language
        return super().save(commit)
