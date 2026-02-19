from django import forms
from app.models import *
class TopicForm(forms.Form):

    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()