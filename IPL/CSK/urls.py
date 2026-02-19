from django.urls import path
from CSK.views import*

app_name='nothing'

urlpatterns = [
    path('captain/',captain,name='captain'),
]
