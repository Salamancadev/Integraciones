"""
URL configuration for proyectointegraciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app4agrodrones.views import home





urlpatterns = [
    path('', home, name='home'),  # Esta línea va primero
    path('admin/', admin.site.urls),
    path('app4/', include('app4agrodrones.urls')),
    
]

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('app1/', include('app1riegoautomatizado.urls')),
    path('app2/', include('app2frankyjoner.urls')),
    path('app3/', include('app3miguelysantiago.urls')),
    path('app4/', include('app4agrodrones.urls')),
    path('app5/', include('app5diegoflores.urls')),
    path('app6/', include('app6alanybrayan.urls')),
    path('app7/', include('app7simonyjp.urls')),
    path('app8/', include('app8nicolasysebastian.urls')),
    path('app9/', include('app9maicolybrayant.urls')),
]