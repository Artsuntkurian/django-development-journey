from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def contact(request):
    ECFO=ContactForm()
    d={'ECFO':ECFO}

    if request.method=='POST':
        CFDO=ContactForm(request.POST)
        
        if CFDO.is_valid():
            print(CFDO.cleaned_data)
            return HttpResponse(str(CFDO.cleaned_data))
        else:
            return HttpResponse("Invalid Entry")

    return render(request,'contact.html',d)