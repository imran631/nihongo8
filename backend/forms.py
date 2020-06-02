from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login

from backend.validators import not_in_admin


class RegistForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control", 
            'placeholder': '아이디를 입력하십시오.'
        }),
        validators=[not_in_admin],
        error_messages={
            'unique': _("ID already exists."),
        }
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "form-control", 
            'placeholder': '이메일을 입력하십시오.'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': '비밀번호를 입력하십시오.'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': '비밀번호 확인을 입력하십시오.'
        })
    )

    JLPT_CHOICES = (
        ('N0', '자격증 없음'),
        ('N5', 'JLPT N5'),
        ('N4', 'JLPT N4'),
        ('N3', 'JLPT N3'),
        ('N2', 'JLPT N2'),
        ('N1', 'JLPT N1')
    )
    jlpt = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': "form-control custom-select"
        }), 
        choices=JLPT_CHOICES
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control", 
            'placeholder': '아이디를 입력하십시오.'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': '비밀번호를 입력하십시오.'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def is_login(self, request):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            self.errors['username'] = [_('ID or password does not match.')]
            return False


class ResetForm(forms.Form):

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "form-control", 
            'placeholder': '이메일을 입력하십시오.'
        })
    )

    class Meta:
        model = User
        fields = ('email')
