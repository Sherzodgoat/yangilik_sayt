from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length = 120)
    password = forms.CharField(max_length = 128)


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password' ]


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ]



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'phone']




class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']