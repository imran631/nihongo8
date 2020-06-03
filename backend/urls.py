from django.urls import path

from backend.views import RegistView, LoginView, ResetView
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('jlpt', views.jlpt, name='jlpt'),

    path('manage/core', views.admin_core, name='admin_core'),
    path('manage/core/regist', views.admin_core_regist, name='admin_core_regist'),
    path('manage/quiz', views.admin_quiz, name='admin_quiz'),
    path('manage/quiz/regist', views.admin_quiz_regist, name='admin_quiz_regist'),
    path('manage/provblem', views.admin_problem, name='admin_problem'),
    path('manage/problem/regist', views.admin_problem_regist, name='admin_problem_regist'),

    path('problem/list', views.problem_list, name='problem_list'),
    path('problem/detail', views.problem_detail, name='problem_detail'),
    path('problem/quiz', views.problem_quiz, name='problem_quiz'),
    path('problem/result', views.problem_result, name='problem_result'),

    path('login', LoginView.as_view()),
    path('regist', RegistView.as_view()),
    path('reset', ResetView.as_view()),
    path('reset_password', views.reset_password, name='reset_password'),

    path('mypage', views.mypage, name='mypage'),
    path('mypage/modify', views.mypage_modify, name='mypage_modify'),

    path('sample', views.sample, name='sample'),
    path('sample/community', views.sample_community, name='sample_community'),
    path('sample/community/detail', views.sample_community_detail, name='sample_community_detail'),
    path('sample/community/write', views.sample_community_write, name='sample_community_write'),
    path('sample/community/modify', views.sample_community_modify, name='sample_community_modify'),
]