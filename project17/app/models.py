from django.db import models

# Create your models here.

class School(models.Model):
    school=models.CharField(max_length=100)
    location=models.CharField(max_length=100)