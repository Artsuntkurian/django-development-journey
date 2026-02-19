from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.dept_no)
class EMP(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    hire_date=models.DateField(null=True)
    sal=models.IntegerField(null=True)
    comm=models.IntegerField(null=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.ename
    

class SALGRADE(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.IntegerField(null=True)
    hisal=models.IntegerField(null=True)