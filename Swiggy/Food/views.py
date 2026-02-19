from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Food(request):
    return render(request,'Food.html')

def Message(request):
    return HttpResponse('<h1>Response message from Food Application</h1> ')