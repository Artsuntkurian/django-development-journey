from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
 
from app.forms import *

def Registration(request):
    
    EUMFO=UserModelForm()
    EPMFO=ProfileModelForm()
    d={
       'EUMFO':EUMFO,
       'EPMFO':EPMFO 
    }
    
    if request.method=='POST' and request.FILES:
        
        NMUMFDO=UserModelForm(request.POST)
        NMPMFDO=ProfileModelForm(request.POST,request.FILES)

        if NMUMFDO.is_valid() and NMPMFDO.is_valid():
            
            pw=NMUMFDO.cleaned_data['password']
            MUMFDO=NMUMFDO.save(commit=False)

            MUMFDO.set_password(pw)
            
            MUMFDO.save()

            MPMFDO=NMPMFDO.save(commit=False)
            MPMFDO.username=MUMFDO
            MPMFDO.save()

            print(MUMFDO.email)
            send_mail(
                'Registion Mail from ABCD',
                'message is that athul is fool',
                'artsuntwork01@gmail.com',
                [MUMFDO.email],
                fail_silently=False
            )

            return HttpResponse('Registration Completed')
        

        else:
            print(NMUMFDO)
            print('______________________________')
            print(NMPMFDO)
            return HttpResponse('Invalid')
            
        


         
    

    return render(request,'Registration.html',d)