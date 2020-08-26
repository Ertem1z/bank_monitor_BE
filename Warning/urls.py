# _*_ coding:utf-8 _*_
# 开发人员：wangxiaofu
# 开发时间：2020/7/19 9:59
# 文件名称：urls.py
# 开发工具：PyCharm
from Warning import views
from Warning.views import AlertThreshold
from django.urls import path
from django.views import View
urlpatterns = [
    path('alert_threshold/', AlertThreshold.as_view()),

]