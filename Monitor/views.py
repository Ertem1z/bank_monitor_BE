import json
import datetime
import random
import datetime

from Monitor.serializers import CPUSerializer, NetWorkSerializer, SystemMemorySerializer
from django.core import serializers
from django.shortcuts import render
from django.utils.datetime_safe import strftime

from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from Monitor.models import *
from django.http import JsonResponse, HttpResponse
from django.db.models.fields import DateTimeField


# Create your views here.
# post&get获取历史数据
class HistoricalData(APIView):

    # @require_POST
    # @csrf_exempt
    @staticmethod
    # @api_view
    def post(request):
        # 根据ip和时间范围返回历史数据
        ip_address = request.POST.get("ip")
        startstamp = int(int(str(request.POST.get("date[0]")).strip()) / 1000)
        endstamp = int(int(str(request.POST.get("date[1]")).strip()) / 1000)
        s = datetime.datetime.fromtimestamp(startstamp)
        e = datetime.datetime.fromtimestamp(endstamp)
        # print(s)
        # print(e)
        # start_date = datetime.datetime.strptime(start, "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
        # end_date = datetime.datetime.strptime(end, "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")

        if ip_address is None:
            print("ip信息缺失！")
            return HttpResponse("ip信息缺失！")

        else:
            # data_all = {}
            # cpu = CPU.objects.filter(ip_address=ip_address, time__range=(s, e))
            # cpu_serializer = CPUSerializer(cpu, many=True)
            # nw = Network.objects.filter(ip_address=ip_address, time__range=(s,e))
            # nw_serializer = NetWorkSerializer(nw, many=True)
            # memory = SystemMemory.objects.filter(ip_address=ip_address, time__range=(s,e))
            # memory_serializer = SystemMemorySerializer(memory, many=True)
            #
            # data_all['cpu'] = cpu_serializer.data
            # data_all['network'] = nw_serializer.data
            # data_all['memory'] = memory_serializer.data
            # # data_all = {'cpu': cpu_serializer.data, 'network': nw_serializer.data, 'systemmemory': memory_serializer.data}
            # if data_all :
            #     print("查询成功！返回结果中...")
            #     return HttpResponse(json.dumps(data_all))
            # else:
            #     print("无查询结果！")
            #     return HttpResponse("无查询结果！")
            cpu_time = []
            nw_time = []
            memory_time = []
            CPU_used_total = []
            CPU_used_user = []
            CPU_used_system = []
            dev_io_read_rate = []
            dev_io_write_rate = []
            dev_io_usage_rate = []
            mem_usage_rate = []
            swap_usage_rate = []
            available_memory = []
            cpu_data = CPU.objects.filter(ip_address=ip_address, time__range=(s, e)).values()
            nw_data = Network.objects.filter(ip_address=ip_address, time__range=(s, e)).values()
            memory_data = SystemMemory.objects.filter(ip_address=ip_address, time__range=(s, e)).values()
            # cpu_serializer = serializers.serialize("json", cpu_data)
            # nw_serializer = serializers.serialize("json", nw_data)
            # memory_serializer = serializers.serialize("json", memory_data)

            for cpu in cpu_data:
                print(cpu.get('time'))
                cpu_time.append(str(cpu.get('time')))
                CPU_used_total.append(cpu.get('cpu_used_total'))
                CPU_used_user.append(cpu.get('cpu_user_used'))
                CPU_used_system.append(cpu.get('cpu_system_used'))

            for nw in nw_data:
                # print(nw)
                nw_time.append(str(nw.get('time')))
                dev_io_read_rate.append(nw.get('tcp_passiveopens'))
                dev_io_write_rate.append(nw.get('tcp_activeopens'))
                dev_io_usage_rate.append(nw.get('close_wait_count'))

            for memory in memory_data:
                # print(memory)
                memory_time.append(str(memory.get('time')))
                mem_usage_rate.append(memory.get('mem_usage_rate'))
                available_memory.append(memory.get('available_memory'))
                swap_usage_rate.append(memory.get('swap_usage_rate'))

            data_all = {}
            data_all["cpu_time"] = cpu_time
            data_all["nw_time"] = nw_time
            data_all["memory_time"] = memory_time
            data_all["CPU_used_total"] = CPU_used_total
            data_all["CPU_used_user"] = CPU_used_user
            data_all["CPU_used_system"] = CPU_used_system
            data_all["dev_io_read_rate"] = dev_io_read_rate
            data_all["dev_io_write_rate"] = dev_io_write_rate
            data_all["dev_io_usage_rate"] = dev_io_usage_rate
            data_all["mem_usage_rate"] = mem_usage_rate
            data_all["available_memory"] = available_memory
            data_all["swap_usage_rate"] = swap_usage_rate

            if data_all:
                print("查询成功！返回结果中...")
                return HttpResponse(json.dumps(data_all))

    def get(self, request):
        cpu_data = serializers.serialize("json", CPU.objects.all())
        nw_data = serializers.serialize("json", Network.objects.all())
        memory_data = serializers.serialize("json", SystemMemory.objects.all())
        data_all = {'cpu': cpu_data, 'network': nw_data, 'systemmemory': memory_data}
        return HttpResponse(json.dumps(data_all))


