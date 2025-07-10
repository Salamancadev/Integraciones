from django.urls import path
from .views import (
    CultivoListCreateView,
    CultivoRetrieveUpdateDestroyView,
    ZonaRiegoListCreateView,
    ZonaRiegoRetrieveUpdateDestroyView,
    SensorHumedadListCreateView,
    SensorHumedadRetrieveUpdateDestroyView,
    LecturaHumedadListCreateView,
    LecturaHumedadRetrieveUpdateDestroyView,
    RiegoListCreateView,
    RiegoRetrieveUpdateDestroyView,
    PronosticoClimaListCreateView,
    PronosticoClimaRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('cultivos/', CultivoListCreateView.as_view(), name='cultivo-list-create'),
    path('cultivos/<int:pk>/', CultivoRetrieveUpdateDestroyView.as_view(), name='cultivo-detail'),
    path('zonas/', ZonaRiegoListCreateView.as_view(), name='zona-riego-list-create'),
    path('zonas/<int:pk>/', ZonaRiegoRetrieveUpdateDestroyView.as_view(), name='zona-riego-detail'),
    path('sensores/', SensorHumedadListCreateView.as_view(), name='sensor-humedad-list-create'),
    path('sensores/<int:pk>/', SensorHumedadRetrieveUpdateDestroyView.as_view(), name='sensor-humedad-detail'),
    path('lecturas/', LecturaHumedadListCreateView.as_view(), name='lectura-humedad-list-create'),
    path('lecturas/<int:pk>/', LecturaHumedadRetrieveUpdateDestroyView.as_view(), name='lectura-humedad-detail'),
    path('riegos/', RiegoListCreateView.as_view(), name='riego-list-create'),
    path('riegos/<int:pk>/', RiegoRetrieveUpdateDestroyView.as_view(), name='riego-detail'),
    path('pronosticos/', PronosticoClimaListCreateView.as_view(), name='pronostico-clima-list-create'),
    path('pronosticos/<int:pk>/', PronosticoClimaRetrieveUpdateDestroyView.as_view(), name='pronostico-clima-detail'),
]