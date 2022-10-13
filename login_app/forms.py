
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class NewUserForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class EditProfile(forms.ModelForm):
    dob= forms.DateField(widget=forms.TextInput(attrs={'type':'date'}),required=False)
    class Meta:
        model = UserProfile
        exclude = ('user',)