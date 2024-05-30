from django import forms
from .models import Formulir

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = '__all__'