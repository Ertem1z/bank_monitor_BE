import json
import datetime
import random
import datetime

from Monitor.serializers import CPUSerializer, NetWorkSerializer, SystemMemorySerializer
from Warning.models import Thresholds, PercentileThresholds
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

        if ip_address is None:
            print("ip信息缺失！")
            return HttpResponse("ip信息缺失！")

        else:

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

            for cpu in cpu_data:
                print(cpu.get('time'))
                cpu_time.append(str(cpu.get('time')))
                CPU_used_total.append(cpu.get('cpu_used_total'))
                CPU_used_user.append(cpu.get('cpu_user_used'))
                CPU_used_system.append(cpu.get('cpu_system_used'))

            for nw in nw_data:
                # print(nw)
                nw_time.append(str(nw.get('time')))
                dev_io_read_rate.append(nw.get('dev_io_read_rate'))
                dev_io_write_rate.append(nw.get('dev_io_write_rate'))
                dev_io_usage_rate.append(nw.get('dev_io_usage_rate'))

            for memory in memory_data:
                # print(memory)
                memory_time.append(str(memory.get('time')))
                mem_usage_rate.append(memory.get('mem_usage_rate'))
                available_memory.append(memory.get('available_memory'))
                swap_usage_rate.append(memory.get('swap_usage_rate'))

            # 获取阈值
            pre_th = Thresholds.objects.filter(ip_address=ip_address).last()

            line_cpu_used_total = [pre_th.cpu_used_total_t1,
                                   pre_th.cpu_used_total_t2,
                                   pre_th.cpu_used_total_t3]
            line_cpu_system_used = [pre_th.cpu_system_used_t1,
                                    pre_th.cpu_system_used_t2,
                                    pre_th.cpu_system_used_t3]
            line_cpu_user_used = [pre_th.cpu_user_used_t1,
                                  pre_th.cpu_user_used_t2,
                                  pre_th.cpu_user_used_t3]
            line_available_memory = [pre_th.available_memory_t1,
                                     pre_th.available_memory_t2,
                                     pre_th.available_memory_t3]
            line_mem_usage_rate = [pre_th.mem_usage_rate_t1,
                                   pre_th.mem_usage_rate_t2,
                                   pre_th.mem_usage_rate_t3]
            line_swap_usage_rate = [pre_th.swap_usage_rate_t1,
                                    pre_th.swap_usage_rate_t2,
                                    pre_th.swap_usage_rate_t3]
            line_dev_io_read_rate = [pre_th.dev_io_read_rate_t1,
                                     pre_th.dev_io_read_rate_t2,
                                     pre_th.dev_io_read_rate_t3]
            line_dev_io_write_rate = [pre_th.dev_io_write_rate_t1,
                                      pre_th.dev_io_write_rate_t2,
                                      pre_th.dev_io_write_rate_t3]
            line_dev_io_usage_rate = [pre_th.dev_io_usage_rate_t1,
                                      pre_th.dev_io_usage_rate_t2,
                                      pre_th.dev_io_usage_rate_t3]

            # 构造字典装载数据
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

            # 阈值线
            data_all['line_cpu_used_total'] = line_cpu_used_total
            data_all['line_cpu_system_used'] = line_cpu_system_used
            data_all['line_cpu_user_used'] = line_cpu_user_used
            data_all['line_available_memory'] = line_available_memory
            data_all['line_mem_usage_rate'] = line_mem_usage_rate
            data_all['line_swap_usage_rate'] = line_swap_usage_rate
            data_all['line_dev_io_read_rate'] = line_dev_io_read_rate
            data_all['line_dev_io_write_rate'] = line_dev_io_write_rate
            data_all['line_dev_io_usage_rate'] = line_dev_io_usage_rate

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
        network.dev_io_usage_rate = random.randint(0, 100)
        network.dev_io_write_rate = random.random()
        network.dev_io_read_rate = random.random()
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
        cpu.cpu_io_wait = random.randint(0, 100)
        csu = random.random() * 100
        cut = random.random() * 100
        cuu = random.random() * 100
        cpu.cpu_system_used = csu
        cpu.cpu_used_total = cut
        cpu.cpu_user_used = cuu
        cpu.save()

        network = Network()
        network.ip_address = ip
        nc = random.randint(0, 100)
        nta = random.random() * 100
        ntp = random.random() * 100
        network.dev_io_usage_rate = nc
        network.dev_io_write_rate = nta
        network.dev_io_read_rate = ntp
        network.save()

        memory = SystemMemory()
        memory.ip_address = ip
        memory.free_swap_spacecon = random.random() * 100
        mam = random.random() * 100
        mur = random.random() * 100
        msu = random.random() * 100
        memory.available_memory = mam
        memory.mem_usage_rate = mur
        memory.swap_usage_rate = msu
        memory.save()

        pt = PercentileThresholds.objects.filter(ip_address=ip).last()
        pre_th = Thresholds.objects.filter(ip_address=ip).last()
        print(type(pt), type(pre_th))
        pre_th.cpu_used_total_t3 = max(pre_th.cpu_used_total_t3, cut * pt.cpu_used_total_p3)
        pre_th.cpu_user_used_t3 = max(pre_th.cpu_user_used_t3, cuu * pt.cpu_user_used_p3)
        pre_th.cpu_system_used_t3 = max(pre_th.cpu_system_used_t3, csu * pt.cpu_system_used_p3)

        pre_th.dev_io_write_rate_t3 = max(pre_th.dev_io_write_rate_t3, nta * pt.dev_io_write_rate_p3)
        pre_th.dev_io_read_rate_t3 = max(pre_th.dev_io_read_rate_t3, ntp * pt.dev_io_read_rate_p3)
        pre_th.dev_io_usage_rate_t3 = max(pre_th.dev_io_usage_rate_t3, csu * pt.dev_io_usage_rate_p3)

        pre_th.mem_usage_rate_t3 = max(pre_th.mem_usage_rate_t3, mur * pt.mem_usage_rate_p3)
        pre_th.swap_usage_rate_t3 = max(pre_th.swap_usage_rate_t3, msu * pt.swap_usage_rate_p3)
        pre_th.available_memory_t3 = max(pre_th.available_memory_t3, mam * pt.available_memory_p3)
        pre_th.save()

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
        data_all["dev_io_read_rate"] = realtime_nw.dev_io_read_rate
        data_all["dev_io_write_rate"] = realtime_nw.dev_io_write_rate
        data_all["dev_io_usage_rate"] = realtime_nw.dev_io_usage_rate
        data_all["mem_usage_rate"] = realtime_memory.mem_usage_rate
        data_all["available_memory"] = realtime_memory.available_memory
        data_all["swap_usage_rate"] = realtime_memory.swap_usage_rate

    print("查询成功！返回实时数据...")
    return HttpResponse(json.dumps(data_all))
