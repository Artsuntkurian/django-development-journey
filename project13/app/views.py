from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.
def InsertDept(request):
    EDFO=DeptForm()
    d={'EDFO':EDFO}

    if request.method=='POST':
        DFDO=DeptForm(request.POST)
        if DFDO.is_valid():
            dno=DFDO.cleaned_data['deptno']
            dn=DFDO.cleaned_data['dname']
            dl=DFDO.cleaned_data['dlocation']

            TDTO=Dept.objects.get_or_create(deptno=dno,dname=dn,dlocation=dl)
            if TDTO[1]:
                return HttpResponse('Data Entered')
            else:
                return HttpResponse('Data already exist')
        else:
            return HttpResponse('Data is invalid')



    return render(request,'InsertDept.html',d)


def InsertEmp(request):
    EWFO=EmpForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        EFDO=EmpForm(request.POST)
        if EFDO.is_valid():
            eno=EFDO.cleaned_data['empno']
            en=EFDO.cleaned_data['ename']
            j=EFDO.cleaned_data['job']
            m=EFDO.cleaned_data['mgr']
            if m:
                MO=Emp.objects.get(empno=m)
            else:
                MO=None
            s=EFDO.cleaned_data['sal']
            c=EFDO.cleaned_data['comm']
            d=EFDO.cleaned_data['deptno']
            DO=Dept.objects.get(deptno='d')

            TETO=Emp.objects.get_or_create(empno=eno,ename=en,job=j,mgr=MO,sal=s,comm=c,deptno=DO)
            if TETO[1]:
                return HttpResponse('Data Entered')
            else:
                return HttpResponse('Data already exist')
        else:
            return HttpResponse('Data is invalid')

    return render(request,'InsertEmp.html',d)


def InserDeptByModelForm(request):
    EDMFO=DeptModelForm()
    d={'EDMFO':EDMFO}
    if request.method=='POST':
        DMFDO=DeptModelForm(request.POST)
        if DMFDO.is_valid():
            DMFDO.save()
            return HttpResponse('Data Entered')
        else:
            return HttpResponse('Data is invalid')
    
    return render(request,'InserDeptByModelForm.html',d)