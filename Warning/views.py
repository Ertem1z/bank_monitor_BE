import json

from Warning.models import PercentileThresholds
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views import View


# Create your views here.

class AlertThreshold(View):
    def get(self, request):
        pass

    # create
    def post(self, request):

        ip_address = request.POST.get("ip")
        if PercentileThresholds.objects.filter(ip_address=ip_address):
            data = {'msg': "Record already exists", 'code': 400}
            return HttpResponse(json.dumps(data), status=201)

        contact = request.POST.get("peopleName")
        contact_email = request.POST.get("peopleEmail")
        label_list = {}
        for i in range(0, 3):
            if request.POST.get("rule[%i][label]" % i) is not None:
                rule_label = request.POST.get("rule[%s][label]" % i)
                dic = {}
                for j in range(0, 3):
                    print(i, j)
                    threshold = request.POST.get("rule[%s][value][%s]" % (i, j))
                    if threshold is not None:
                        dic[j] = threshold
                label_list[rule_label] = dic

        # 只要有被更新的资源
        if label_list is not None:
            pThreshold = PercentileThresholds()
            pThreshold.ip_address = ip_address
            pThreshold.contact = contact
            pThreshold.contact_email = contact_email
            for label in label_list:
                for p in label_list[label]:
                    print(label, p)
                    exec("pThreshold.{}_p{} = float(label_list[label][p])".format(label, p + 1))

            pThreshold.save()
            data = {'msg': "ok"}
        return HttpResponse(json.dumps(data), status=201)

    # update
    def put(self, request):

        put = QueryDict(request.body)
        ip_address = put.get("ip")
        pThreshold = PercentileThresholds.objects.get(ip_address=ip_address)
        contact = put.get("peopleName")
        contact_email = put.get("peopleEmail")
        label_list = {}
        for i in range(0, 3):
            if put.get("rule[%i][label]" % i) is not None:
                rule_label = put.get("rule[%s][label]" % i)
                dic = {}
                for j in range(0, 3):
                    print(i, j)
                    threshold = put.get("rule[%s][value][%s]" % (i, j))
                    if threshold is not None:
                        dic[j] = threshold
                label_list[rule_label] = dic

        # 只要有被更新的资源
        if label_list is not None:
            pThreshold.ip_address = ip_address
            pThreshold.contact = contact
            pThreshold.contact_email = contact_email
            for label in label_list:
                for p in label_list[label]:
                    print(label, p)
                    exec("pThreshold.{}_p{} = float(label_list[label][p])".format(label, p + 1))
        pThreshold.save()
        data = {'msg': "ok"}
        return HttpResponse(json.dumps(data), status=201)
