from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Formulir(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.TextField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nik = models.CharField(max_length=16, blank=True, null=True)
    tempat_lahir = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    no_hp = models.CharField(max_length=16, blank=True, null=True)
    no_hp_ortu = models.CharField(max_length=16, blank=True, null=True)
    kelurahan = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    kota = models.TextField(blank=True, null=True)
    jenis_kelamin = models.TextField(blank=True, null=True)
    prog1 = models.TextField(blank=True, null=True)
    prog2 = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Formulir"

from django.db import models

class Pendaftaran(models.Model):
    # definisi fields
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
