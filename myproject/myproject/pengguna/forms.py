from django import forms
from .models import Pendaftaran

class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        fields = '__all__'