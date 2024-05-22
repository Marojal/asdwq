from django.shortcuts import render

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def form_pendaftaran(request):
    template = "formulir-pendaftaran.html"
    context = {
        'title': 'Form Pendaftaran',
    }
    return render(request, template, context)

def upload_berkas(request):
    template = "upload-file.html"
    context = {
        'title': 'Forgot Password',
    }
    return render(request, template, context)

def contact(request):
    template = "contact.html"
    context = {
        'title': 'Contact',
    }
    return render(request, template, context)