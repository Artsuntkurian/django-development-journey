from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Message(request):
    return HttpResponse('Hey , this is the message  ')


def profile(request):
    return HttpResponse('Hey , this is the profile  ')

def contacts(request):
    return HttpResponse('Hey , this is the contacts  ')

def about(request):
    return HttpResponse('Hey , this is the about  ')