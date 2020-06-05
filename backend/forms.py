import logging

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _

from backend.validators import not_in_admin, min_username


logger = logging.getLogger(__name__)


class RegistForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control", 
            'placeholder': '아이디를 입력하십시오.'
        }),
        validators=[not_in_admin, min_username],
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


class ResetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': '비밀번호를 입력하십시오.'
        })
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': '비밀번호 확인을 입력하십시오.'
        })
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')