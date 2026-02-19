from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('Enter the Topic : ')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    for i in Topic.objects.all():
        print(i.topic_name)
    if TTO[1]:
        print('The given Topic is Created')
        return HttpResponse('The given Topic is Created')
    else:
        print('The Topic already Exist in Database')
        return HttpResponse('The Topic already Exist in Database')
    
def insert_webpage(request):
    tn=input('Enter the Topic from Topic Table : ')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        n=input('Enter the name from Webpage Table : ')
        ur=input('Enter the url from Webpage Table : ')
        TWO=Webpage.objects.get_or_create(topic_name=LTO[0],name=n,url=ur)
        if TWO[1]:
            print('The given Webpage is Created')
            return HttpResponse('The given Webpage is Created')
        else:
            print('The Webpage already Exist in Database')
            return HttpResponse('The Webpage already Exist in Database')
    else:
        print('The topic Entered is Not in Topic Table')
        print('Availabe Topics are : ')
        for i in Topic.objects.all():
            print(i.topic_name)

        return HttpResponse('The topic Entered is Not in Topic Table ')

def insert_AR(request):
    i=input('Enter the id from Webpage Table : ')
    LWO=Webpage.objects.filter(id=i)

    if LWO:
        
        aur=input('Enter the author for AceessRecord Table : ')
        d=input('Enter the date for AceessRecord Table in format (YYYY-MM-DD): ')
        TAO=AccessRecord.objects.get_or_create(name=LWO[0],author=aur,date=d)
        if TAO[1]:
            print('The given AccessRecord is Created')
            return HttpResponse('The given AccessRecord is Created')
        else:
            print('The AccessRecord already Exist in Database')
            return HttpResponse('The AccessRecord already Exist in Database')
    else:
        print('The id Entered is Not in webpage Table')
        print('Availabe webpage id and contents  are : ')
        for i in Webpage.objects.all():
            print(i.id,i.topic_name,i.name,i.url)

        return HttpResponse('The id Entered is Not in Webpage Table ')
    

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)


def display_wp(request):
    QLWO=Webpage.objects.all()
    d={'QLTO':QLWO}
    return render(request,'display_webpage.html',d)


def display_ar(request):
    QLRO=AccessRecord.objects.all()
    d={'QLRO':QLRO}
    return render(request,'display_ar.html',d)

def update_webpage(request):

    #Webpage.objects.filter(name='Ronaldo').update(url='http://ronaldo.com')

    #Webpage.objects.filter(name='Msd').update(url='http://msd.com')

    #Webpage.objects.filter(name='ronaldo').update(url='http://ronaldo.com')

    #Webpage.objects.filter(name='Msd').update(topic_name='Football')

    #Webpage.objects.filter(name='Msd').update(topic_name='Cricket')







    #Webpage.objects.update_or_create(name='Ronaldo',defaults={'url':'http://cristianoronaldo.com'})

   # errorrrr --- Webpage.objects.update_or_create(name='Msd',defaults={'url':'http://cristianoronaldo.com'})

    # errorrrr --- Webpage.objects.update_or_create(name='Ajith',defaults={'url':'http://cristianoronaldo.com'})
    WO=Topic.objects.get(topic_name='Cricket')
    print(WO)
    Webpage.objects.update_or_create(name='Ajith',defaults={'topic_name':WO})

    d={'QLTO':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):

    Webpage.objects.filter(name='Ronaldo').delete()
    Webpage.objects.all().delete()
    d={'QLTO':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)