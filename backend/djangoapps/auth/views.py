import logging

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from backend.models import UserProfile
from backend.mixin import SendMailMixin, TokenPackerMixin, LoginSuccessTxtMixin
from backend.forms import RegistForm, LoginForm, ResetForm, ResetPasswordForm


logger = logging.getLogger(__name__)


class RegistView(View, SendMailMixin):

    template_name = 'backend/auth/regist.html'

    def get(self, request, *args, **kwargs):
        form = RegistForm()
        return render(request, self.template_name, {'form': form})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = RegistForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            if len(users) == 0:
                user = form.save()
                user.is_active = 0
                user.save()
                UserProfile(user=user, jlpt=form.cleaned_data["jlpt"]).save()
                super().send_mail(request, user, 'regist')
                return JsonResponse({'result': 200})
            else:
                form.errors['username'] = [_('Email already registered.')]
        return JsonResponse({'result': 500, 'errors': form.errors})


class ActiveView(View, TokenPackerMixin, PasswordResetTokenGenerator):

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        try:
            token_code, email = super().unpacking(token)
        except BaseException as e:
            logger.error(e)
            return redirect('/login?type=non_active&alert=fail')
        user = User.objects.filter(email=email).first()
        if super().check_token(user, token_code):
            user.is_active = 1
            user.save()
            return redirect('/login?type=active&alert=success')


class LoginView(View, LoginSuccessTxtMixin):

    template_name = 'backend/auth/login.html'

    def get(self, request, *args, **kwargs):
        type = request.GET.get('type')
        alert = request.GET.get('alert')
        alert_txt1, alert_txt2 = super().makeText(type)
        form = LoginForm()
        context = {'form': form, 'alert': alert, 'alert_txt1': alert_txt1, 'alert_txt2': alert_txt2}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'result': 200})
            else:
                users = User.objects.filter(username=username)
                if len(users) > 0:
                    user = users.first()
                    if user.is_active == 0:
                        form.errors['username'] = [_('Your account has not been activated. Please check your identity email.')]
                else:
                    form.errors['username'] = [_('ID or password does not match.')]
        return JsonResponse({'result': 500, 'errors': form.errors})


class ResetView(View, SendMailMixin):
    template_name = 'backend/auth/reset.html'

    def get(self, request, *args, **kwargs):
        form = ResetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            if len(users) != 0:
                super().send_mail(request, users.first(), 'reset')
                return JsonResponse({'result': 200})
            else:
                form.errors['email'] = [_('This email is not registered.')]
        return JsonResponse({'result': 500, 'errors': form.errors})


class ResetPasswordView(View, TokenPackerMixin, PasswordResetTokenGenerator):
    template_name = 'backend/auth/reset_password.html'

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        try:
            token_code, email = super().unpacking(token)
        except BaseException as e:
            logger.error(e)
            return redirect('/login')
        form = ResetPasswordForm(user=None)
        context = {'form': form, 'token': token}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        try:
            token_code, email = super().unpacking(token)
        except BaseException as e:
            logger.error(e)
            return redirect('/login')
        user = User.objects.filter(email=email).first()
        form = ResetPasswordForm(data=request.POST, user=user)
        if super().check_token(user, token_code):
            if form.is_valid():
                form.save()
                return JsonResponse({'result': 200})
        else:
            form.errors['new_password1'] = [_('The link has expired. If you want to change it, send an email again.')]
        return JsonResponse({'result': 500, 'errors': form.errors})