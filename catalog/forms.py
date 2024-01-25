from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Review, Hotel


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


class AddReviewForm(forms.ModelForm):

    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), empty_label="Отель не выбран",
                                   label="Название отеля")

    class Meta:
        model = Review
        fields = ('hotel', 'comment', 'rating')
        widgets = {
           'comment': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
