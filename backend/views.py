from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'backend/index/index.html', context)


def jlpt(request):
    context = {}
    return render(request, 'backend/jlpt/jlpt.html', context)


def mypage(request):
    context = {}
    return render(request, 'backend/mypage/mypage.html', context)


def mypage_modify(request):
    context = {}
    return render(request, 'backend/mypage/mypage_modify.html', context)


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
