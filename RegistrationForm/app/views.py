from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
from app.forms import *

def Registration(request):
    EUMFO=UserModelForm()
    EPMFO=ProfileModelForm()
    d={
       'EUMFO':EUMFO,
       'EPMFO':EPMFO 
    }

    

    return render(request,'Registration.html',d)