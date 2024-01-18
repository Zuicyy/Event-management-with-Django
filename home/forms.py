# home/forms.py
from django import forms
from django.contrib.auth.forms import RegistrationForm
from django.contrib.auth.models import User

#class RegistrationForm(forms.Form):
class SignupForm(RegistrationForm):
    model=User
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
