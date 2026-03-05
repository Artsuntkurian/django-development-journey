from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView


from django.http import HttpResponse

class School_List(ListView):
    context_object_name='schools'
    model=School

class School_Detail(DetailView):
    context_object_name='schoolobject'
    model=School


def wish(request,name):
    print(name)
    return HttpResponse(f' Heloo {name}')