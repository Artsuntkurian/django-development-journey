from django import forms
g=[('Male','Male'),('Female','Female')]


def check_for_m(value):
    if value[0].lower()=='m':
        raise forms.ValidationError('Starting with M')
    
def length_check(value):
    if len(value)<5:
        raise forms.ValidationError('Lenght is less ')
class ContactForm(forms.Form):

    name=forms.CharField(validators=[check_for_m,length_check])
    age=forms.IntegerField()
    #gender=forms.ChoiceField(choices=g)
    #m=forms.MultipleChoiceField(choices=g)
    #course=forms.MultipleChoiceField(choices=g,widget=forms.CheckboxSelectMultiple)
    
    #c=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    email=forms.EmailField()
    re_enter_email=forms.EmailField()


    botcapture=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_enter_email']
        if e!=re:
            raise forms.ValidationError('missmatch')

    def clean_botcapture(self):
        b=self.cleaned_data['botcapture']
        if len(b)>0:
            raise forms.ValidationError('botcapture')
