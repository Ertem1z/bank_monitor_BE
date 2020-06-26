# _*_ coding:utf-8 _*_
# 开发人员：wangxiaofu
# 开发时间：2020/6/22 16:48
# 文件名称：urls.py.py
# 开发工具：PyCharm
from Monitor import views
from Monitor.views import HistoricalData
from django.urls import path
from django.views import View

urlpatterns = [
    # path('auth/', AuthView.as_view()),
    path('historical_data/', HistoricalData.as_view()),
    path('test/', HistoricalData.as_view()),
    path('add_data/', views.add_data),
    path('get_realtime_data/', views.get_realtime_data),
    path('realtime_data/', views.realtime_data)
]
