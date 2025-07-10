from django.urls import path
from .views import (
    RolListCreateView, RolRetrieveUpdateDestroyView, CultivoListCreateView, CultivoRetrieveUpdateDestroyView,SensorListCreateView
    , SensorRetrieveUpdateDestroyView, LecturaSensorListCreateView, LecturaSensorRetrieveUpdateDestroyView,
    CosechaListCreateView, CosechaRetrieveUpdateDestroyView, AlertaListCreateView, AlertaRetrieveUpdateDestroyView,
    InformeListCreateView, InformeRetrieveUpdateDestroyView)

urlpatterns = [
    path('roles/', RolListCreateView.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', RolRetrieveUpdateDestroyView.as_view(), name='rol-detail'),

    #path('usuarios/', views.UsuarioListCreateView.as_view(), name='usuario-list-create'),
    #path('usuarios/<int:pk>/', views.UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),

    path('cultivos/', CultivoListCreateView.as_view(), name='cultivo-list-create'),
    path('cultivos/<int:pk>/', CultivoRetrieveUpdateDestroyView.as_view(), name='cultivo-detail'),

    path('sensores/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensor-detail'),

    path('lecturas/', LecturaSensorListCreateView.as_view(), name='lecturasensor-list-create'),
    path('lecturas/<int:pk>/', LecturaSensorRetrieveUpdateDestroyView.as_view(), name='lecturasensor-detail'),

    path('cosechas/', CosechaListCreateView.as_view(), name='cosecha-list-create'),
    path('cosechas/<int:pk>/', CosechaRetrieveUpdateDestroyView.as_view(), name='cosecha-detail'),

    path('alertas/', AlertaListCreateView.as_view(), name='alerta-list-create'),
    path('alertas/<int:pk>/', AlertaRetrieveUpdateDestroyView.as_view(), name='alerta-detail'),

    path('informes/', InformeListCreateView.as_view(), name='informe-list-create'),
    path('informes/<int:pk>/', InformeRetrieveUpdateDestroyView.as_view(), name='informe-detail'),
]