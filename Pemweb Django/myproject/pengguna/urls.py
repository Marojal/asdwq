from django.urls import path
from pengguna.views import formulir_list,home


urlpatterns = [
    path('', home, name='home'),
    path('formulir/list', formulir_list, name='formulir_list'),
]