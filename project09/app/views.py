from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.











def Login(request):
    
    if request.POST:
        S_username=request.POST['user']
        return HttpResponse(f'The username login in is {S_username}')
    return render(request,'Login.html')


def insertTopicForm(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TTO=Topic.objects.get_or_create(topic_name=topic)
        if TTO[1]:
            return HttpResponse('Topic is susscefully created')
        else:
            return HttpResponse('Topic already present in DataBase Add new')
    return render(request,'insertTopicForm.html')





def insertWebpageForm(request):
    QLTO=Topic.objects.all()
    d={"QLTO":QLTO}
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get(topic_name=topic)
        name=request.POST['name']
        url=request.POST['url']
        
        
        WTO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)
        if WTO[1]:
            return HttpResponse('Webpage is susscefully created')
        else:
            return HttpResponse('webpage already present in DataBase Add new')
            
    return render(request,'insertWebpageForm.html',d)



def inserAcessRecordForm(request):
    
    QLWO=Webpage.objects.all()
    print(QLWO[1])
    d={'QLWO':QLWO}
    if request.method=='POST':
        id=request.POST['id']
        WO=Webpage.objects.get(id=id)
        authr=request.POST['author']
        d=request.POST['date']
        TARTO=AccessRecord.objects.get_or_create(name=WO,author=authr,date=d)
        if TARTO[1]:
            return HttpResponse('AccessRecord is susscefully created')
        else:
            return HttpResponse('AccessRecord already present in DataBase Add new')
    
    return render(request,'inserAcessRecordForm.html',d)



def multipleSelect(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=="POST":
        LTO=request.POST.getlist('topic')
        
        EQWS=Webpage.objects.none()
        for TO in LTO:
            EQWS=EQWS|Webpage.objects.filter(topic_name=TO)
        d1={'EQWS':EQWS}
        return render(request,'displayWebpages.html',d1)


    return render(request,'multipleSelect.html',d)


def checkboxSelect(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    return render(request,'checkboxSelect.html',d)




