# home/forms.py
from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput, label='Create New Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    agree_terms = forms.BooleanField(required=True, label='I agree to the Terms & Conditions')
