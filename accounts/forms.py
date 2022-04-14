from dataclasses import field, fields
from tabnanny import verbose
from  django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Address

class SignupForm(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم',
    widget=forms.TextInput(attrs={'placeholder':'اسم ','class':'text-end'})) 
    email = forms.EmailField(label=' الايميل') 
    password1 = forms.CharField(label='كلمه السر ') 
    password2 = forms.CharField(label=' تاكيد كلمه السر ')

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserForms(forms.ModelForm):
    class Meta:
        model =User
        fields=['first_name','last_name','email']

class ProfileForms(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['image','phone_number']

class AddressForms(forms.ModelForm):
    class Meta:
        model =Address
        fields=['country','phone_number','Street_name','Building_name_or_number','Region','district','Governorate','nearest_mark']



