# _*_ coding:utf-8 _*_
# 开发人员：wangxiaofu
# 开发时间：2020/6/21 11:00
# 文件名称：urls.py.py
# 开发工具：PyCharm
from User.views import UsersList, AuthView
from django.urls import path

urlpatterns = [
    path('', UsersList.as_view()),
    path('auth/', AuthView.as_view()),
]