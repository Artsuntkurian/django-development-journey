from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView


class School_List(ListView):
    context_object_name='schools'
    model=School