"""project_module3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app_sensado import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_sensado/', include('app_sensado.urls', namespace='app_sensado')),
    path('app_praes/', include('app_praes.urls', namespace="app_praes")),
    path('paws/', include('paws.urls', namespace="paws")),
    path('nariz_electronica/', include('nariz_electronica.urls', namespace="nariz_electronica")),
    path('', views.main_index, name='main-index'),
    path('accounts/', include('django.contrib.auth.urls')),
]
