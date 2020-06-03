import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _

from .models import UserProfile
from .forms import RegistForm, LoginForm, ResetForm


logger = logging.getLogger(__name__)

class RegistView(View):
    template_name = 'backend/auth/regist.html'

    def get(self, request, *args, **kwargs):
        form = RegistForm()
        return render(request, self.template_name, {'form': form})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = RegistForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile(
                user = user,
                jlpt = form.cleaned_data["jlpt"]
            ).save()
            return HttpResponseRedirect('/login?success=regist')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'backend/auth/login.html'

    def get(self, request, *args, **kwargs):
        success = request.GET.get('success')
        form = LoginForm()
        context = {}
        context['form'] = form
        context['success'] = success
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.is_login(request):
                return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class ResetView(View):
    template_name = 'backend/auth/reset.html'

    def get(self, request, *args, **kwargs):
        form = ResetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ResetForm(request.POST)
        if form.is_valid():
            if form.is_excute():
                return JsonResponse({'result': 200})
        return JsonResponse({'result': 500})


def index(request):
    context = {}
    return render(request, 'backend/index/index.html', context)


def mypage(request):
    context = {}
    return render(request, 'backend/mypage/mypage.html', context)


def mypage_modify(request):
    context = {}
    return render(request, 'backend/mypage/mypage_modify.html', context)


def jlpt(request):
    context = {}
    return render(request, 'backend/jlpt/jlpt.html', context)


def admin_core(request):
    context = {}
    return render(request, 'backend/admin/core.html', context)


def admin_core_regist(request):
    context = {}
    return render(request, 'backend/admin/core_regist.html', context)


def admin_quiz(request):
    context = {}
    return render(request, 'backend/admin/quiz.html', context)


def admin_quiz_regist(request):
    context = {}
    return render(request, 'backend/admin/quiz_regist.html', context)


def admin_problem(request):
    context = {}
    return render(request, 'backend/admin/problem.html', context)


def admin_problem_regist(request):
    context = {}
    return render(request, 'backend/admin/problem_regist.html', context)


def problem_list(request):
    context = {}
    return render(request, 'backend/problem/list.html', context)


def problem_detail(request):
    context = {}
    return render(request, 'backend/problem/detail.html', context)


def problem_quiz(request):
    context = {}
    return render(request, 'backend/problem/quiz.html', context)


def problem_result(request):
    context = {}
    return render(request, 'backend/problem/result.html', context)


def reset_password(request):
    context = {}
    return render(request, 'backend/auth/reset_password.html', context)


def sample(request):
    context = {}
    return render(request, 'backend/sample/sample.html', context)


def sample_community(request):
    sample = [1,2,3,4,5,6,7,8,9,10]
    context = {}
    context['sample'] = sample
    return render(request, 'backend/sample/community.html', context)


def sample_community_detail(request):
    context = {}
    return render(request, 'backend/sample/community_detail.html', context)


def sample_community_write(request):
    context = {}
    return render(request, 'backend/sample/community_write.html', context)


def sample_community_modify(request):
    context = {}
    return render(request, 'backend/sample/community_modify.html', context)
