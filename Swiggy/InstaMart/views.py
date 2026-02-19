from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def InstaMart(request):
    return render(request,'InstaMart.html')

def Message(request):
    return HttpResponse('<h1>Response message from InstaMart Application</h1> ')


