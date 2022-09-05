# I created this file to allow for the addition of fields to standard Django forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Adding an email input to the Django's existing UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
