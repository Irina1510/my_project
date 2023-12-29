from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(label='Логин',
                widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    # class Meta:
    #     model = User
    #     fields = ('username', 'password')


class RegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')