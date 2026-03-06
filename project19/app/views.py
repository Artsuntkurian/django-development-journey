from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy
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


class School_Create(CreateView):
    model=School
    fields="__all__"

class School_Update(UpdateView):
    model=School
    fields="__all__"
    

class School_Delete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('School_List')
