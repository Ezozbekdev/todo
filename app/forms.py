from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Main


class MainEditFrom(forms.ModelForm):
    class Meta:
        model = Main
        fields = ["title", 'img']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
