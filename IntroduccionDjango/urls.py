"""IntroduccionDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Devices import views as v #importando todas las vistas
from Rest import views as vr  #importando todas las vistas de Rest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/',v.sensores),  #mapeo de la vista sensores a la url sensor/
    path('', v.index),  #mapeo de la vista index a la url principal del host
    path('data/', v.data), #mapeo de la vista data a la url data/
    path('rest/', vr.temperatura) #mapeo de la vista temperatura a la url rest/
]
