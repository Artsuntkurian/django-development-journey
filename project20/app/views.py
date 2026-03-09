from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import csv
from app.models import *


def insert_bank(self):
    with open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\QSpiders\\PYTHON\\Django\\Qspiders\\Scripts\\project20\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data is inserted successfully')


def insert_branch(self):
    with open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\QSpiders\\PYTHON\\Django\\Qspiders\\Scripts\\project20\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
                
    
    
    
    
    
    return HttpResponse('Branch data is inserted successfully')









