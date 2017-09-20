from django import forms

from django.contrib.auth.models import User

from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())# this
    class Meta():
        model=User
        fields= ['username','email','password'] # these fields are available in the user class
        


class UserProfileInfoForm(forms.ModelForm):    
    class Meta():
        model = UserProfileInfo
        exclude=['user',]