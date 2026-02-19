from django.db import models
from django import forms
# Create your models here.
from django.core.validators import RegexValidator,MinLengthValidator


def check_for_A(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('A in name')

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100,validators=[check_for_A])
    email=models.EmailField()
    number=models.CharField(max_length=10,validators=[RegexValidator('[6-9]\d{9}'),MinLengthValidator(10)])