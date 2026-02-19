from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def InsertTopic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TTO=Topic.objects.get_or_create(topic_name=tn)
            if TTO[1]:
                return HttpResponse('Topic Table is created ')
            else:
                return HttpResponse('Table is already exist ')
    return render(request,'InsertTopic.html',d)

def InsertWebpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            WTO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)
            if WTO[1]:
                return HttpResponse('Webpage  is created ')
            else:
                return HttpResponse('Webpage is already exist ')
        else: 
            return HttpResponse('data entere is invalid  ')
    return render(request,'InsertWebpage.html',d)
