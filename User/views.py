import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import time
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from User.models import *
from User.serializers import UserSerializer
from django.views.decorators.csrf import csrf_protect


# 获取用户列表
class UsersList(APIView):
    def get(self, request):
        queryset = Users.objects.all()
        ret = UserSerializer(queryset, many=True)
        return Response(ret.data)

    def post(self, requests):
        users = UserSerializer(data=requests.data)
        if users.is_valid():
            users.save()
            return Response(users.data)
        else:
            return Response(users.errors)


class AuthView(APIView):

    # @csrf_protect
    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}
        try:
            # 参数是datadict 形式
            usr = request.POST.get("username")
            pas = request.POST.get("password")

            # usr = request._request.POST.get('username')
            # pas = request._request.POST.get('password')

            # usr = request.POST.get('username')
            # pas = request.POST.get('password')

            print("usr:", usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = Users.objects.filter(username=usr, password=pas).first()
            print("obj:", obj)
            print("type(obj):",type(obj))
            print("obj.usr:", obj.username)
            print("obj.pas:", obj.password)

            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = str(time.time()) + usr
            print(token)
            UserToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            ret['token'] = token
            ret['csrftoken'] = request.COOKIES['csrftoken']

        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
            print(e)
        return JsonResponse(ret)
