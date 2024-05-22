from django.shortcuts import render
from pengguna.models import Formulir
# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)
    
