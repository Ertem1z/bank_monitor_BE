import json

from ResourceManagement.models import Resource
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def getResourceList(request):
    res={}
    alldata=Resource.objects.filter().values()
    if alldata.exists():
        res['data']=list(alldata)
        ret=json.dumps(res)
        print('get ResourceList successful')
        return HttpResponse(ret)
    else:
        res['data']=[]
        ret=json.dumps(res)
        return HttpResponse(ret)

#新增
def addResource(request):
    dic={}
    dic['id']=request.POST.get('id')
    dic['tag']=request.POST.get('tag')
    dic['model']=request.POST.get('model')
    dic['ip_address']=request.POST.get('ip')
    dic['type']=request.POST.get('type')
    dic['state']= False
    # Resource.objects.create(**dic)
    # print('Add resource successful')
    # return HttpResponse(status=200)
    try:
        Resource.objects.create(**dic)
        print('Add resource successful')
        return HttpResponse(status=200)
    except Exception as info:
        print(info)
        return HttpResponse(status=204)

#修改
def editResource(request):
    dic={}
    dic['id']=request.POST.get('id')
    dic['tag']=request.POST.get('tag')
    dic['model']=request.POST.get('model')
    dic['ip_address']=request.POST.get('ip')
    dic['type']=request.POST.get('type')
    dic['state']= False
    print(dic)
    try:
        Resource.objects.filter(ip=request.POST.get('id')).update(dic)
        print('Update resource successful')
        return HttpResponse(status=200)
    except Exception as info:
        print(info)
        return HttpResponse(status=204)


#加入监控
def AddResourceById(request):
    id=request.POST.get('id')
    state=Resource.objects.filter(id=id).values()
    if state.exists():
        Resource.objects.filter(id=id).update(state=True)
        print('Add monitor successful')
        return HttpResponse(status=200)
    else:
        print('Add monitor fail')
        return HttpResponse(status=204)


#退出监控
def delResourceById(request):
    id=request.POST.get('id')
    state=Resource.objects.filter(id=id).values()
    if state.exists():
        Resource.objects.filter(id=id).update(state=False)
        print('Del monitor successful')
        return HttpResponse(status=200)
    else:
        print('Del monitor fail')
        return HttpResponse(status=204)


#从数据库移除资源
def removeResourceById(request):
    id=request.POST.get('id')
    #print(id)
    state=Resource.objects.filter(id=id).values()
    if state.exists():
        Resource.objects.filter(id=id).delete()
        print('Del resource successful')
        return HttpResponse(status=200)
    else:
        print('Del resource fail')
        return HttpResponse(status=204)