def add_data(request):
    # 手动添加数据
    ip_list = ['52.82.122.115',
               '52.82.122.116',
               '52.82.122.117',
               '52.82.122.118',
               '52.82.122.119']
    for ip in ip_list:
        cpu = CPU()
        cpu.ip_address = ip
        cpu.cpu_average_5min = random.random()
        cpu.cpu_system_used = random.random()
        cpu.cpu_used_total = random.random()
        cpu.cpu_user_used = random.random()
        cpu.cpu_io_wait = random.randint(0, 100)
        cpu.save()
        network = Network()
        network.ip_address = ip
        network.close_wait_count = random.randint(0, 100)
        network.tcp_activeopens = random.random()
        network.tcp_passiveopens = random.random()
        network.save()
        memory = SystemMemory()
        memory.ip_address = ip
        memory.available_memory = random.random()
        memory.free_swap_spacecon = random.random()
        memory.mem_usage_rate = random.random()
        memory.swap_usage_rate = random.random()
        memory.save()
    return HttpResponse("test数据插入成功")


def get_realtime_data(request):
    # 不断生成实时数据并保存至数据库中
    ip_list = ['52.82.122.115',
               '52.82.122.116',
               '52.82.122.117',
               '52.82.122.118',
               '52.82.122.119']
    for ip in ip_list:
        cpu = CPU()
        cpu.ip_address = ip
        cpu.cpu_average_5min = random.random() * 100
        cpu.cpu_system_used = random.random() * 100
        cpu.cpu_used_total = random.random() * 100
        cpu.cpu_user_used = random.random() * 100
        cpu.cpu_io_wait = random.randint(0, 100)
        cpu.save()
        network = Network()
        network.ip_address = ip
        network.close_wait_count = random.randint(0, 100)
        network.tcp_activeopens = random.random() * 100
        network.tcp_passiveopens = random.random() * 100
        network.save()
        memory = SystemMemory()
        memory.ip_address = ip
        memory.available_memory = random.random() * 100
        memory.free_swap_spacecon = random.random() * 100
        memory.mem_usage_rate = random.random() * 100
        memory.swap_usage_rate = random.random() * 100
        memory.save()
    return HttpResponse("实时数据加入成功！")


def realtime_data(request):
    # 返回指定ip的最新数据
    ip_address = request.POST.get("ip")
    if ip_address is None:
        print("ip信息缺失！")
        return HttpResponse("ip信息缺失！")

    else:
        realtime_cpu = CPU.objects.filter(ip_address=ip_address).last()
        realtime_nw = Network.objects.filter(ip_address=ip_address).last()
        realtime_memory = SystemMemory.objects.filter(ip_address=ip_address).last()

        data_all = {}
        data_all["CPU_used_total"] = realtime_cpu.cpu_used_total
        data_all["CPU_used_user"] = realtime_cpu.cpu_user_used
        data_all["CPU_used_system"] = realtime_cpu.cpu_system_used
        data_all["dev_io_read_rate"] = realtime_nw.tcp_passiveopens
        data_all["dev_io_write_rate"] = realtime_nw.tcp_activeopens
        data_all["dev_io_usage_rate"] = realtime_nw.close_wait_count
        data_all["mem_usage_rate"] = realtime_memory.mem_usage_rate
        data_all["available_memory"] = realtime_memory.available_memory
        data_all["swap_usage_rate"] = realtime_memory.swap_usage_rate
        
    print("查询成功！返回实时数据...")
    return HttpResponse(json.dumps(data_all))
