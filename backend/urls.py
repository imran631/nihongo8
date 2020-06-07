from django.urls import path

from backend.djangoapps.auth.views import (
    RegistView, LoginView, ResetView, ResetPasswordView, ActiveView, LanguageView
)
from backend.djangoapps.manage.views import (
    WordView, WordMoidfyView, WordAddView,
    QuizView, QuizModifyView, QuizAddView,
    ProblemView, ProblemMoidfyView, ProblemAddView
)
from . import views


urlpatterns = [

    # Updated
    path('login', LoginView.as_view()),
    path('regist', RegistView.as_view()),
    path('active', ActiveView.as_view()),
    path('reset', ResetView.as_view()),
    path('reset_password', ResetPasswordView.as_view()),
    path('language', LanguageView.as_view()),

    path('manage/word/list', WordView.as_view()),
    path('manage/word/modify', WordMoidfyView.as_view()),
    path('manage/word/add', WordAddView.as_view()),

    path('manage/quiz/list', QuizView.as_view()),
    path('manage/quiz/modify', QuizModifyView.as_view()),
    path('manage/quiz/add', QuizAddView.as_view()),

    path('manage/problem/list', ProblemView.as_view()),
    path('manage/problem/modify', ProblemMoidfyView.as_view()),
    path('manage/problem/add', ProblemAddView.as_view()),

    # Update target
    path('', views.index, name='index'),
    path('jlpt', views.jlpt, name='jlpt'),

    path('problem/list', views.problem_list, name='problem_list'),
    path('problem/detail', views.problem_detail, name='problem_detail'),
    path('problem/quiz', views.problem_quiz, name='problem_quiz'),
    path('problem/result', views.problem_result, name='problem_result'),

    path('mypage', views.mypage, name='mypage'),
    path('mypage/modify', views.mypage_modify, name='mypage_modify'),

    path('sample', views.sample, name='sample'),
    path('sample/community', views.sample_community, name='sample_community'),
    path('sample/community/detail', views.sample_community_detail, name='sample_community_detail'),
    path('sample/community/write', views.sample_community_write, name='sample_community_write'),
    path('sample/community/modify', views.sample_community_modify, name='sample_community_modify'),
]