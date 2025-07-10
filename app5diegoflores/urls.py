from django.urls import path
from .views import MedicionList, AlertaList

urlpatterns = [
    path('mediciones/', MedicionList.as_view()),
    path('alertas/', AlertaList.as_view()),
]