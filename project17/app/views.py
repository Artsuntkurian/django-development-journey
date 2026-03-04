from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

from django.views.generic import View
# Create your views here.


def fbv_string(request):
    return HttpResponse('fbv_string')



class CBV_String(View):
    def get(self,request):
        return HttpResponse('CBV_String')



def fbv_Html(request):
    return render(request,'fbv_Html.html')


class CBV_Html(View):
    def get(self,request):
        return render(request,'CBV_Html.html')
    


def fbv_insert(request):
    ESMFO=SchoolMF()
    d={
        'ESMFO':ESMFO
    }
    return render(request,'fbv_insert.html',d)


class CBV_Insert(View):
    def get(self,request):
        
        ESMFO=SchoolMF()
        
        d={
            'ESMFO':ESMFO
        }
        return render(request,'CBV_Insert.html',d)
    def post(self,request):
        SMFDO=SchoolMF(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Data Inserted')
        else:
            return HttpResponse('Data Invalid')