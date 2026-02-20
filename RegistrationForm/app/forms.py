from app.models import *
from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:

        model=User
        #fields='__all__'
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}
class ProfileModelForm(forms.ModelForm):
    class Meta:

        model=Profile
        fields='__all__'
        exclude=['username']