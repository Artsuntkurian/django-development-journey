from django.db import models

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)


    def __str__(self):
        return self.school_name

class Student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()

    def __str__(self):
        return self.sname