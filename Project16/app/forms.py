from django import forms
from app.models import *

class TopicMF(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageMF(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        exclude=['topic_name']


class AcessRecordMF(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        exclude=['name']
