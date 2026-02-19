from django.urls import path
from Food.views import *
app_name='FoodPage'

urlpatterns = [
    path('Food/',Food,name='Food'),
    path('Message/',Message,name='Message'),
]
