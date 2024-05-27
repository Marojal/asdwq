from django.shortcuts import render
from pengguna.models import Formulir

from pengguna.forms import PendaftaranForm
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

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)
    
def pendaftaran_view(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect ke halaman sukses setelah menyimpan data
    else:
        form = PendaftaranForm()
    return render(request, 'dashboard/snippets/formulir.html', {'form': form})