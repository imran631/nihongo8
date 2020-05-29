from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('regist', views.regist, name='regist'),
    path('reset', views.reset, name='reset'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('sample', views.sample, name='sample'),
]