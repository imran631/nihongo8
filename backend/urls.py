from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('jlpt', views.jlpt, name='jlpt'),

    path('admin/core', views.admin_core, name='admin_core'),
    path('admin/core/regist', views.admin_core_regist, name='admin_core_regist'),
    path('admin/quiz', views.admin_quiz, name='admin_quiz'),
    path('admin/quiz/regist', views.admin_quiz_regist, name='admin_quiz_regist'),
    path('admin/problem', views.admin_problem, name='admin_problem'),
    path('admin/problem/regist', views.admin_problem_regist, name='admin_problem_regist'),

    path('problem/list', views.problem_list, name='problem_list'),
    path('problem/detail', views.problem_detail, name='problem_detail'),
    path('problem/quiz', views.problem_quiz, name='problem_quiz'),
    path('problem/result', views.problem_result, name='problem_result'),

    path('login', views.login, name='login'),
    path('regist', views.regist, name='regist'),
    path('reset', views.reset, name='reset'),
    path('reset_password', views.reset_password, name='reset_password'),

    path('mypage', views.mypage, name='mypage'),
    path('mypage/modify', views.mypage_modify, name='mypage_modify'),

    path('sample', views.sample, name='sample'),
    path('sample/community', views.sample_community, name='sample_community'),
    path('sample/community/detail', views.sample_community_detail, name='sample_community_detail'),
    path('sample/community/write', views.sample_community_write, name='sample_community_write'),
    path('sample/community/modify', views.sample_community_modify, name='sample_community_modify'),
]