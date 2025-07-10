from django.urls import path
from .views import (
    RegistroGetViewSet,
    RegistroUpdateViewSet,


    iniciaSecioViewSet,
    iniciaSecioUpdateViewSet,
    

    AdminInventarioViewSet,
    AdminInventarioUpdateViewSet,

    AdminGestionViewSet,
    AdminGestionUpdateViewSet,

    AdminPerdidasViewSet,
    AdminPerdidasUpdateViewSet,

    InventarioCosechaViewSet,
    InventarioCosechaUpdateViewSet,

    ReporteAdminViewSet,
    ReporteAdminUpdateViewSet,

    SemillaViewSet,
    SemillaUpdateViewSet,

)

urlpatterns = [
    # ---Registro---
    path('registro-GET/', RegistroGetViewSet.as_view()),
    path('registro/<int:pk>/', RegistroUpdateViewSet.as_view()),



    path('Inicio-Sesion-GET/', iniciaSecioViewSet.as_view()),
    path('Inicio-Sesion/<int:pk>/', iniciaSecioUpdateViewSet.as_view()),

    path('Inventario-GET/', AdminInventarioViewSet.as_view()),
    path('Inventario/<int:pk>/', AdminInventarioUpdateViewSet.as_view()),

    path('Gestion-GET/', AdminGestionViewSet.as_view()),
    path('Gestion/<int:pk>/', AdminGestionUpdateViewSet.as_view()),

    path('Perdidas-GET/', AdminPerdidasViewSet.as_view()),
    path('Perdidas/<int:pk>/', AdminPerdidasUpdateViewSet.as_view()),

    path('Cosecha-GET/', InventarioCosechaViewSet.as_view()),
    path('Cosecha/<int:pk>/', InventarioCosechaUpdateViewSet.as_view()),

    path('Reportes-GET/', ReporteAdminViewSet.as_view()),
    path('Reportes/<int:pk>/', ReporteAdminUpdateViewSet.as_view()),

    path('Semillas-GET/', SemillaViewSet.as_view()),
    path('Semillas/<int:pk>/', SemillaUpdateViewSet.as_view()),
]
