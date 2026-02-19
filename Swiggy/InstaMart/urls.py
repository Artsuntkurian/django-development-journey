from django.urls import path
from InstaMart.views import *
app_name='InstaMartPage'

urlpatterns = [
    path('InstaMart/',InstaMart,name='InstaMart'),
    path('Message/',Message,name='Message'),
]
