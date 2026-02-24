"""
URL configuration for proyecto project.

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
from django.urls import path
from apps.inicio.views import saludo
from apps.productos.views import productos_views
from apps.ventas.views import ventas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',saludo),
    path('productos/', productos_views, name='productos_url'),
    path('productos/alta', productos_views, name='productos_alta'),
    path('ventas/', ventas_views, name='ventas_url'),
]
