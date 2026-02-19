from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    d={'data':'Hai How ARE yoU','d':datetime.datetime.now(),'c':1}
    return render(request,'filters.html',d)