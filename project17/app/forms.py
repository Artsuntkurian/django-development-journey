from app.models import *
from django import forms

class SchoolMF(forms.ModelForm):
    class Meta():
        model=School
        fields="__all__"