from django.urls import path
from .views import (
    CientificoDeDatosListCreateView, CientificoDeDatosDetailView,
    AgricultorListCreateView, AgricultorDetailView,
    CultivoListCreateView, CultivoDetailView,
    DatoClimaticoListCreateView, DatoClimaticoDetailView,
    ModeloPredictivoListCreateView, ModeloPredictivoDetailView,
    AlertaListCreateView, AlertaDetailView,
    RecomendacionListCreateView, RecomendacionDetailView,
)

urlpatterns = [

    # CientificoDeDatos
    path('cientificos/', CientificoDeDatosListCreateView.as_view(), name='cientifico-list-create'),
    path('cientificos/<int:pk>/', CientificoDeDatosDetailView.as_view(), name='cientifico-detail'),

    # Agricultor
    path('agricultores/', AgricultorListCreateView.as_view(), name='agricultor-list-create'),
    path('agricultores/<int:pk>/', AgricultorDetailView.as_view(), name='agricultor-detail'),

    # Cultivo
    path('cultivos/', CultivoListCreateView.as_view(), name='cultivo-list-create'),
    path('cultivos/<int:pk>/', CultivoDetailView.as_view(), name='cultivo-detail'),

    # DatoClimatico
    path('datos_climaticos/', DatoClimaticoListCreateView.as_view(), name='datoclimatico-list-create'),
    path('datos_climaticos/<int:pk>/', DatoClimaticoDetailView.as_view(), name='datoclimatico-detail'),

    # ModeloPredictivo
    path('modelos_predictivos/', ModeloPredictivoListCreateView.as_view(), name='modelopredictivo-list-create'),
    path('modelos_predictivos/<int:pk>/', ModeloPredictivoDetailView.as_view(), name='modelopredictivo-detail'),

    # Alerta
    path('alertas/', AlertaListCreateView.as_view(), name='alerta-list-create'),
    path('alertas/<int:pk>/', AlertaDetailView.as_view(), name='alerta-detail'),

    # Recomendacion
    path('recomendaciones/', RecomendacionListCreateView.as_view(), name='recomendacion-list-create'),
    path('recomendaciones/<int:pk>/', RecomendacionDetailView.as_view(), name='recomendacion-detail'),
]