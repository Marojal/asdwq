"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from myproject.auth import akun_login
from django.contrib import admin
from django.urls import path, include

from myproject.auth import akun_login,akun_logout,akun_registrasi
from myproject.views import home,form_pendaftaran,upload_berkas,contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('form-pendaftaran',form_pendaftaran,name='form-pendaftaran'),
    path('upload-berkas',upload_berkas,name='upload-berkas'),
    path('contact',contact,name='contact'),
    path('login',akun_login,name='login'),
    path('logout',akun_logout,name='logout'),
    path('registrasi',akun_registrasi,name='registrasi'),
    path('', include('pengguna.urls')),
    
]
