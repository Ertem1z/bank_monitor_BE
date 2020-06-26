from django.db import models

# Create your models here.
# class AllHardwareDevices(models.Model):
#     label = models.CharField()
from django.utils import timezone


class CPU(models.Model):
    ip_address = models.CharField(max_length=32)
    cpu_used_total = models.FloatField()
    cpu_user_used = models.FloatField()
    cpu_system_used = models.FloatField()
    cpu_average_5min = models.FloatField()
    cpu_io_wait = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['time']

class Network(models.Model):
    ip_address = models.CharField(max_length=32)
    tcp_activeopens = models.IntegerField()
    tcp_passiveopens = models.IntegerField()
    close_wait_count = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['time']

class SystemMemory(models.Model):
    ip_address = models.CharField(max_length=32)
    mem_usage_rate = models.FloatField()
    available_memory = models.FloatField()
    swap_usage_rate = models.FloatField()
    free_swap_spacecon = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['time']

