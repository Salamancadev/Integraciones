from django.urls import path
from .views import (
    UsuarioList, UsuarioDetail,
    TerrenoList, TerrenoDetail,
    DronList, DronDetail,
    ParametroFertilizacionList, ParametroFertilizacionDetail,
    RutaList, RutaDetail,
    EjecucionList, EjecucionDetail,
    ReporteList, ReporteDetail
)

urlpatterns = [
    # Usuarios
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),

    # Terrenos
    path('terrenos/', TerrenoList.as_view(), name='terreno-list'),
    path('terrenos/<int:pk>/', TerrenoDetail.as_view(), name='terreno-detail'),

    # Drones
    path('drones/', DronList.as_view(), name='dron-list'),
    path('drones/<int:pk>/', DronDetail.as_view(), name='dron-detail'),

    # Parámetros de fertilización
    path('parametros-fertilizacion/', ParametroFertilizacionList.as_view(), name='parametro-list'),
    path('parametros-fertilizacion/<int:pk>/', ParametroFertilizacionDetail.as_view(), name='parametro-detail'),

    # Rutas
    path('rutas/', RutaList.as_view(), name='ruta-list'),
    path('rutas/<int:pk>/', RutaDetail.as_view(), name='ruta-detail'),

    # Ejecuciones
    path('ejecuciones/', EjecucionList.as_view(), name='ejecucion-list'),
    path('ejecuciones/<int:pk>/', EjecucionDetail.as_view(), name='ejecucion-detail'),

    # Reportes
    path('reportes/', ReporteList.as_view(), name='reporte-list'),
    path('reportes/<int:pk>/', ReporteDetail.as_view(), name='reporte-detail'),
]