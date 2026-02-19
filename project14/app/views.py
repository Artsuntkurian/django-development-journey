from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def insert_topic(request):
    ETFO=TopicModelForm()

    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse("created")
        else:
            print(TMFDO.add_error)
            return HttpResponse(str(TMFDO))

    return render(request,'insert_topic.html',{'ETFO':ETFO})