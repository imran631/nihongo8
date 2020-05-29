from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('login', views.login, name='login'),
    path('regist', views.regist, name='regist'),
    path('reset', views.reset, name='reset'),
    path('reset_password', views.reset_password, name='reset_password'),

    path('sample', views.sample, name='sample'),
    path('sample/community', views.sample_community, name='sample_community'),
    path('sample/community/detail', views.sample_community_detail, name='sample_community_detail'),
    path('sample/community/write', views.sample_community_write, name='sample_community_write'),
    path('sample/community/modify', views.sample_community_modify, name='sample_community_modify'),
]