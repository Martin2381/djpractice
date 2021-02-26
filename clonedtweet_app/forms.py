from django import forms

from clonedtweet_app.models import CustomUser

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    display_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)