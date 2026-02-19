from app.models import *
from django import forms


class TopicModelForm(forms.ModelForm):
    Re_Enter_email=forms.EmailField()
    botcap=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Topic
        fields="__all__"

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['Re_Enter_email']
        if e!=re:
            raise forms.ValidationError('email not matched')
        
    def clean_botcap(self):
        bot=self.cleaned_data['botcap']
        if len(bot)>0:
            raise forms.ValidationError('bot capture caught')
        