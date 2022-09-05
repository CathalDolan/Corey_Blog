# I created this file to allow for the addition of fields to standard Django forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Adding an email input to the Django's existing Django UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Allows the User to update their Username and Email from their Profile page
# This is combined with ProfileUpdateForm to look like a single form on the front end
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Allows the User to update their profile pic from their Profile page
# This is combined with UserUpdateForm to look like a single form on the front end
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
