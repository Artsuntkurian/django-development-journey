from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Prefetch
from django.db.models import Aggregate
from django.db.models import *
from django.db.models.functions import Length

# Create your views here.
def insert_dept(request):
    for i in Dept.objects.all():
        print(i.dept_no,i.dname,i.loc)
    dn=input("Enter the Department Number : ")
    LDO=Dept.objects.filter(dept_no=dn)
    if LDO:
        return HttpResponse('Dept no already exist')
    
    else:
        n=input('Enter the department name : ')
        l=input('Enter the Location of Department : ')

        TDTO=Dept.objects.get_or_create(dept_no=int(dn),dname=n,loc=l)

        if TDTO[1]:
            return HttpResponse('NEW ROW iN DEPARTMENT TABLE IS CREATED !!!!!!')
        else:
            return HttpResponse('Given DATA IS NOT ADDED TO  DEPARTMENT TABLE!')


def insert_emp(request):
    E=EMP.objects.all()
    if E:
        print("existing details are : ")
        for i in E:
            print(i.emp_no,i.ename,i.job,i.mgr,i.hire_date,i.sal,i.comm,i.dept_no.dept_no)
    
    en=input('Enter the Employee number : ')
    
    LEO=EMP.objects.filter(emp_no=en)
    
    if LEO:
        return HttpResponse('Employee no already exist')
    else:
        
        n=input('Enter the Employee name ')
        j=input('Enter the Employee job ')
        m=input('Enter the Employee manger empno ')
        
        if m:
            m=int(m)
            MO=EMP.objects.filter(emp_no=m)[0]
            
        else:
            MO=None
        h=input('Enter the Employee hiredate ')
        s=input('Enter the Employee salary ')
        c=input('Enter the Employee commission ')
        if c:
            c=float(c)
        else:
            c=None
        
        for i in Dept.objects.all():
            print(i.dept_no,i.dname,i.loc)
        dn=input('Enter the department number ')
        
        LDO=Dept.objects.filter(dept_no=int(dn))
        
        if LDO:
            TEO=EMP.objects.get_or_create(emp_no=en,ename=n,job=j,mgr=MO,sal=float(s),comm=c,dept_no=LDO[0])
            if TEO[1]:
                return HttpResponse('NEW ROW iN EMP TABLE IS CREATED !!!!!!')
            else:
                return HttpResponse('Given DATA IS NOT ADDED TO  EMP TABLE!')


def EmpToDept(request):
    QSLEDO=EMP.objects.select_related('dept_no')
    
    

    # aggregate function examples 
    MSET=EMP.objects.aggregate(Max('sal'))
    QSLEDO=EMP.objects.annotate(LE=Length('ename')).filter(LE__gt=6)
    MDS=EMP.objects.values('dept_no').annotate(Max('sal'))
    MDSF=EMP.objects.values('dept_no').annotate(Max('sal')).filter(dept_no=10)
    print(MDSF)

    print(MSET['sal__max'])

    print(MDS)

    #A=EMP.objects.filter(sal__gt=EMP.objects.values('dept_no').annotate(AvgS=Avg('sal').filter(dept_no=10)['AvgS']))
    davgsal=EMP.objects.filter(dept_no=10).aggregate(Avg('sal'))
    print(davgsal)
    avgsal=davgsal['sal__avg']
    print(avgsal)
    A=EMP.objects.filter(sal__gt=EMP.objects.filter(dept_no=10).aggregate(Avg('sal'))['sal__avg'])
    print(A)

    QSLEDO=EMP.objects.filter(sal__gt=avgsal)
    d={'QSLEDO':QSLEDO}
    return render (request,'EmpToDept.html',d)

def EmpToMgr(request):
    QSLEMO=EMP.objects.select_related('mgr').all()

    QSLEMO=EMP.objects.select_related('mgr').filter(sal__gt=F('mgr__sal'))
    QSLEMO=EMP.objects.select_related('mgr').filter(comm__isnull=False,comm__gt=F('sal')/1000)
    d={'QSLEMO':QSLEMO}
    a=F('sal')*2
    print(a)










    #emp name length > mgr name length
    QSLEMO=EMP.objects.select_related('mgr').annotate(ENL=Length('ename'),MNL=Length('mgr__ename')).filter(ENL__gt=F('MNL'))
    
    #print mgr details , where his employee sal>50k
    QSLEMO=EMP.objects.select_related('mgr').filter(sal__gt=50000)

    for i in QSLEMO:
        print(i.mgr.ename)













    d={'QSLEMO':QSLEMO}
    return render (request,'EmpToMgr.html',d)

def EmpToDeptToMgr(request):
    OSLEDMO=EMP.objects.select_related('dept_no','mgr').all()
    OSLEDMO=EMP.objects.select_related('dept_no','mgr').filter(mgr__job='Developer')
    OSLEDMO=EMP.objects.select_related('dept_no','mgr').filter(job='Developer')
    OSLEDMO=EMP.objects.select_related('dept_no','mgr').filter(dept_no__dept_no=20)



    d={'OSLEDMO':OSLEDMO}
    return render(request,'EmpToDeptToMgr.html',d)

def DeptToEmpPrefetchTable(request):
    QSLDEO=Dept.objects.prefetch_related('emp_set').all
    QSLDEO=Dept.objects.prefetch_related('emp_set').filter(dname__in=('development','Maintainance'))
    QSLDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=EMP.objects.filter(job__in=('Intern','intern'))))
    
    d={'QSLDEO':QSLDEO}
    return render(request,'DeptToEmpPrefetchTable.html',d)