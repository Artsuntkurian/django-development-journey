from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def insert(request):
    
    ETMFO=TopicMF()
    EWMFO=WebpageMF()
    EARMFO=AcessRecordMF()
    d={
        'ETMFO':ETMFO,
        'EWMFO':EWMFO,
        'EARMFO':EARMFO,
    }

    if request.method=="POST":
        TMFDO=TopicMF(request.POST)
        WMFDO=WebpageMF(request.POST)
        ARMFDO=AcessRecordMF(request.POST)

        if TMFDO.is_valid() and WMFDO.is_valid() and ARMFDO.is_valid():
            TMFDO=TMFDO.save()

            print(TMFDO)


            MWMFDO=WMFDO.save(commit=False)
            MWMFDO.topic_name=TMFDO
            MWMFDO.save()
            
            MARMFDO=ARMFDO.save(commit=False)
            MARMFDO.name=MWMFDO
            MARMFDO.save()

            return HttpResponse('Data entered susessfully')
        
        else:
            print(TMFDO)
            print(WMFDO)
            print(ARMFDO)
            return HttpResponse("invalid")
        
        

    
    return render(request,'insert.html',d)