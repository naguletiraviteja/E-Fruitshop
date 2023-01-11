from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class Forms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","password","email"]


    def __init__(self,*args,**kwargs):
        super(Forms,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter username'
        self.fields['password'].widget.attrs['placeholder'] = 'Create Password'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
