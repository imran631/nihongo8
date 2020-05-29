from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context = {}
    return render(request, 'backend/index/index.html', context)


def login(request):

    context = {}
    return render(request, 'backend/auth/login.html', context)


def regist(request):

    context = {}
    return render(request, 'backend/auth/regist.html', context)


def reset_password(request):

    context = {}
    return render(request, 'backend/auth/reset_password.html', context)


def reset(request):

    context = {}
    return render(request, 'backend/auth/reset.html', context)


def sample(request):

    context = {}
    return render(request, 'backend/auth/sample.html', context)