from django import forms
from app.models import *


class DeptForm(forms.Form):
    deptno=forms.IntegerField()
    dname=forms.CharField()
    dlocation=forms.CharField()

class EmpForm(forms.Form):
    empno=forms.IntegerField()
    ename=forms.CharField()
    job=forms.CharField()
    mgr=forms.ModelChoiceField(queryset=Emp.objects.all())
    sal=forms.DecimalField()
    comm=forms.DecimalField()
    deptno=forms.ModelChoiceField(queryset=Dept.objects.all())



## MODEL FORMS CODE 

class DeptModelForm(forms.ModelForm):
    class Meta:
        model=Dept
        fields='__all__'
    # fields=['deptno','dname','dlocation']
    # exclude=['coloumnName','coloumName2']
    # widgets={'forkeycolum name':forms.RadioSelect}
        help_texts={'deptno':'Write deptnumber'}
        labels={'deptno':'Department Number'}
