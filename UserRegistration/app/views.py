from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
 
from app.forms import *


from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
            
            return HttpResponse('Invalid')

    return render(request,'Registration.html',d)



def home(request):

    username= request.session.get('username')
    if username:
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        

        AUO=authenticate(username=username,password=password)

        print(AUO)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username

                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User is not active ')
        else:
                return HttpResponse('Invalid crendiatls  ')

    return render(request,'signin.html')


@login_required
def SignOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    #return render(request,'home.html')