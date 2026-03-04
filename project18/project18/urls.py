"""
URL configuration for project18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from app.views import *

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directTV/',TemplateView.as_view(template_name='directTV.html'),name='directTV'),

    path('TVWData/',TVWData.as_view(),name='TVWData'),

    path('InsertwithTV/',InsertwithTV.as_view(),name='InsertwithTV'),

    path('InsertwithFV/',InsertwithFV.as_view(),name='InsertwithFV'),

    path('display_topic/',display_topic.as_view(),name="display_topic"),

]
