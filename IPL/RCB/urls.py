from django.urls import path
from RCB.views import *
app_name='athul'
urlpatterns = [
    path('captain/',captain,name='captain')
]
