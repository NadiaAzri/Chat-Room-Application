from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth import get_user_model
from .models import ProfileUser
User = get_user_model()

class SignupForm(forms.ModelForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password')


class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())