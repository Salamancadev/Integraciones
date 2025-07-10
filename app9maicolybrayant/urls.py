from django.urls import path
from .views import (inicio, lista_lotes, lista_mediciones, lista_estandares)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lotes/', lista_lotes, name='lista_lotes'),
    path('mediciones/', lista_mediciones, name='lista_mediciones'),
    path('estandares/', lista_estandares, name='lista_estandares'),
]
