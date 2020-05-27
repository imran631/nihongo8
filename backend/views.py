from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context = {}
    return render(request, 'backend/index.html', context)


def sample(request):

    context = {}
    return render(request, 'backend/sample.html', context)