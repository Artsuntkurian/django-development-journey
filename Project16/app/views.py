from django.shortcuts import render
from app.forms import *
# Create your views here.


def insert(request):
    
    ETMFO=TopicMF()
    EWMFO=WebpageMF()
    EARMFO=AcessRecordMF()
    d={
        'ETMFO':ETMFO,
        'EWMFO':EWMFO,
        'EARMFO':EARMFO,
    }

    
    return render(request,'insert.html',d)