# _*_ coding:utf-8 _*_
# 开发人员：wangxiaofu
# 开发时间：2020/6/21 11:08
# 文件名称：serializers.py.py
# 开发工具：PyCharm

from rest_framework import serializers
from Monitor.models import *


class CPUSerializer(serializers.ModelSerializer):
    # time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = CPU
        fields = '__all__'


class NetWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class SystemMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMemory
        fields = '__all__'


