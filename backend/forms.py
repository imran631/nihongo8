import logging

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import validators
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

from backend.validators import not_in_admin
from backend.util import AESCipher


logger = logging.getLogger(__name__)

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

    def is_excute(self):
        email = self.cleaned_data["email"]
        users = User.objects.filter(email=email)
        user = users.first()
        text = str(user.id)
        cipher = AESCipher(settings.AES_KEY)
        token = cipher.encrypt(text).decode('ascii')
        subject = '[日本語８] 비밀번호 초기화 메일'
        message = get_template('backend/email/reset_template.html').render(
            {
                'base_url': settings.BASE_URL + 'reset_password',
                'token': token
            }
        )
        if len(users) > 0:
            user = users.first()
            from_email = settings.EMAIL_HOST_EMAIL
            recipient_list = [email]
            send_mail(
                subject, 
                None, 
                from_email, 
                recipient_list,
                False,
                None,
                None,
                None,
                message
            )
            return True
        else:
            return False


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