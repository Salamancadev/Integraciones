from django.urls import path
from .views import Humedadgenerics, Luzgenerics, Temperaturagenerics

urlpatterns = [
    path('humedad/', Humedadgenerics.as_view(), name='humedad'),
    path('luz/', Luzgenerics.as_view(), name='luz'),
    path('temperatura/', Temperaturagenerics.as_view(), name='temperatura'),
]