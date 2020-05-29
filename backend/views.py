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
    return render(request, 'backend/sample/sample.html', context)


def sample_community(request):
    context = {}
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
