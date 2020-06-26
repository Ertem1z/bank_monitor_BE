# _*_ coding:utf-8 _*_
# 开发人员：wangxiaofu
# 开发时间：2020/6/21 11:08
# 文件名称：serializers.py.py
# 开发工具：PyCharm

from rest_framework import serializers
from User.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Users
