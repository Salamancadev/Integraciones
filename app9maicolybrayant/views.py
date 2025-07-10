from django.shortcuts import render
from django.http import HttpResponse
from .models import LoteGrano, MedicionCalidad, EstandarCalidad
from rest_framework import viewsets
from .serializers import LoteGranoSerializer, MedicionCalidadSerializer, EstandarCalidadSerializer

def inicio(request):
    return HttpResponse("""
        <h1>Bienvenido al sistema de control de calidad.</h1>
        <ul>
            <li><a href='/lotes/'>Ver Lotes</a></li>
            <li><a href='/mediciones/'>Ver Mediciones</a></li>
            <li><a href='/estandares/'>Ver Estándares</a></li>
        </ul>
        <h3>Acceso directo a la API (Postman o navegador):</h3>
        <ul>
            <li><a href="/api/lotes/">/api/lotes/</a></li>
            <li><a href="/api/mediciones/">/api/mediciones/</a></li>
            <li><a href="/api/estandares/">/api/estandares/</a></li>
        </ul>
    """)

def lista_usuarios(request):
    return HttpResponse("""
        <h2>Funcionalidad de usuarios no disponible</h2>
        <p>El sistema no maneja usuarios en este momento.</p>
    """)

def lista_lotes(request):
    lotes = LoteGrano.objects.all()
    texto = "<h2>Lotes de grano:</h2><ul>"
    for l in lotes:
        texto += f"<li>{l.codigo_lote} - {l.tipo_grano}</li>"
    texto += "</ul>"
    return HttpResponse(texto)

def lista_mediciones(request):
    mediciones = MedicionCalidad.objects.all()
    texto = "<h2>Mediciones:</h2><ul>"
    for m in mediciones:
        texto += f"<li>{m.parametro} = {m.valor_medido} ({'✔' if m.cumple_estandar else '✘'})</li>"
    texto += "</ul>"
    return HttpResponse(texto)

def lista_estandares(request):
    estandares = EstandarCalidad.objects.all()
    texto = "<h2>Estándares de calidad:</h2><ul>"
    for e in estandares:
        texto += f"<li>{e.parametro}: {e.valor_minimo} - {e.valor_maximo}</li>"
    texto += "</ul>"
    return HttpResponse(texto)

class LoteGranoViewSet(viewsets.ModelViewSet):
    queryset = LoteGrano.objects.all()
    serializer_class = LoteGranoSerializer

class MedicionCalidadViewSet(viewsets.ModelViewSet):
    queryset = MedicionCalidad.objects.all()
    serializer_class = MedicionCalidadSerializer

class EstandarCalidadViewSet(viewsets.ModelViewSet):
    queryset = EstandarCalidad.objects.all()
    serializer_class = EstandarCalidadSerializer