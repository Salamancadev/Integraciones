from .views import historialView, controlView
from django.urls import path

urlpatterns = [
    path('historial/', historialView.as_view()),
    path('sensor/', controlView.as_view()),
]