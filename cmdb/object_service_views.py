# --*-- coding: utf-8 --*--
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cmdb.models import Service
import json
import urllib

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def service_get(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    key = request.POST.get('key','all')
    if key == 'all':
        pageIndex = request.POST.get('pageIndex',0)
        pageSize = request.POST.get('pageSize',100)
        start = int(pageIndex)*int(pageSize)
        stop = int(pageIndex)*int(pageSize) + int(pageSize)
        service_r = list(Service.objects.all().values())
        data = {"total":len(service_r),"data":service_r[start:stop]}
        json_r = json.dumps(data)
    elif key == 'id':
        id = request.POST.get('id')
        service_r = list(Service.objects.filter(id=id).values())[0]
        json_r = json.dumps(service_r)
    else:
        service_r = list(Service.objects.filter(Service_Name__contains=key).values())
        json_r = json.dumps(service_r)
    return HttpResponse(json_r)

@csrf_exempt
def service_search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("http://10.100.30.174/ops/cmdb/html/login.html")
    json_str =request.body
    data = json.loads(json_str)
    key = data['key']
    if key == 'id':
        service_r = list(Service.objects.filter(id=data['id']).values())[0]
        json_r = json.dumps(service_r)
    if key == 'Service_Name':
        service_r = list(Service.objects.filter(Service_Name__contains=data['Service_Name']).values())[0]
        json_r = json.dumps(service_r)
    return HttpResponse(json_r)

@csrf_exempt  
def service_save(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_service'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str = request.body
    data = json.loads(json_str)
    if  data['id']:
        i = Service.objects.filter(id=data['id'])
        i.update(Service_Name = data['Service_Name'])
    else:
        i = Service(Service_Name = data['Service_Name'])
        i.save()
    json_r = json.dumps({"result":"save sucess"})
    return HttpResponse(json_r)
@csrf_exempt
def service_del(request):
    if not request.user.is_authenticated():
        json_r = json.dumps({"result":"no login"})
        return HttpResponse(json_r)
    elif not request.user.has_perm('cmdb.change_service'):
        json_r = json.dumps({"result":"no permission"})
        return HttpResponse(json_r)
    json_str =request.body
    data = json.loads(json_str)
    ids = data['id']
    for del_id in ids:
        i = Service.objects.filter(id=del_id)
        i.delete()
    json_r = json.dumps({"result":"delete sucess"})
    return HttpResponse(json_r)
