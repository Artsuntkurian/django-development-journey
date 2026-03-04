from django import forms
from app.models import *


class TopicMF(forms.ModelForm):
    class Meta:
        model=Topics
        fields='__all__'


 