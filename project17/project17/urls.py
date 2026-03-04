"""
URL configuration for project17 project.

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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('fbv_string/',fbv_string,name='fbv_string'),
    path('CBV_String/',CBV_String.as_view(),name='CBV_String'),

    path('fbv_Html/',fbv_Html,name='fbv_Html'),
    path('CBV_Html/',CBV_Html.as_view(),name='CBV_Html'),

    path('fbv_insert/',fbv_insert,name='fbv_insert'),
    path('CBV_Insert/',CBV_Insert.as_view(),name='CBV_Insert'),

]
